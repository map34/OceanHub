import logging

from flask_script import Command, Shell

from oceanhub.scripts.producer import test_video

logger = logging.getLogger(__name__)


def test_global():
    logger.info('Hi, my name is Si!')


def make_shell_context():  # get all the tasks loaded up into the application
    return {
        'test_global': test_global,
        'test_producer_video': test_video
    }


class RunOceanHubShell(Command):
    def run(self):
        Shell(make_context=make_shell_context).run(False, False, False, False)
