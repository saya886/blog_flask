from flask_script import Manager, Shell, Server
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')

manager = Manager(app)

migrate = Migrate(app, db)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
