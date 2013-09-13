#! /usr/bin/env python

for x in range(1, 11):
	print repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)

print '{0} and {1}'.format('spam', 'eggs')
print '{1} and {0}'.format('spam', 'eggs')

print 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')

print 'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg')




import math
print 'The value of PI is approximately {}.'.format(math.pi)

print 'The value of PI is approximately {!r}'.format(math.pi)

print 'The value of PI is approximately {0: .48f}.'.format(math.pi)

table = {'Sjoerd': 4127, 'Jack':4098, 'Dcab':7678}

for name, phone in table.items():
	print '{0:10} ==> {1:10d}'.format(name, phone)

f = open('filetest', 'r+')

f.write('0123456789abcdef')

f.seek(10)
print f.read(1)

f.close()

with open('filetest', 'r') as f:
	read_data = f.read()
	print read_data
	print f.closed

print f.closed















