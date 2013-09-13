#! /usr/bin/env python

import sys

try:
	f=open('myfile.txt')
	s=f.readline()
	i=int(s.trip())
except IOError as e:
	print "I/O error ({0}) :{1}".format(e.errno, e.strerror)
except ValueError as e:
	print "Could not convert data to an interger"
except:
	print "Unexpected error : ", sys.exc_info()[0]
	raise