#! /usr/bin/env python

def fib(n):
	result=[]
	a, b=0, 1
	while a<n:
		result.append(a)
		a, b=b, a+b
	return result

def fib2(n):
	result = []
	a, b=0, 1
	while b<n:
		result.append(b)
		a, b=b, a+b
	return result