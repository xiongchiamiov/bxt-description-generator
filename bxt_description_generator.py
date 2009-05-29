#!/usr/bin/env ipython

"""
This software is licensed under version 2.0 of the WTFPL (see COPYING for details)
"""

import sys
import os
from models import *

# Check to see if we have all the information we need
try:
	directory = sys.argv[1]
	template = sys.argv[2]
except IndexError:
	print "Usage: " + sys.argv[0] + " <directory> <template>"
	exit()

root = Folder(directory)
root.scan()
