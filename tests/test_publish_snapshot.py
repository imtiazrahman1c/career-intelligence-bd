import json
import unittest
from collectors.publish_snapshot import publish, public_payload, PROJECT_URL
from test_refresh_snapshot import fixture


class Response:
    def __init__(self,status=201,data=None):
        self.status=status
        self.data=data
    def __enter__(self): return self
    def __exit__(self,*args): pass
    def read(self,n): return json.dumps(self.data).encode()


class PublishTests(unittest.TestCase):
    def test_projection_removes_unexpected_raw_content(self):
        data=fixture();data['raw']='secret';data['results'][0]['description']='raw text'
        result=public_payload(data)
        self.assertNotIn('raw text',str(result))
        self.assertNotIn('secret',str(result))

    def test_publish_and_verify(self):
        calls=[]
        def opener(request,timeout):
            calls.append(request)
            self.assertTrue(request.full_url.startswith(PROJECT_URL))
            return Response() if request.get_method()=='POST' else Response(200,[{'is_published':True}])
        publish(fixture(),'sb_secret_test',opener)
        self.assertEqual(len(calls),2)
        self.assertIn('on_conflict=checked_at',calls[0].full_url)
        self.assertTrue(json.loads(calls[0].data)['is_published'])

    def test_missing_secret_and_failed_verification(self):
        with self.assertRaises(ValueError): publish(fixture(),'sb_publishable_test')
        with self.assertRaises(ValueError):
            publish(fixture(),'sb_secret_test',lambda request,timeout:Response(201,[]))
