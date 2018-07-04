import unittest
import json
from app import create_app


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_get(self):
        response = self.client.get('/')
        print(vars(response))
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['data']['status'], 'ok')

    def test_head(self):
        # HEAD Test - Returns status/ok, 200
        response = self.client.head('/')
        self.assertEqual(response.status_code, 200)

    def test_unusedmethods(self):
        response = self.client.put('/')
        self.assertEqual(response.status_code, 405)

        response = self.client.delete('/')
        self.assertEqual(response.status_code, 405)

        response = self.client.options('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.trace('/')
        self.assertEqual(response.status_code, 405)

    def test_404(self):
        response = self.client.get('/wrong/path')
        self.assertEqual(response.status_code, 404)
