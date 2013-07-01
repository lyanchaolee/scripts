t = 12345, 54321, 'hello!'
print t[0]

u = t, (1, 2, 3, 4, 5)

print u

v=([1, 2, 3], [3, 2, 1])

print v

empty = ()

singleton = 'hello',

print len(singleton)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit=set(basket)

print fruit

print 'orange' in fruit
print 'xxxx' in fruit

a=set('abtracadabra')
b=set('alacazam')

print a

print a - b

print a|b

print a&b

print a ^ b

a = {x for x in 'abracadabra' if x not in 'abc'}

print a





