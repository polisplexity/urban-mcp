"""Protect public SWMM source/observation identities; these are not engine tests."""
import csv
import hashlib
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1];CASE=ROOT/'cases/two-city-swmm'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


class SwmmEvidence(unittest.TestCase):
    def test_full_native_rows_and_comparison_hashes_survive_git(self):
        for city in ['odense','utrecht']:
            out=CASE/'evidence'/city;c=load(out/'comparison.json')
            with (out/'comparison.csv').open(encoding='utf-8',newline='') as stream:rows=list(csv.DictReader(stream))
            self.assertEqual(len(rows),c['nodes']);self.assertEqual(sha(out/'comparison.csv'),c['comparison_csv']['sha256'])
            self.assertEqual(sum(r['newly_at_or_above_10m3']=='True' for r in rows),c['newly_at_or_above_10m3'])
            for scenario in ['baseline','capacity75']:
                summary=load(out/(scenario+'-summary.json'))
                for name,receipt in summary['artifacts'].items():
                    p=out/(scenario+'-'+name);self.assertEqual(sha(p),receipt['sha256']);self.assertEqual(p.stat().st_size,receipt['bytes'])

    def test_four_actual_host_files_and_claim_verdicts_are_hash_bound(self):
        agents=load(CASE/'evidence/agents.json');self.assertEqual(len(agents['runs']),4)
        self.assertEqual({(r['host'],r['city']) for r in agents['runs']},{(h,c) for h in ['codex','hermes'] for c in ['odense','utrecht']})
        for row in agents['runs']:
            folder=CASE/'evidence'/row['city']/row['host']
            for name,receipt in row['files'].items():self.assertEqual(sha(folder/name),receipt['sha256'])
            review=load(folder/'review.json');self.assertTrue(review['checks_passed']);self.assertTrue(review['structured_claims']['passed'])
            self.assertEqual(review['successful_tool_families'],27)
            self.assertTrue(review['task_ordering']['session_status_read_before_close'])
            self.assertTrue(load(folder/'query-oracle.json')['passed'])

    def test_source_and_public_task_fingerprints_are_current(self):
        for city in ['odense','utrecht']:
            native=load(CASE/'evidence'/city/'native-mcp.json')
            self.assertTrue(native['passed']);self.assertTrue(all(c['passed'] for c in native['checks']))
            for name in ['data.py','engine.py','server.py','checks.py']:
                self.assertEqual(sha(ROOT/'urban_mcp_swmm'/name),native['source_sha256'][name])
            self.assertEqual(load(CASE/'evidence'/city/'quality.json')['source_binding']['recipe_sha256'],sha(CASE/'recipe.json'))
            for host in ['codex','hermes']:
                process=load(CASE/'evidence'/city/host/(host+'-process.json'))
                self.assertEqual(sha(ROOT/process['task_path']),process['task_template_sha256'])
                prompt=(ROOT/process['task_path']).read_text(encoding='utf-8').replace('{{city}}',city)+'\nYour host name is '+host+'.\n'
                self.assertEqual(hashlib.sha256(prompt.encode()).hexdigest(),process['submitted_prompt_sha256'])

    def test_negative_prose_verdicts_cannot_be_replaced_with_numeric_success(self):
        rows=load(CASE/'evidence/narrative-review.json')['runs']
        for r in rows:
            p=CASE/'evidence'/r['city']/r['host']/(r['host']+'-answer.md');self.assertEqual(sha(p),r['answer_sha256'])
            self.assertEqual(r['passed'],r['facts_passed'] and r['length_passed'])
            if r['host']=='hermes':self.assertFalse(r['passed']);self.assertTrue(r['issues'])

    def test_case_admission_is_not_final_product_or_forecast_qualification(self):
        register=load(ROOT/'registry/product-qualification.json')
        entry=next(r for r in register['capabilities'] if r['id']=='historical-drainage-capacity')
        self.assertFalse(entry['product_qualified']);self.assertEqual(entry['tracking_issue'],'https://github.com/polisplexity/urban-mcp/issues/46')
        for city in ['odense','utrecht']:
            case=load(ROOT/'cases'/(city+'-swmm')/'case.json')
            self.assertTrue(case['ready_to_run']);self.assertEqual(case['status'],'admitted')
            for key in ['product_qualified','forecast_admitted','calibration_revalidated']:self.assertIs(case[key],False)


if __name__=='__main__':unittest.main()
