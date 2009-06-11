#!/bin/sh

pythons='python2.5 python2.6'

for version in $pythons; do
	/usr/bin/env $version setup.py bdist_egg
	/usr/bin/env $version setup.py bdist_egg upload
done
