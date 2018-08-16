import unittest
from flask import current_app, session
from app import create_app


class post_test_case(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()


    def get_api_headers(self):
        return {
            'Accept': 'text/html',
            'Content-Type': 'text/html;charset=utf-8'
        }

    def test_get_post(self):
        response = self.client.get('/', headers=self.get_api_headers())
        self.assertEqual(response.status_code, 200)
        print("test_get_post    OK")

    def test_login_req(self):
        response = self.client.get('/edit/1', headers=self.get_api_headers())
        self.assertEqual(response.status_code, 302)
        print("test_login_req    OK")

    def test_login(self):
        response = self.client.post('/login',data={
            'name': 'rango',
            'pwd': 'rango',
        },follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/cate/1', headers=self.get_api_headers())
        self.assertEqual(response.status_code, 200)
        print("test_get_cate_post    OK")
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()