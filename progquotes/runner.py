from django_coverage.coverage_runner import CoverageRunner
from django_nose import NoseTestSuiteRunner


class LocalRunner(CoverageRunner, NoseTestSuiteRunner):
    """This test runner allows us to use both django-nose (to discover tests),
    and django-coverage (to check our code coverage).
    """
    pass
