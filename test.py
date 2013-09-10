#!/usr/bin/env python

a, b = 0, 1
while b<10:
	print b
	a, b = b, a+b


i = 256*256
print 'The value of i is', i

a, b = 0,1
while b<1000:
	print b
	a, b=b, a+b


words = ['cat', 'window', 'diffenestrate']

for w in words:
	print w, len(w)

###make a copy
for w in words[:]:
	if len(w)>6:
		words.insert(0,w)

for w in words:
	print w, len(w)


