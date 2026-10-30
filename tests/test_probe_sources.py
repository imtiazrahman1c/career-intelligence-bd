import unittest
from collectors.probe_sources import summarize


class ProbeTests(unittest.TestCase):
    def test_analysis_deduplicates_and_excludes_missing_id(self):
        result = summarize('jobicy', {'jobs': [
            {'id': 1, 'jobDescription': 'SQL sql', 'jobGeo': 'Worldwide'},
            {'id': 1, 'jobDescription': 'Python'},
            {'jobDescription': 'Python'},
        ]}, analyze=True)['analysis']
        self.assertEqual(result['unique_records_analyzed'], 1)
        self.assertEqual(result['skill_mention_counts']['sql'], 1)
        self.assertEqual(result['skill_mention_counts']['python'], 0)
        self.assertEqual(result['location_signal_counts'], {'worldwide_listed_review_required': 1})

    def test_rejects_error_response_even_with_jobs(self):
        with self.assertRaises(ValueError):
            summarize('jobicy', {'success': False, 'jobs': []})

    def test_rejects_invalid_rows(self):
        with self.assertRaises(ValueError):
            summarize('jobicy', {'jobs': [None]})

    def test_empty_feed_is_not_missing_schema(self):
        result = summarize('himalayas', {'jobs': []})
        self.assertEqual(result['sample_records'], 0)
        self.assertEqual(result['nonempty_field_counts']['description'], 0)

    def test_detects_duplicates_and_missing_fields(self):
        result = summarize('jobicy', {'jobs': [
            {'id': 3, 'jobTitle': 'A', 'jobDescription': ''},
            {'id': 3, 'jobTitle': 'B', 'jobDescription': 'SQL'},
            {'jobTitle': 'C'},
        ], 'nextCursor': 'opaque'})
        self.assertEqual(result['duplicate_ids'], 1)
        self.assertEqual(result['nonempty_field_counts']['id'], 2)
        self.assertEqual(result['nonempty_field_counts']['description'], 1)
        self.assertTrue(result['has_next_cursor'])
        self.assertNotIn('SQL', str(result))


if __name__ == '__main__':
    unittest.main()
