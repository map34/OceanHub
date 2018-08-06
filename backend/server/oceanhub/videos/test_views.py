import json
import unittest

from oceanhub import app


class VideosTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_test_endpoint(self):
        resp = self.app.get('videos/test')
        assert resp.status_code == 200
        assert json.loads(resp.data)[0]['id'] == 'example_id'
