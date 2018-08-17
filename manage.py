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
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
