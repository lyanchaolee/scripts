class MyClass:
	"""A Simple example class"""
	i = 12345
	def f(self):
		return 'hello world'

x = MyClass()

print x.f()
print x.__doc__


xf = x.f

print xf()

class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

x = Complex(3.0, -4.5)

print x.r, x.i
