#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pysyft-proto",
    version='0.0.1',
    description='PySyft protocol constants.',
    packages=['pysyft_proto'],
    package_data={'': ['proto.json']},
    data_files=[('.', ['proto.json'])],
    license='LICENSE',
    include_package_data=True
)
