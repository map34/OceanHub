from flask_script import Command, Manager

from oceanhub import app
from oceanhub.scripts.shell import RunOceanHubShell
from oceanhub.scripts.tests import RunOceanHubTests

manager = Manager(app)


class RunOceanHubServer(Command):
    def run(self):
        app.run(
            host='0.0.0.0',
            debug=True,
            port=5000
        )


manager.add_command('shell', RunOceanHubShell())
manager.add_command('runserver', RunOceanHubServer())
manager.add_command('test', RunOceanHubTests())

if __name__ == '__main__':
    manager.run()
