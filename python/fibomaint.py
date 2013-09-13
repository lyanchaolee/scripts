#! /usr/bin/env python

if __name__=="__main__":
	import sys
	from fibo import fib
	print fib(int(sys.argv[1]))