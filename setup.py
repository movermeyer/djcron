# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

MODULE = 'djcron'

def read_file(filename):
    with open(filename) as fd:
        return fd.read()

def app_info():
    version_file = os.path.join(MODULE, 'versions.py')
    local = dict()
    exec(read_file(version_file), local)
    return local.get('APP')


APP = app_info()


setup(
    name=MODULE.replace('_', '-'),
    version=APP.version,
    description=APP.description,
    long_description=read_file('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
    ],
    keywords='distributed cron',
    author='Miguel Ángel García',
    author_email='miguelangel.garcia@gmail.com',
    url='https://github.com/djcron-project/djcron',
    license='Affero',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'djcron-server',
        'djcron-agent',
    ],
)
