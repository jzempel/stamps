#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    setup
    ~~~~~

    Setup the stamps distribution.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup
import stamps

setup(
    name="stamps.py",
    version=stamps.__version__,
    url="http://github.com/jzempel/stamps",
    license=stamps.__license__,
    author=stamps.__author__,
    author_email="jzempel@gmail.com",
    description="Stamps.com API for Python.",
    long_description=__doc__,
    packages=["stamps"],
    package_data={"stamps": ["wsdls/*.wsdl"]},
    include_package_data=True,
    install_requires=["suds==0.4.1"],
    dependency_links=["https://github.com/nemith/suds/tarball/master#egg=suds-0.4.1"],  # NOQA
    test_suite="stamps.tests"
)
