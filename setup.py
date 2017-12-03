#!/usr/bin/env python3

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='username_generator',
    version='2.0.0',
    description='A command line application to generate random usernames.',
    long_description=long_description,
    url='https://github.com/abactel/username_generator_cli',
    author='Awes Mubarak',
    author_email='awes.mubarak@awesmubarak.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    keywords='cli random usernames',
    packages=['username_generator'],
    entry_points={
        'console_scripts': [
            'usernames=username_generator:main',
        ],
    },
)
