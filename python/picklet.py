#! /usr/bin/env python

a={'xxx':1, 'yyy':2, 'zzz':3}


import pickle

with open('picklexx','r+') as f:
	pickle.dump(a, f)

