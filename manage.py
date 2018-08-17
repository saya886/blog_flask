from flask_script import Manager, Shell, Server
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand

import click
import os
import sys


app = create_app('development')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
