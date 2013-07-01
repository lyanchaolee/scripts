class MyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

try:
	raise MyError(2*2)
except MyError as e:
	print 'My exception occurred, value:', e.value


def divide(x, y):
	result = 0
	try:
		result = x / y
	except ZeroDivisionError:
		print "result is", result
	except Exception:
		pass
	finally:
		print "executing finally clause"

divide(2, 1)
divide(2, 0)
print "*******"*20
divide("2", "0")

with open("dictionaries.py") as f:
	for line in f:
		print line