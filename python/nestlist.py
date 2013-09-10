#! /usr/bin/env python

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
]

print [[row[i] for row in matrix] for i in range(4)]

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]

print a
del a[2:4]
print a
del a
