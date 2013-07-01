def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print "--This parrot wouldn't", action
	print "if you put", voltage, "volts through it."
	print "--Lovely plumage, the", type
	print "--It's", state, "!"

#parrot(1000)
#parrot(voltage=1000)
#parrot(voltage=1000000, action="VOOOOOM")
#parrot(action="VOOOOM", voltage=1000000)
parrot('a million', 'bereft of life', 'jump')


def cheeseshop(kind, *arguments, **keywords):
	print "--Do you have any", kind, "?"
	print "--I'm sorry, we're all out of", kind
	for arg in arguments:
		print arg
	print "---"*40
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw, ":", keywords[kw]

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

args=[3, 6]
range(*args)

d={"voltage":"four million", "state":"bleedin' demised", "action": "VOOM"}
parrot(**d)

