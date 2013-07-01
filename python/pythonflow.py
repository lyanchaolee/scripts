x = 4

if x<0:
	x=0
	print "Negative changed to zero"
elif x==0:
	print 'Zero'
elif x==1:
	print 'Single'
else:
	print 'More'

words=['cat', 'window', 'defenestrate']

for w in words[:]:
	if len(w)>6:
		words.insert(0,w)

for w in words:
	print w, len(w)

print range(10)

a=['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print i, a[i]

for n in range(2, 10):
	for x in range(2, n):
		if n%x==0:
			print n, 'equals', x, '*', n/x
			break
	else:
		print n, 'is a prime number'
 



