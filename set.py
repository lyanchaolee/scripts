#! /usr/bin/env python

basket = ['apple', 'orange','pear', 'apple', 'banana']

fruit = set(basket)

print fruit

print 'orange' in fruit

a = set('abracadabra')
b = set('alacazam')

print a
print b

print a-b

print a|b

print a&b

print a^b

c = {x for x in 'abracadabra' if x not in 'abc'}
print c
