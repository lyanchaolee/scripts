def fib(n):
	a, b = 0, 1
	while b<n:
		print b
		a, b=b, a+b

fib(2000)

def fib2(n):
	result=[]
	a, b = 0, 1
	while a<n:
		result.append(a)
		a, b=b, a+b
	return result

print fib2(1000)

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
	while True:
		ok=raw_input(prompt)
		if ok in ('y','ye','yes'):
			return True
		if ok in ('n','no','nope'):
			return False
		retries=retries-1
		if retries<0:
			raise IOError('refusenik user')
		print complaint

i = 5
def f(arg=i):
	print arg

i = 6
f()

def f(a, L=[]):
	L.append(a)
	return L

print f(1)
print f(2)
print f(3)

def f2(a,  L=None):
	if L is None:
		L=[]
	L.append(a)
	return L

print f2(1)
print f2(2)
print f2(3)








