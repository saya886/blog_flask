from tests.test_basics import basics_test_case
from tests.test_api import api_test_case
from tests.test_user import user_test_case
from tests.test_post import post_test_case
import os
import unittest
from coverage import coverage
cov = coverage(branch = True, include='app/*')
cov.start()

basedir = os.path.abspath(os.path.dirname(__file__))


if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print ("\n\nCoverage Report:\n")
    cov.report()
    print ("HTML version: " + os.path.join(basedir, "tmp/coverage/index.html"))
    cov.html_report(directory = 'tmp/coverage')
    cov.erase()
