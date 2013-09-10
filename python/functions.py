#! /usr/bin/env python

def fib(n):
	a, b = 0, 1
	while a<n:
		print a,
		a, b=b, a+b

fib(2000) 


def fib2(n):
	result = []
	a, b = 0, 1
	while a<n:
		result.append(a)
		a, b= b, a+b
	return result

print 'next line: '

for x in fib2(1000):
	print x

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print "--This parrot wouldn't", action,
	print "if you put", voltage, "volts through it."
	print "--Lovely plumage, the", type
	print "--It's", state, "!"


parrot (1000)

parrot (voltage=1000)
parrot(voltage=1000000, action='VOOOOOM')


def cheeseshop(kind, *arguments, **keywords):
	print "--Do you have any", kind, "?"
	print "--I'm sorry, we're all out of", kind
	for arg in arguments:
		print arg
	print "-"*40
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw, ":", keywords[kw]

cheeseshop(
			"Limburger", "It's very runny, sir.",
			"It's really very, VERY runny, sir.",
			shopkeeper="Michael Palin",
			client="John Cleese",
			sketch="Cheese Shop Sketch"
			)

d = {"voltage" : "xxx", "state":"yyy", "action":"VOOOOOOOOOM"}
parrot(**d)













