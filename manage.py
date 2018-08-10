import os

from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import *
from flask_script import Manager, Shell, Server

app = create_app("config")
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))
# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role)
# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)




# @app.cli.command()
# def run():
#     app.run


@app.cli.command()
def deploy():
    #更新数据库
    upgrade()


if __name__ == '__main__':
    manager.run()
