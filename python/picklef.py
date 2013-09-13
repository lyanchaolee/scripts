#! /usr/bin/env python



import pickle

with open('picklexx','r+') as f:
	a=pickle.load(f)

print a
