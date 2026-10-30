import unittest
from collectors.availability import check_jobicy, check_himalayas, fetch_himalayas_status


class AvailabilityTests(unittest.TestCase):
    def test_himalayas_status_handling(self):
        jobs=[{'source':'himalayas','source_id':str(n)} for n in (1,2,3)]
        result=check_himalayas(jobs,lambda identity:{'1':'active','2':'closed','3':'unknown'}[identity])
        self.assertEqual([j['source_id'] for j in result],['1','3'])
        self.assertEqual(result[0]['availability'],'active_at_collection')

    def test_himalayas_failure_and_url_guard(self):
        def failed(identity):
            raise TimeoutError()
        self.assertEqual(check_himalayas([{'source':'himalayas','source_id':'x'}],failed)[0]['availability'],'unknown')
        self.assertEqual(fetch_himalayas_status('https://evil.test/companies/a/jobs/b'),'unknown')

    def jobs(self):
        return [{'source':'jobicy','source_id':str(n)} for n in (1,2,3)]

    def test_active_closed_unknown(self):
        result=check_jobicy(self.jobs(),lambda ids:{'success':True,'statusCode':200,'jobs':[{'id':1,'status':'active'},{'id':2,'status':'closed'}]})
        self.assertEqual([r['source_id'] for r in result],['1','3'])
        self.assertEqual([r['availability'] for r in result],['active_at_collection','unknown'])

    def test_network_failure_is_unknown(self):
        def failed(ids):
            raise TimeoutError()
        self.assertTrue(all(r['availability']=='unknown' for r in check_jobicy(self.jobs(),failed)))

    def test_duplicate_status_is_unknown(self):
        result=check_jobicy(self.jobs(),lambda ids:{'success':True,'statusCode':200,'jobs':[{'id':1,'status':'active'},{'id':1,'status':'closed'}]})
        self.assertEqual(result[0]['availability'],'unknown')

    def test_unsuccessful_payload_not_trusted(self):
        result=check_jobicy(self.jobs(),lambda ids:{'success':False,'statusCode':500,'jobs':[{'id':1,'status':'active'}]})
        self.assertEqual(result[0]['availability'],'unknown')
