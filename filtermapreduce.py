#! /usr/bin/env python

def f(x):
	return x % 2 !=0 and x % 3 !=0

xxx = filter(f, range(2, 25))

print xxx

def cube(x): return x*x*x
yyy = map(cube, range(1, 11))
print yyy

seq = range(8)
def add(x, y): return x+y
zzz = map(add, seq, seq)
print zzz


xxxx = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print xxxx


vec = [-4, -2, 0, 2, 4]

yyyy=[item for item in vec if item > 0]
print yyyy

print [abs(item) for item in vec]

freshfruit = [' banana', ' loganberry ', 'passion fruit ']

print [item.strip() for item in freshfruit]

print [(x, x**2) for x in range(6)]






