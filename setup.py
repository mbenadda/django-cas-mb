#!/usr/bin/env python
import codecs

from setuptools import setup

setup(package_data={"django_cas_ng": ["locale/*/LC_MESSAGES/*", "py.typed"]})
