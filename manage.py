import os

from app.models import Post
from flask_script import Manager, Shell, Server
from app import app, db
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
