import os
import unittest
import coverage

from flask_script import Manager
from src.app import app

COV = coverage.coverage(
    branch=True,
    include=['src/controllers/*', 'src/models/*']
)

COV.start()

manager = Manager(app)


@manager.command
def test():
    import xmlrunner
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('/tests')
    xmlrunner.XMLTestRunner(output=os.environ.get(
        'CIRCLE_TEST_REPORTS', 'test-reports')).run(tests)


if __name__ == '__main__':
    manager.run()
