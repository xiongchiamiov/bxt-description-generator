#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

ENTRY_POINTS = \
"""[console_scripts]
tgp = bxt_description_generator:main
"""

def main():
	setup(
	    name='bxt_description_generator',
	    version='0.1',
	    description='BoxTorrents Description Generator',
	    author='xiong_chiamiov',
	    url='http://github.com/xiongchiamiov/bxt-description-generator/tree/master',
	    package_data = {'templates':['*.*']},
	    packages=['.', 'templates'],
	    zip_safe=False,
	    install_requires=['setuptools', 'jinja2', 'mutagen'],
	    long_description="""
	    Generates a description suitable for including with your Boxtorrents offers. Well, hopefully.""",
	    license='WTFPL',
	    entry_points=ENTRY_POINTS,
	    classifiers=[
	    "Assistant :: YumiNanako",
	    "License :: DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE (WTFPL)",
	    "Programming Language :: Python",
	    "Topic :: Internet",
	    "Intended Audience :: BoxTorrent OST Uploaders",
	    "Development Status :: Beta"])
	return 0

if __name__ == '__main__':
	sys.exit(main())
