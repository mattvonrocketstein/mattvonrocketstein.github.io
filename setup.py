#!/usr/bin/env python
""" setup.py for ghio
"""
import os, sys
from setuptools import setup

# make sure that finding packages works, even
# when setup.py is invoked from outside this dir
this_dir = os.path.dirname(os.path.abspath(__file__))
if not os.getcwd()==this_dir:
    os.chdir(this_dir)

# make sure we can import the version number so that it doesn't have
# to be changed in two places. ghio/__init__.py is also free
# to import various requirements that haven't been installed yet
sys.path.append(os.path.join(this_dir, 'ghio'))
from version import __version__
sys.path.pop()

base_url = 'https://github.com/mattvonrocketstein/ghio/'
setup(
    name         = 'ghio',
    version      = __version__,
    description  = '',
    author       = 'mattvonrocketstein',
    author_email = '$author@gmail',
    url          = base_url,
    download_url = base_url+'/tarball/0.1',
    packages     = ['ghio'],
    keywords     = ['ghio'],
    entry_points = {
        'console_scripts': \
        ['ghio = ghio.bin.ghio:main', ] }
    )
