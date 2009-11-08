#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This software is licensed under version 2.0 of the WTFPL (see COPYING for details)
"""

import sys
import os
import re
from models import *
from jinja2 import Environment, PackageLoader

reload(sys)
sys.setdefaultencoding("utf-8")

def absolute_path(path):
	''' Get the absolute path of a file, from this script '''
	ROOT = os.path.dirname(os.path.realpath(__file__))
	os.path.join(ROOT,path)
	return os.path.join(ROOT,path)

def cleanify(name):
	''' Strip out some things that don't play well in element ids '''
	return re.sub(r"[\. ']", r'_', name)

# are we running this standalone, rather than as a module?
def main():
	# Check to see if we have all the information we need
	try:
		#directory = unicode(sys.argv[1])
		directory = sys.argv[1]
		template = sys.argv[2]
	except IndexError:
		try:
			import easygui
			
			# get directory from user
			directory = None
			while not directory:
				directory = easygui.diropenbox('Where are the files?')
			
			# get template from user
			template = None
			while not template:
				template = easygui.choicebox('What template do you want?', choices=os.listdir(absolute_path('templates')))
		except ImportError:
			sys.stderr.write("Usage: " + sys.argv[0] + " <directory> <template>\n")
			exit()
	
	root = Folder(directory)
	root.scan()
	
	env = Environment(loader=PackageLoader('bxt_description_generator', 'templates'))
	env.filters['cleanify'] = cleanify
	template = env.get_template(template)
	output = template.render(root=root).encode("utf-8")
	
	try:
		easygui.codebox(text=output)
	except NameError:
		print output

if __name__ == '__main__':
	sys.exit(main())
