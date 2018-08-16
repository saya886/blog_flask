from flask_script import Manager, Shell, Server
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand

import click
import os
import sys

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)


# @app.cli.command()
# def test():
#     """Run the unit tests."""
#     import unittest
#     from test import test_basics

@manager.command
def test(coverage):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
