from flask_migrate import MigrateCommand
from App import create_app
from flask_script import Manager

app = create_app("develop")
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()
