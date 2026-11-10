"""Synthetic boundary regressions, separate from municipal/solver evidence."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from . import data,engine


def dmi(start,value=1,valid=True):
    return {'id':start.isoformat(),'geometry':{'coordinates':[10.3304,55.4748]},'properties':{
        'stationId':'06120','parameterId':'acc_precip','timeResolution':'hour','from':start.isoformat(),
        'to':(start+dt.timedelta(hours=1)).isoformat(),'validity':valid,'value':value}}


class Contracts(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.folder=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def write_dmi(self,records):data.dump(self.folder/'rainfall.json',{'features':records,'timeStamp':'envelope'})

    def test_dmi_start_is_not_shifted_again(self):
        start=dt.datetime(2018,8,1,22,tzinfo=dt.timezone.utc);self.write_dmi([dmi(start,2)])
        self.assertEqual(engine.observations('odense',self.folder),[(start,2.0,False)])

    def test_dmi_invalid_missing_negative_and_nonfinite_rejected(self):
        start=dt.datetime(2018,8,1,tzinfo=dt.timezone.utc)
        for value,valid in [(None,True),(-1,True),(1,False)]:
            with self.subTest(value=value,valid=valid):
                self.write_dmi([dmi(start,value,valid)])
                with self.assertRaises(ValueError):engine.observations('odense',self.folder)

    def test_duplicate_observations_rejected(self):
        row=dmi(dt.datetime(2018,8,1,tzinfo=dt.timezone.utc));self.write_dmi([row,row])
        with self.assertRaises(ValueError):engine.observations('odense',self.folder)

    def test_knmi_24_is_next_day_end_and_trace_has_explicit_midpoint(self):
        with zipfile.ZipFile(self.folder/'rainfall.zip','w') as z:
            z.writestr('uurgeg_260_2011-2020.txt','# STN,YYYYMMDD,HH,RH\n260,20180801,24,-1\n')
        self.assertEqual(engine.observations('utrecht',self.folder),[(dt.datetime(2018,8,1,23,tzinfo=dt.timezone.utc),.025,True)])

    def test_knmi_blank_is_not_zero(self):
        with zipfile.ZipFile(self.folder/'rainfall.zip','w') as z:z.writestr('uurgeg_260_2011-2020.txt','# STN,YYYYMMDD,HH,RH\n260,20180801,24,\n')
        with self.assertRaises(ValueError):engine.observations('utrecht',self.folder)

    def test_incomplete_warmup_cannot_be_selected(self):
        start=dt.datetime(2018,7,31,22,tzinfo=dt.timezone.utc)
        self.write_dmi([dmi(start+dt.timedelta(hours=i)) for i in range(71)])
        with self.assertRaises(ValueError):engine.event('odense',self.folder)

    def test_local_timezone_and_complete_three_day_window(self):
        start=dt.datetime(2018,7,31,22,tzinfo=dt.timezone.utc)
        self.write_dmi([dmi(start+dt.timedelta(hours=i),1 if 24<=i<48 else 0) for i in range(72)])
        rain,event=engine.event('odense',self.folder)
        self.assertEqual(event['wet_day'],'2018-08-02');self.assertEqual(event['forcing_total_mm'],24)
        self.assertEqual(rain[0][0],dt.datetime(2018,8,1));self.assertEqual(event['hourly_intervals'],72)

    def test_dmi_content_fingerprint_excludes_only_envelope_and_preserves_raw_hash(self):
        f=self.folder/'rainfall.json';self.write_dmi([dmi(dt.datetime(2018,8,1,tzinfo=dt.timezone.utc))])
        a=data.weather_fingerprint('odense',f);raw=data.sha(f)
        obj=json.loads(f.read_text());obj['timeStamp']='new';data.dump(f,obj)
        self.assertEqual(a,data.weather_fingerprint('odense',f));self.assertNotEqual(raw,data.sha(f))
        obj['features'][0]['properties']['value']=2;data.dump(f,obj)
        self.assertNotEqual(a,data.weather_fingerprint('odense',f))

    def test_report_paging_preserves_raw_crlf_identity_and_bounds(self):
        f=self.folder/'rows.csv';f.write_bytes(b'id,value\r\na,1\r\n')
        p=data.page(f,0,4);self.assertEqual(p['sha256'],hashlib.sha256(f.read_bytes()).hexdigest())
        self.assertEqual(p['text'],'id,v');self.assertEqual(p['next_offset'],4)
        for offset,limit in [(-1,1),(True,1),(0,12001),(100,1)]:
            with self.assertRaises(ValueError):data.page(f,offset,limit)

    def test_source_target_uses_area_and_id_not_model_results(self):
        src={'SUBCATCHMENTS':[['s','r','n','2']], 'CONDUITS':[['b','n','m','10'],['a','n','m','10'],['huge','m','n','10']],
            'XSECTIONS':[['b','CIRCULAR','1'],['a','CIRCULAR','1'],['huge','CIRCULAR','5']]}
        target=engine.select_target(src)
        self.assertEqual(target['conduit_id'],'a');self.assertEqual(target['scenario_diameter_m'],.75)


if __name__=='__main__':unittest.main()
