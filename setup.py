#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

def main():
	setup (
		name = 'bxt_description_generator',
		version = '0.2',
		description = 'BoxTorrents Description Generator',
		author = 'xiong_chiamiov',
		author_email = 'xiong.chiamiov@gmail.com',
		url = 'http://github.com/xiongchiamiov/bxt-description-generator/tree/master',
		packages = ['bxt_description_generator'],
		package_data  =  {'bxt_description_generator': ['templates/*']},
		zip_safe = False,
		install_requires = ['setuptools', 'jinja2', 'mutagen'],
		long_description = """
			Generates a description suitable for including with your Boxtorrents offers. Well, hopefully.
		""",
		license = 'WTFPL',
		entry_points = """
			[console_scripts]
			tgp = bxt_description_generator.bxt_description_generator:main
		""",
		classifiers = [
			"Development Status :: 4 - Beta",
			"Environment :: Console",
			"License :: Other/Proprietary License",
			"Operating System :: OS Independent",
			"Programming Language :: Python",
			"Topic :: Internet",
		],
	)
	return 0

if __name__ == '__main__':
	sys.exit(main())
