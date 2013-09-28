#! /usr/bin/env python

import urllib2

c = urllib2.urlopen('http://www.alibaba.com')

contents = c.read()

print contents[0:50000000]