import unittest
from flask import current_app
from app import create_app


class basics_test_case(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()


    def test_app_exists(self):
        self.assertFalse(current_app is None)
        print("test_app_exists    OK")

    def test_app_is_testing(self):
        self.assertEqual(False, current_app.config['WTF_CSRF_ENABLED'])
        print("test_app_is_testing    OK")


if __name__ == '__main__':
    unittest.main()