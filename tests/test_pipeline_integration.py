"""Collector/public projection/JS model contract, using synthetic data only."""
import json
import shutil
import subprocess
import unittest
from datetime import datetime, timezone
from pathlib import Path
from collectors.probe_sources import summarize
from collectors.publish_snapshot import public_payload


@unittest.skipUnless(shutil.which('node'), 'Node is required for the frontend contract')
class PipelineTests(unittest.TestCase):
    def test_formatted_mentions_survive_publication_and_frontend(self):
        rows = []
        fixtures = [
            ('himalayas', {'jobs': [{'guid': 'synthetic-a', 'description':
                'Py<strong>thon</strong><div hidden>SQL</div>'}]}),
            ('jobicy', {'jobs': [{'id': 'synthetic-b', 'jobDescription':
                'S<span>QL</span><template>Python</template>'}]}),
        ]
        for source, fixture in fixtures:
            row = summarize(source, fixture, analyze=True)
            row['http_status'] = 200
            rows.append(row)
        payload = public_payload({'checked_at': datetime.now(timezone.utc).isoformat(),
                                  'results': rows})
        self.assertNotIn('description', payload['results'][0])
        code = """
import assert from 'node:assert/strict';
import {analysisTotals} from './web/model.mjs';
let text='';for await(const part of process.stdin)text+=part;
const rows=JSON.parse(text).results;
const a=analysisTotals(rows);
assert.equal(a.methodVersion,'editorial-mentions-v2');
assert.equal(a.records,2);
assert.equal(a.skills.find(x=>x.id==='sql').count,1);
assert.equal(a.skills.find(x=>x.id==='python').count,1);
rows[0].analysis.method_version='editorial-mentions-v1';
assert.equal(analysisTotals(rows),null);
"""
        result = subprocess.run(['node', '--input-type=module', '-e', code],
            input=json.dumps(payload), text=True, capture_output=True,
            cwd=Path(__file__).resolve().parents[1], timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
