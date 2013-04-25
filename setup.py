import sys
from setuptools import setup, find_packages
from setuptools.command.test import test

def run_tests(*args):
    from sample_app.tests import run_tests
    errors = run_tests()
    if errors:
        sys.exit(1)
    else:
        sys.exit(0)

test.run_tests = run_tests

setup(
    name = "django-sample-app",
    version = "0.1",
    packages = find_packages(),
    license = "BSD",
    description = "A Django sample app, with setup, unittests, docs and demo site.",
    long_description = "A simple pluggable Django app that does nothing special but to serve as a sample layout for another Django apps. It offers a simple arithmetic calculator. Read the docs to know more.",
    author = "Daniel Rus Morales",
    author_email = "mbox@danir.us",
    maintainer = "Daniel Rus Morales",
    maintainer_email = "mbox@danir.us",
    url = "http://pypi.python.org/pypi/django-sample-app/",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    test_suite = "dummy",
    include_package_data = True,
)
