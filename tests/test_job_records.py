import unittest
from collectors.job_records import normalize_jobs


class JobRecordsTests(unittest.TestCase):
    def row(self, **extra):
        return dict(id=1,jobTitle='Analyst &amp; Research',companyName='Example',url='https://jobicy.com/jobs/example',**extra)

    def test_minimal_metadata_and_duplicates(self):
        row=self.row(jobDescription='private raw text',jobGeo='Worldwide')
        result=normalize_jobs('jobicy',[row,row])
        self.assertEqual(len(result),1)
        self.assertEqual(result[0]['title'],'Analyst & Research')
        self.assertNotIn('private raw text',str(result))

    def test_invalid_apply_urls(self):
        for url in ('javascript:alert(1)','https://jobicy.com.evil.test/a','https://user@jobicy.com/a','http://jobicy.com/a','https://jobicy.com:8080/a'):
            row=self.row(); row['url']=url
            self.assertEqual(normalize_jobs('jobicy',[row]),[])

    def test_expired_job_removed(self):
        self.assertEqual(normalize_jobs('jobicy',[self.row(expiryDate=1)]),[])
