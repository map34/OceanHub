import sys
import unittest

from flask_script import Command, Option


class RunOceanHubTests(Command):
    """
    By default, runs all unit tests in the project.
    """

    option_list = (
        Option(
            '--name',
            '-n',
            dest='location_of_tests',
            required=False
        ),
        Option(
            '--failfast',
            action='store_true',
            dest='failfast',
            default=False
        ),
        Option(
            '--verbosity',
            '-v',
            dest='verbosity',
            default=3
        ),
    )

    def run(
        self, location_of_tests=None, travis=False, failfast=False, verbosity=0
    ):
        from oceanhub import app
        from oceanhub.core.blueprints import initialize_blueprints

        initialize_blueprints(app)

        if location_of_tests is None:
            tests = unittest.TestLoader().discover('.')
        else:
            tests = unittest.TestLoader().loadTestsFromName(location_of_tests)
            if tests.countTestCases() == 0:
                tests = unittest.TestLoader().discover(location_of_tests)

        result = unittest.TextTestRunner(
            failfast=failfast,
            verbosity=verbosity
        ).run(tests)

        sys.exit(len(result.errors) + len(result.failures))
