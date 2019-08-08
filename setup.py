#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
      name="pysyft-proto",
      version='0.0.1',
      description='PySyft protocol constants.',
      packages=find_packages(exclude=['js']),
      license='LICENSE',
      include_package_data=True
)
