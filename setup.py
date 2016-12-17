import sys

from setuptools import setup, find_packages

setup(
    name = "Django-Next-Please",
    version = '16.12.1',
    description = "Simple Pagination Decorator for Django.",
    url = "https://github.com/pizzapanther/Django-Next-Please",
    author = "Paul Bailey",
    author_email = "paul.m.bailey@gmail.com",
    license = "BSD",
    packages = ['NextPlease'],
    include_package_data = True,
)
