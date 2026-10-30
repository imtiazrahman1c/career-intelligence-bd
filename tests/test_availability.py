import unittest
from collectors.availability import check_jobicy


class AvailabilityTests(unittest.TestCase):
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
