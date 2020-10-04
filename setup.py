#!/usr/bin/env python

from setuptools import setup, find_packages


with open("README.md", "rt", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name="pyh",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["pyh = pyh:main"]
    },
    version="1.0",
    description="man-like tool to get online help on Python modules, classes and functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Benoit Hamelin",
    author_email="benoit@benoithamelin.com",
    url="https://github.com/hamelin/pyh/",
    install_requires=["nestedtext"]
)
