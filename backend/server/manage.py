from flask_script import Command, Manager, Shell

from oceanhub import app
from oceanhub.scripts.shell import make_shell_context

manager = Manager(app)


class StartShell(Command):
    def run(self):
        Shell(make_context=make_shell_context).run(False, False, False, False)


class RunServer(Command):
    def run(self):
        app.run(
            host='0.0.0.0',
            debug=True,
            port=5000
        )


manager.add_command('shell', StartShell())
manager.add_command('runserver', RunServer())

if __name__ == '__main__':
    manager.run()
