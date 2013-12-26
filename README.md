Claymore
========

Generates a random string from ASCII/ASCII-EXTENDED/UTF-8 Table and store it in a file

This was tested on Python3.3 x64 and is the recommended version to use.


!! WARNING !!
Currently length isn't handled which will cause an MemError if you do not have enough ram for the given length to be generated.



Usage:
------

program [-a | -e | -v | -h] length filename


Options:
-------
	-a 		Generate the string using only the ASCII table
	-e 		Generate the string using the Extended ASCII table
	-v 		Shows progress
	-h 		Shows usage
