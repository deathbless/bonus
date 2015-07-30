__author__ = 'hzsunyuda'

from distutils.core import setup
import py2exe

options = {"py2exe":{"bundle_files": 1}}
setup(console=["bonus.py"])