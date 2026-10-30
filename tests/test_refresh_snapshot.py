import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from collectors.refresh_snapshot import save_snapshot, validate
from collectors.probe_sources import summarize, SOURCES


def fixture():
    rows = []
    for source in SOURCES:
        row = summarize(source, {'jobs': []}, analyze=True)
        row['http_status'] = 200
        rows.append(row)
    return {'checked_at': datetime.now(timezone.utc).isoformat(), 'results': rows}


class RefreshTests(unittest.TestCase):
    def test_atomic_valid_replace(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'snapshot.json'
            path.write_text('previous')
            value = fixture()
            save_snapshot(value, path)
            self.assertEqual(json.loads(path.read_text()), value)
            self.assertEqual(len(list(Path(folder).iterdir())), 1)

    def test_failure_preserves_last_good_snapshot(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'snapshot.json'
            path.write_text('previous')
            value = fixture()
            value['results'][0]['http_status'] = 503
            with self.assertRaises(ValueError):
                save_snapshot(value, path)
            self.assertEqual(path.read_text(), 'previous')

    def test_missing_source_rejected(self):
        value = fixture()
        value['results'].pop()
        with self.assertRaises(ValueError):
            validate(value)

    def test_invalid_counts_rejected(self):
        value = fixture()
        value['results'][0]['analysis']['skill_mention_counts']['sql'] = True
        with self.assertRaises(ValueError):
            validate(value)

    def test_stale_collection_rejected(self):
        value = fixture()
        value['checked_at'] = '2000-01-01T00:00:00Z'
        with self.assertRaises(ValueError):
            validate(value)
