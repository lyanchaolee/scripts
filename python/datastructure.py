#!/usr/bin/python

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')

a.insert(2,-1)
a.append(333)

print a
print a.index(333)
a.remove(333)
a.reverse()
print a

a.sort()
print a



#######use lists as stacks############

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print stack
print stack.pop(), stack


#######use lists as queues############

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print queue.popleft()
print queue.popleft()

print queue

#######functional programming tools#######

def f(x):
	return x % 2 != 0 and x % 3 != 0

print filter(f, range(2, 25))

def cube(x):
	return x*x*x
print map(cube, range(1, 11))

def add(x, y):
	return x+y
print reduce(add, range(1, 11))

def sum(seq):
	def add(x,y):
		return x+y
	return reduce(add, seq, 0)

print sum(range(1, 11))

squares = []
for x in range(10):
	squares.append(x**2)

print squares

squares=[x**2 for x in range(10)]

xxx = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print xxx

vec = [-4, -2, 0, 2, 4]
print [x*2 for x in vec]

print [x for x in vec if x>=0]

print [abs(x) for x in vec]

freshfruit = [' banana ', 'loganberry ', 'passion fruit ']
print [fruit.strip() for fruit in freshfruit]

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [x for y in vec for x in y]

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
]

print [[row[i] for row in matrix] for i in range(4)]

transposed=[]
for i in range(4):
	matrix_trans_item=[]
	for item in matrix:
		matrix_trans_item.append(item[i])
	transposed.append(matrix_trans_item)

print transposed

a = [-1, 1, 66.25, 333, 1234.5]
del a[0]
print a
del a[2:4]
print a
del a[:]
print a







