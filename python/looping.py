for i, v in enumerate(['tic', 'tac', 'toe']):
	print i, v

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
	print "What's your {0} ? It is {1}. ".format(q, a)

for i in reversed(xrange(1, 10, 2)):
	print i

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
	print f

words = ['cat', 'window', 'defenestrate']

for w in words[:]:
	if len(w)>6:
		words.insert(0, w)

print words

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3

print non_null

print (1, 2, 3) < (1, 2, 4)
print [1, 2, 3] < [1, 2, 3]
print (1, 2, 3, 4) < (1, 2, 4)
print (1, 2, 3) == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab'), 4) < (1, 2, ('abc', 'a'))