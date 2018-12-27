import os
import unittest
import coverage

from flask_script import Manager
from app import app

COV = coverage.coverage(
    branch=True,
    include=['controllers/*', 'models/*']
)

COV.start()

manager = Manager(app)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
