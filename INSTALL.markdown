Requirements
============
[Python](http://www.python.org/) >= 2.4 (3.0 compatability not guaranteed)  
[Jinja 2](http://jinja.pocoo.org/2/)  
[Mutagen](http://code.google.com/p/quodlibet/wiki/Mutagen)  >= 1.15  

Windows
=======
Python
------
1. Download and run [the installation file](http://www.python.org/ftp/python/2.5.4/python-2.5.4.msi)

easy_install
------------
1. Download and run [setuptools](http://pypi.python.org/packages/2.5/s/setuptools/setuptools-0.6c9.win32-py2.5.exe#md5=602d06054ec1165e995ae54ac30884d7)
2. Alter your PATH to include C:\Python25\Scripts.  You have two options as to how to go about doing this:
### Manually ###
	* [XP](http://www.computerhope.com/issues/ch000549.htm)
	* [Vista](http://banagale.com/2007/03/03/changing-your-system-path-in-windows-vista/)
### Automatically, using SetEnv ###
	1. Download [fixpath.zip](http://cloud.github.com/downloads/xiongchiamiov/bxt-description-generator/fixpath.zip)
	2. Unzip it.
	3. Run `fixpath.bat`
	
Either way, it should end up looking something like
`%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;C:\Python25\Scripts`;
you can check by running `echo %PATH%` in a command prompt.

EasyGui (optional, required for GUI)
------------------------------------
1. Download [easygui.zip](http://easygui.sourceforge.net/current_version/easygui_v0.93.zip).
2. Extract the files.
3. Put `easygui.py` in `C:\Python25\Lib\site-packages`.

Get the Script
--------------
1. Open a command prompt (Start -> Run -> cmd) and type `easy_install.exe -U bxt_description_generator`

Arch Linux
==========
Python, Jinja, Mutagen, easy_install
---------------------------
1. Open a terminal.
2. Run `pacman -Sy python python-jinja mutagen setuptools` as root.

EasyGui (optional, required for GUI)
------------------------------------
1. Install `python-easygui` from the AUR.

Get the script
--------------
1. Also as root, run `easy_install -U bxt_description_generator`

Ubuntu/Debian
=============
Python, Jinja, Mutagen, easy_install
---------------------------
1. Open a terminal.
2. Run `sudo apt-get install python python-jinja2 python-mutagen python-setuptools`.

EasyGui (optional, required for GUI)
------------------------------------
1. Download [easygui.tar.gz](http://easygui.sourceforge.net/current_version/easygui_v0.93.tar.gz).
2. Extract the files.
3. Put `easygui.py` in `/usr/local/lib/python2.6/dist-packages`.

Get the script
--------------
1. Run `sudo easy_install -U bxt_description_generator`
