import unittest
import json
import re
from base64 import b64encode
from app import create_app, db
from app.models import User, Post, Comment

class api_test_case(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def get_api_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_404(self):
        response = self.client.get(
            '/wrong/url',
            headers=self.get_api_headers())
        self.assertEqual(response.status_code, 404)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['error'], 'not found')
        print("test_404    OK")


    def test_200(self):
        response = self.client.get(
            '/api/v1/get_post/?page=2',
            headers=self.get_api_headers())
        self.assertEqual(response.status_code, 200)
        print("test_200    OK")


    def test_page(self):
        response = self.client.get(
            '/api/v1/get_post/?page=1',
            headers=self.get_api_headers())
        self.assertEqual(response.status_code, 200)
        print("test_page    OK")


    def test_get_comment(self):
        response = self.client.get(
            '/api/v1/get_post_comment/?post_id=1',
            headers=self.get_api_headers())
        self.assertEqual(response.status_code, 200)
        print("test_get_comment    OK")

if __name__ == '__main__':
    unittest.main()