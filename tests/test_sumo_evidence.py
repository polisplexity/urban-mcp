"""Protect real observed trip accounting, complete host payloads and explicit limits."""
from collections import Counter
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1];CASE=ROOT/"cases/two-city-sumo"
sys.path.insert(0,str(ROOT/"tools"))
from review_sumo_agents import TOOLS, claims, expected_claims, pages, semantic, success


def load(path):return json.loads(path.read_text(encoding="utf-8"))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def rows(path):
    with path.open(encoding="utf-8",newline="") as stream:return list(csv.DictReader(stream))


class SumoEvidenceTests(unittest.TestCase):
    def test_both_live_harvest_modes_preserve_exact_publisher_assets(self):
        receipt=load(CASE/"evidence/live-mcp.json")
        self.assertTrue(receipt["passed"]);self.assertTrue(receipt["cli_acquisition_and_preparation_also_executed"])
        self.assertEqual({r["city"] for r in receipt["observations"]},{"bologna","ingolstadt"})
        for record in receipt["observations"]:
            folder=CASE/"evidence"/record["city"];frozen=load(folder/"harvest.json")
            for mode in ["cli","mcp"]:
                path=folder/("live-"+mode+"-harvest.json");live=load(path)
                self.assertEqual(live["files"],frozen["files"])
                self.assertEqual(len(live["requests"]),len(frozen["files"]))
                self.assertTrue(all(r["status"]==200 for r in live["requests"]))
                self.assertEqual(sha(path),record["live_"+mode+"_manifest_sha256"])
            self.assertEqual(sha(folder/"live-mcp-harvest.json"),record["harvest_response"]["input_manifest_sha256"])
            self.assertTrue(record["prepared_files_identical_to_locked_snapshot"])

    def test_native_contracts_and_all_published_artifact_bytes(self):
        for city,count in [("bologna",80),("ingolstadt",73)]:
            folder=CASE/"evidence"/city;record=load(folder/"native-mcp.json")
            self.assertTrue(record["passed"]);self.assertFalse(record["quick_protocol_only"])
            self.assertEqual(len(record["checks"]),count);self.assertTrue(all(c["passed"] for c in record["checks"]))
            self.assertEqual(set(record["tools_exercised"]),TOOLS)
            for name,digest in record["artifact_sha256"].items():self.assertEqual(sha(folder/name),digest)
            for name,digest in record["source_sha256"].items():self.assertEqual(sha(ROOT/"urban_mcp_sumo"/name),digest)

    def test_every_scheduled_trip_and_paired_threshold_is_accounted(self):
        for city in ["bologna","ingolstadt"]:
            folder=CASE/"evidence"/city;comparison=load(folder/"comparison.json")
            cohorts=[]
            for label in ["baseline","works"]:
                summary=load(folder/(label+"-summary.json"));all_rows=rows(folder/(label+"-all-vehicles.csv"));cohort=rows(folder/(label+"-cohort.csv"))
                self.assertEqual(len({r["vehicle_id"] for r in all_rows}),len(all_rows))
                self.assertEqual(len(all_rows),summary["scheduled_vehicles"])
                self.assertEqual(dict(Counter(r["state"] for r in all_rows)),summary["all_scheduled_states"])
                self.assertEqual({k:sum(r["state"]==k for r in cohort) for k in summary["corridor_cohort_states"]},summary["corridor_cohort_states"])
                for row in all_rows:
                    if row["state"]=="arrived":self.assertAlmostEqual(float(row["scheduled_to_arrival_s"]),float(row["arrival"])-float(row["scheduled_depart"]),places=7)
                    else:self.assertEqual(row["duration"],"");self.assertEqual(row["scheduled_to_arrival_s"],"")
                self.assertIs(summary["model_quality"]["forecast_admitted"],False)
                self.assertIs(summary["model_quality"]["calibration_revalidated"],False)
                cohorts.append({r["vehicle_id"]:r for r in cohort})
            compared=rows(folder/"comparison.csv");deltas=[];censored=teleported=0
            self.assertEqual({r["vehicle_id"] for r in compared},set(cohorts[0]));self.assertEqual(len(compared),len(cohorts[0]))
            for row in compared:
                a,b=[c[row["vehicle_id"]] for c in cohorts]
                completed=a["state"]==b["state"]=="arrived";teleport=a["teleport_warning_seen"]=="True" or b["teleport_warning_seen"]=="True"
                eligible=completed and not teleport
                self.assertEqual(row["eligible_paired_comparison"],str(eligible))
                if eligible:
                    delta=round(float(b["arrival"])-float(a["arrival"]),8);deltas.append(delta)
                    self.assertEqual(float(row["scheduled_to_arrival_delta_s"]),delta)
                    self.assertEqual(row["increased_over_30s"],str(delta>30))
                else:
                    self.assertEqual(row["increased_over_30s"],"");self.assertEqual(row["scheduled_to_arrival_delta_s"],"")
                    censored+=not completed;teleported+=completed and teleport
            self.assertEqual(len(deltas),comparison["eligible_paired_comparison"])
            self.assertEqual(sum(v>30 for v in deltas),comparison["increased_over_30s"])
            self.assertEqual(censored,comparison["excluded_censored_pairs"]);self.assertEqual(teleported,comparison["excluded_teleport_identified_completed_pairs"])
            self.assertAlmostEqual(sum(deltas)/len(deltas),comparison["mean_matched_scheduled_to_arrival_delta_s"])

    def test_all_four_hosts_returned_complete_native_payloads_and_pages(self):
        for city in ["bologna","ingolstadt"]:
            folder=CASE/"evidence"/city
            for host in ["codex","hermes"]:
                trace=load(folder/(host+"-trace.json"));calls=trace["calls"];review=load(folder/(host+"-review.json"))
                self.assertTrue(review["computational_workflow_passed"]);self.assertFalse(review["errors"])
                self.assertEqual({c["tool"] for c in calls if success(c)},TOOLS)
                self.assertEqual(sha(folder/(host+"-trace.json")),review["trace_sha256"])
                self.assertEqual(sha(folder/(host+"-process.json")),review["process_sha256"])
                for run_id,label in [("agent-baseline","baseline"),("agent-works","works")]:
                    actual=[c["result"] for c in calls if success(c) and c["tool"]=="run_sumo_scenario" and c["arguments"].get("run_id")==run_id]
                    self.assertEqual(len(actual),1);self.assertEqual(semantic(actual[0]),semantic(load(folder/(label+"-summary.json"))))
                actual=[c["result"] for c in calls if success(c) and c["tool"]=="compare_sumo_runs"]
                self.assertEqual(len(actual),1);self.assertEqual(semantic(actual[0]),semantic(load(folder/"comparison.json")))
                complete=pages(calls,"read_sumo_artifact",{"city":city,"run_id":"agent-works","name":"comparison.csv"},folder/"comparison.csv")
                self.assertTrue(complete["all_pages_match"])
                self.assertEqual(len(complete["pages"]),8 if city=="bologna" else 2)
                self.assertTrue(pages(calls,"read_sumo_source",{"city":city,"name":"manifest.json"},folder/"harvest.json")["all_pages_match"])

    def test_structured_claims_are_strict_and_nan_bool_or_duplicate_lanes_fail(self):
        for city in ["bologna","ingolstadt"]:
            folder=CASE/"evidence"/city;expected=expected_claims(load(folder/"baseline-summary.json"),load(folder/"works-summary.json"),load(folder/"comparison.json"))
            for host in ["codex","hermes"]:
                self.assertTrue(claims((folder/(host+"-answer.md")).read_text(encoding="utf-8"),expected)["passed"])
            for key,value in [("scheduled_vehicles",True),("increased_over_30s",float(expected["increased_over_30s"])),("mean_matched_scheduled_to_arrival_delta_s",float("nan")),("target_lane_ids",expected["target_lane_ids"]*2)]:
                changed={**expected,key:value};answer="```json\n"+json.dumps(changed)+"\n```"
                self.assertFalse(claims(answer,expected)["passed"])

    def test_model_problems_and_manual_prose_verdicts_cannot_be_silently_promoted(self):
        narrative=load(CASE/"evidence/narrative-review.json")
        self.assertFalse(narrative["independent_person_review"])
        for entry in narrative["entries"]:
            answer=CASE/"evidence"/entry["city"]/(entry["host"]+"-answer.md")
            self.assertEqual(sha(answer),entry["answer_sha256"])
            words=len(re.sub(r"```json.*?```","",answer.read_text(encoding="utf-8"),flags=re.S).split())
            self.assertEqual(words,entry["length_constraint"]["observed_words"])
            self.assertEqual(entry["length_constraint"]["passed"],words<=600)
            self.assertEqual(entry["factual_status"],"failed" if entry["findings"] else "passed")
            self.assertEqual(entry["status"],"passed" if entry["host"]=="codex" else "failed_facts_and_length")
        for label in ["baseline","works"]:
            quality=load(CASE/"evidence/ingolstadt"/(label+"-summary.json"))["model_quality"]
            self.assertEqual(quality["incompatible_signal_program_warning_count"],577)
            self.assertEqual(quality["native_teleport_events"],20);self.assertEqual(quality["native_collisions"],2)
        capability=next(c for c in load(ROOT/"registry/product-qualification.json")["capabilities"] if c["id"]=="historical-traffic-works")
        self.assertIs(capability["product_qualified"],False);self.assertIsNone(capability["independent_operator"])


if __name__=="__main__":unittest.main()
