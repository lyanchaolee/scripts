#! /usr/bin/env python

tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127

print tel

print tel['jack']

del tel['sape']

print tel

print tel.keys()

zmap = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

for i, v in enumerate(['tic', 'tac', 'toe']):
	print i, v

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
	print 'What is you{0}? It is {1}.'.format(q, a)

for i in reversed(xrange(1, 10, 2)):
	print i

basket = ['apple', 'orange', 'apple']

for f in sorted(set(basket)):
	print f

knights = {'gallahad': 'the pure', 'robin':'the brave'}
for k, v in knights.iteritems():
	print k, v










