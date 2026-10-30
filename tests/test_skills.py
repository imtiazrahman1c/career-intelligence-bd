import unittest
from analysis.skills import skill_mentions, bangladesh_location_signal


class SkillsTests(unittest.TestCase):
    def test_unique_and_case_insensitive(self):
        self.assertEqual(skill_mentions('SQL sql Python PYTHON'), ['python', 'sql'])

    def test_word_boundaries(self):
        self.assertEqual(skill_mentions('excellent NoSQL PostgreSQL'), [])

    def test_html_and_hidden_content(self):
        self.assertEqual(skill_mentions('<p>Google&nbsp;Ads</p><script>SQL</script>'), ['google_ads'])

    def test_no_requirement_inference(self):
        self.assertEqual(skill_mentions('SQL is not required'), ['sql'])

    def test_missing_description(self):
        self.assertEqual(skill_mentions(None), [])

    def test_location_is_not_eligibility(self):
        self.assertEqual(bangladesh_location_signal(['BD']), 'bangladesh_listed_review_required')
        self.assertEqual(bangladesh_location_signal('Worldwide'), 'worldwide_listed_review_required')

    def test_uncertain_locations_stay_unknown(self):
        for value in (None, [], '', 'Remote', 'APAC', 'US only', 'Not Bangladesh', ['US', None]):
            self.assertEqual(bangladesh_location_signal(value), 'unknown')


if __name__ == '__main__':
    unittest.main()
