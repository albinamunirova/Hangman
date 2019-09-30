#!/usr/bin/env python3.5

"""Setup script."""

from setuptools import setup

setup(
    name="hangman",
    version="0.0.0",
    author="Albina Munirova",
    author_email="albamoon@mail.ru",
    url="https://github.com/albinamunirova/Hangman",
    license="MIT",
    packages=[
        "game",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
        "mock",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5.2",
    ],
    entry_points={
        'console_scripts': ['hangman=game.start:main'],
    }
)