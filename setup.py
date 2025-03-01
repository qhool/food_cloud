#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name = "Food Cloud",
    version = "0.1.0",
    description = "builds a word cloud of available food trucks in San Francisco, California",
    author = "Josh Burroughs",
    author_email = "josh@qhool.com",

    long_description=open("README.md", "r", encoding="utf-8").read(),
    python_requires='>=3.7, <4',
    install_requires = [
        "pandas",
        "numpy<2",
        "wordcloud",
        "geocoder"
    ]
)
