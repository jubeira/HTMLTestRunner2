#!/usr/bin/env python

from setuptools import setup

setup(
    name='html-testRunner2',
    version='0.1.0',
    description="A Test Runner in python, for Human Readable HTML Reports",
    packages=[
        'HTMLTestRunner',
    ],
    package_dir={'HTMLTestRunner': 'src'},
    include_package_data=True,

    package_data={'HTMLTestRunner': ['resources/css/*.*', 'resources/fonts/*.*', 'resources/js/*.*', 'resources/templates/*.*']}
)
