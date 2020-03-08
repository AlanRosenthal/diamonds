#!/usr/bin/evn python

requires = ["Click==7.0"]

from setuptools import setup, find_packages

setup(
    name="diamonds",
    version="0.1",
    packages=find_packages(),
    entry_points={"console_scripts": ["diamonds = diamonds.diamonds:cli"]},
    install_requires=requires,
)
