from oceanhub import app
from oceanhub.scripts.shell import make_shell_context
from flask_script import Manager, Command, Shell

manager = Manager(app)

class StartShell(Command):
    def run(self):
        Shell(make_context=make_shell_context).run(False, False, False, False)

manager.add_command("shell", StartShell())

if __name__ == "__main__":
    manager.run()
