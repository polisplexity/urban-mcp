"""Synthetic edge-case and lifecycle regressions; not municipal observations."""
import builtins
from contextlib import redirect_stdout, redirect_stderr
import hashlib
import io
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import warnings
import xml.etree.ElementTree as ET
import zipfile

import traci.main
from . import data, engine
from .compat import install_traci_stderr


class SumoContracts(unittest.TestCase):
    def test_strict_scheduled_arrival_threshold_censor_and_teleport_denominators(self):
        with tempfile.TemporaryDirectory() as temp, patch.dict(os.environ,{"URBAN_MCP_DATA":temp}):
            rows=[]
            for key,state,teleported in [("equal","arrived",False),("above","arrived",False),("censored","unfinished",False),("teleported","arrived",True)]:
                rows.append({"vehicle_id":key,"state":state,"arrival":100 if state=="arrived" else -1,"duration":80 if state=="arrived" else None,"departDelay":20 if state=="arrived" else None,"scheduled_to_arrival_s":100 if state=="arrived" else None,"teleport_warning_seen":teleported})
            for run,scenario in [("base","baseline"),("works","works30")]:
                folder=Path(temp)/"results/bologna"/run;folder.mkdir(parents=True)
                output=[dict(r) for r in rows]
                if run=="works":
                    for row in output:
                        if row["state"]=="arrived":
                            row["arrival"]+=30.01 if row["vehicle_id"]=="above" else 30
                            row["scheduled_to_arrival_s"]=row["arrival"]
                            row["duration"]+=10
                            row["departDelay"]+=20.01 if row["vehicle_id"]=="above" else 20
                engine.write_csv(folder/"cohort.csv",output)
                data.dump(folder/"summary.json",{"city":"bologna","scenario":scenario,"input_manifest_sha256":"synthetic","implementation_sha256":"synthetic","seed":37,"begin":0,"end":200,"target_edge":{"id":"synthetic"},"corridor_cohort_states":{"arrived":3,"unfinished":1,"undeparted":0,"removed":0,"not_recorded":0},"model_quality":{"native_teleport_events":1}})
            result=engine.compare("bologna","base","works")
            self.assertEqual(result["eligible_paired_comparison"],2)
            self.assertEqual(result["excluded_censored_pairs"],1)
            self.assertEqual(result["excluded_teleport_identified_completed_pairs"],1)
            self.assertEqual(result["increased_over_30s"],1)
            self.assertAlmostEqual(result["mean_matched_scheduled_to_arrival_delta_s"],30.005)
            self.assertEqual(result["mean_matched_in_network_duration_delta_s"],10)

    def test_native_end_vaporization_is_not_confused_with_completed_arrival(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            root=ET.Element("tripinfos")
            for key,depart,arrival,vaporized in [("pending",-1,-1,"end"),("running",0,-1,"end"),("removed",0,10,"collision"),("arrived",0,10,"")]:
                ET.SubElement(root,"tripinfo",id=key,depart=str(depart),arrival=str(arrival),vaporized=vaporized,duration="10",departDelay="0",waitingTime="0",timeLoss="0",routeLength="100")
            engine.xml_write(folder/"tripinfo.xml",root)
            (folder/"sumo-errors.log").write_text("Warning: Teleporting vehicle 'arrived'; synthetic fixture\n",encoding="utf-8")
            schedule=[{"vehicle_id":key,"scheduled_depart":0,"corridor_cohort":True} for key in ["pending","running","removed","arrived"]]
            with patch.object(engine,"read_schedule",return_value=schedule):rows=engine.trip_rows("bologna",folder)
            self.assertEqual([r["state"] for r in rows],["undeparted","unfinished","removed","arrived"])
            self.assertIsNone(rows[1]["duration"])
            self.assertIsNone(rows[2]["duration"])
            self.assertTrue(rows[3]["teleport_warning_seen"])

    def test_unsafe_identifiers_unknown_city_and_scenario_are_rejected(self):
        for value in ["../outside","", "x"*49]:
            with self.assertRaisesRegex(ValueError,"run_id"):data.token(value)
        with self.assertRaisesRegex(ValueError,"Unknown city"):data.config("outside")
        with self.assertRaisesRegex(ValueError,"scenario"):engine.make_run("bologna","fixture","random")

    def test_original_traci_retry_stdout_is_routed_to_stderr(self):
        out,err=io.StringIO(),io.StringIO()
        with patch.object(traci.main,"print",builtins.print,create=True), patch.object(traci.main,"_urban_mcp_stderr_installed",False,create=True):
            with patch.object(traci.main.connection,"Connection",side_effect=[socket.error("synthetic"),object()]):
                with redirect_stdout(out),redirect_stderr(err):traci.main.connect(numRetries=1,waitBetweenRetries=0)
            self.assertIn("Retrying",out.getvalue())
            install_traci_stderr();out,err=io.StringIO(),io.StringIO()
            with patch.object(traci.main.connection,"Connection",side_effect=[socket.error("synthetic"),object()]):
                with redirect_stdout(out),redirect_stderr(err):traci.main.connect(numRetries=1,waitBetweenRetries=0)
            self.assertEqual(out.getvalue(),"")
            self.assertIn("Retrying",err.getvalue())

    def test_shutdown_terminates_a_real_owned_child_and_prevents_new_registration(self):
        process=subprocess.Popen([sys.executable,"-c","import time; time.sleep(60)"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        original=engine.SHUTTING_DOWN
        try:
            engine.ACTIVE_PROCESSES[process.pid]=process
            engine.stop_owned_batches()
            self.assertIsNotNone(process.poll())
            self.assertEqual(engine.ACTIVE_PROCESSES,{})
            self.assertTrue(engine.SHUTTING_DOWN)
        finally:
            engine.SHUTTING_DOWN=original
            if process.poll() is None:process.kill();process.wait()

    def snapshot_fixture(self,entries,error,corrupt=False):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp);case=folder/"case";case.mkdir()
            (case/"recipe.json").write_bytes((data.CASE/"recipe.json").read_bytes())
            buffer=io.BytesIO()
            with warnings.catch_warnings():
                warnings.simplefilter("ignore",UserWarning)
                with zipfile.ZipFile(buffer,"w") as archive:
                    for name,value in entries:archive.writestr(name,value)
            blob=buffer.getvalue()
            data.dump(case/"snapshot.lock.json",{"bologna":{"url":"https://example.invalid/synthetic.zip","bytes":len(blob),"sha256":"0"*64 if corrupt else hashlib.sha256(blob).hexdigest(),"manifest_sha256":"0"*64}})
            with patch.object(data,"CASE",case),patch.dict(os.environ,{"URBAN_MCP_DATA":str(folder/"workspace")}),patch.object(data,"urlopen",return_value=io.BytesIO(blob)):
                with self.assertRaisesRegex(ValueError,error):data.restore("bologna")

    def test_snapshot_traversal_is_rejected(self):
        self.snapshot_fixture([("../outside",b"fixture")],"Unsafe snapshot member")

    def test_snapshot_duplicate_members_are_rejected(self):
        self.snapshot_fixture([("same",b"a"),("same",b"b")],"duplicate/member/expansion")

    def test_snapshot_symlink_is_rejected(self):
        info=zipfile.ZipInfo("link");info.external_attr=0o120777<<16
        self.snapshot_fixture([(info,b"../outside")],"Unsafe snapshot member")

    def test_snapshot_hash_is_checked_before_extraction(self):
        self.snapshot_fixture([("anything",b"synthetic")],"size/hash mismatch",corrupt=True)

    def test_source_manifest_identity_and_receipts_reject_tampering(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp);case=folder/"case";case.mkdir();inputs=folder/"inputs";inputs.mkdir()
            source=inputs/"source.xml";source.write_bytes(b"synthetic")
            asset={"file":"source.xml","url":"https://example.invalid/synthetic.xml","bytes":source.stat().st_size,"sha256":data.sha(source)}
            cfg={"publisher_commit":"fixture","publisher_repository":"fixture/fixture","license":"MIT","attribution":"Synthetic fixture","assets":[asset]}
            data.dump(case/"recipe.json",{"id":"fixture","cities":{"bologna":cfg}})
            manifest={"case":"fixture","city":"bologna","recipe_sha256":data.sha(case/"recipe.json"),**{k:cfg[k] for k in ["publisher_commit","publisher_repository","license","attribution"]},"files":{"source.xml":{k:asset[k] for k in ["url","bytes","sha256"]}}}
            with patch.object(data,"CASE",case):
                data.dump(inputs/"manifest.json",manifest);data.verify("bologna",inputs)
                changed=json.loads(json.dumps(manifest));changed["case"]="other"
                data.dump(inputs/"manifest.json",changed)
                with self.assertRaisesRegex(ValueError,"identity mismatch"):data.verify("bologna",inputs)
                changed=json.loads(json.dumps(manifest));changed["files"]["source.xml"]["url"]="https://example.invalid/other"
                data.dump(inputs/"manifest.json",changed)
                with self.assertRaisesRegex(ValueError,"integrity failure"):data.verify("bologna",inputs)


if __name__=="__main__":unittest.main()
