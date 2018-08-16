import unittest
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash


class user_test_case(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()


    def test_password_setter(self):
        u = User(pwd='cat')
        self.assertTrue(u.pwd is not None)
        print("test_password_setter    OK")


    def test_password_verification(self):
        pwd_hash = generate_password_hash('cat')
        u = User(pwd=pwd_hash)

        self.assertTrue(u.check_pwd('cat'))
        self.assertFalse(u.check_pwd('dog'))
        print("test_password_verification    OK")

if __name__ == '__main__':
    unittest.main()