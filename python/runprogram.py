#!/usr/bin/python

import commands
import os,sys

def test(program, params):
	paramStr
	for param in params:
		paramStr+=param
	 a, b=commands.getstatusoutput(program+paramStr)
	 print a, b

print sys.argv

test(sys.argv, [3, 'xxxx', 'yyyy', 'zzzzz'])