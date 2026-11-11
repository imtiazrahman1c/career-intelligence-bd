import unittest
from analysis.trends import compare_periods


class TrendTests(unittest.TestCase):
    def setUp(self):
        self.old = dict(source_set=['a','b'], geography='global', method_version='v1', coverage_version='v1', metric='unique_postings', unit='count', start='2026-09-01', end='2026-09-07', value=100, complete=True, deduplicated=True)
        self.new = dict(self.old, start='2026-09-08', end='2026-09-14', value=120)

    def test_comparable(self):
        self.assertEqual(compare_periods(self.old, self.new)['percent_change'], 20)

    def test_source_and_coverage_change(self):
        for key in ('source_set','coverage_version','method_version','geography'):
            with self.subTest(key=key):
                self.assertEqual(compare_periods(self.old, dict(self.new, **{key:'changed'}))['state'], 'unavailable')

    def test_partial_duplicates_and_overlap(self):
        for delta in ({'complete':False},{'deduplicated':False},{'start':'2026-09-07'},{'value':True}):
            self.assertEqual(compare_periods(self.old, dict(self.new, **delta))['state'], 'unavailable')

    def test_zero_baseline(self):
        result=compare_periods(dict(self.old,value=0),self.new)
        self.assertIsNone(result['percent_change'])
        self.assertEqual(result['absolute_change'],120)
