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

Jinja
-----
1. Download and run [setuptools](http://pypi.python.org/packages/2.5/s/setuptools/setuptools-0.6c9.win32-py2.5.exe#md5=602d06054ec1165e995ae54ac30884d7)
2. Open a command prompt (Start -> Run -> cmd) and type `C:\Python25\Scripts\easy_install.exe jinja2`

Mutagen
-------
1. Open a command prompt (Start -> Run -> cmd) and type `C:\Python25\Scripts\easy_install.exe mutagen`

Get the Script
--------------
1. Open a command prompt (Start -> Run -> cmd) and type `C:\Python25\Scripts\easy_install.exe bxt_description_generator`

Arch Linux
==========
Python, Jinja, Mutagen, easy_install
---------------------------
1. Go to Terminal, whatever terminal program you may have.
2. Type `su -` and then type in your root password.
3. Type `pacman -Sy python python-jinja mutagen setuptools` while in su mode and y for the confirmation prompt to install.

Get the script
--------------
1. While still root, type `easy_install boxtorrents_description_generator`

Ubuntu/Debian
=============
Python, Jinja, Mutagen, easy_install
---------------------------
1. Go to Terminal, whatever terminal program you may have.
2. Type `sudo apt-get install python python-jinja2 python-mutagen python-setuptools` and y for the confirmation prompt to install.

Get the script
--------------
1. While still root, type `easy_install boxtorrents_description_generator`
