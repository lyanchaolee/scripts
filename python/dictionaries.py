tel = {'jack' : 4098, 'sape' : 4139}

tel['guido'] = 4127

print tel

print tel['sape']

del tel['sape']

print tel

print tel.keys()

print 'guido' in tel

dd = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print dd

xx = {x : x**2 for x in (2, 4, 6)}

print xx


yy = dict(sape=4139, guido=4127, jack=4098)

print yy