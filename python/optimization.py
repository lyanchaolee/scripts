#! /usr/bin/env python

import time
import random
import math

people =[('Seymour', 'BOS'),
		 ('Franny', 'DAL'),
		 ('Zooey', 'CAK'),
		 ('Walt', 'MIA'),
		 ('Buddy', 'ORD'),
		 ('Les', 'OMA')]
destination = 'LGA'

flights = {}

for line in file('./schedule.txt'):
	orgin, dest, depart, arrive, price = line.strip().split(',')
	flights.setdefault((orgin,dest),[])
	flights[(orgin,dest)].append((depart, arrive, int(price)))

def getminutes(t):
	x = time.strptime(t, '%H:%M')
	return x[3]*60+x[4]

def printschedule(r):
	for d in range(len(r)/2):
		name = people[d][0]
		origin = people[d][1]
		out = flights[(origin,destination)][r[2*d]]
		ret = flights[(destination,origin)][r[2*d+1]]
		print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, origin, out[0], out[1], out[2], ret[0], ret[1], ret[2])

def schedulecost(sol):
	print 'sol is :', sol
	totalprice = 0
	latestarrival=0
	earliestdep=24*60

	for d in range(len(sol)/2):
		origin = people[d][1]
		outbound = flights[(origin, destination)][int(sol[2*d])]
		returnf = flights[(destination, origin)][int(sol[2*d+1])]
		totalprice+=outbound[2]+returnf[2]

		if latestarrival<getminutes(outbound[1]):
			latestarrival=getminutes(outbound[1])
		if earliestdep>getminutes(returnf[0]):
			earliestdep=getminutes(returnf[0])

	totalwait = 0
	for d in range(len(sol)/2):
		outbound = flights[(origin, destination)][int(sol[2*d])]
		returnf = flights[(destination, origin)][int(sol[2*d+1])]
		totalwait += latestarrival-getminutes(outbound[1])
		totalwait += getminutes(returnf[0])-earliestdep

	if latestarrival>earliestdep:
		totalprice+=50

	return totalprice+totalwait


def randomoptimize(domain, costf):
	best = 999999999
	bestr = None

	for i in range(1000000):
		r =[random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]

	cost = costf(r)

	if cost <best:
		best = cost
		bestr = r

	return r

def hillclimb(domain, costf):
	sol = [random.randint(domain[i][0], domain[i][1]) for i in range(len(domain))]

	while 1:
		neighbors=[]
		for j in range(len(domain)):
			if sol[j]>domain[j][0]:
				neighbors.append(sol[0:j]+[sol[j]-1]+sol[j+1:])
			if sol[j]<domain[j][1]:
				neighbors.append(sol[0:j]+[sol[j]+1]+sol[j+1:])
		current = costf(sol)
		best=current
		for j in range(len(neighbors)):
			cost = costf(neighbors[j])
			if cost<best:
				sol = neighbors[j]
		if best==current:
			break
	return sol

def mostoptimize(costf):
	best = 999999999
	bestr = None
	domain = []
	for i1 in range(10):
		for i2 in range(10):
			for i3 in range(10):
				for i4 in range(10):
					for i5 in range(10):
						for i6 in range(10):
							for i7 in range(10):
								for i8 in range(10):
									for i9 in range(10):
										for i10 in range(10):
											 domain=[]
											 domain.append(i1)
											 domain.append(i2)
											 domain.append(i3)
											 domain.append(i4)
											 domain.append(i5)
											 domain.append(i6)
											 domain.append(i7)
											 domain.append(i8)
											 domain.append(i9)
											 domain.append(i10)
											 if best>costf(domain):
											 	best = costf(domain)
											 	bestr = domain

	return bestr

def annealingoptimize(domain, costf, T=1000.0, cool=0.95, step=1):
	vec = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
	
	while T>0.1:
		i = random.randint(0, len(domain)-1)
		dir = random.randint(-step, step)
		vecb = vec[:]
		vec[i]+=dir
		if vecb[i]<domain[i][0]:
			vecb[i]=domain[i][0]
		elif vecb[i]>domain[i][1]:
			vecb[i]=domain[i][1]

		ea=costf(vec)
		eb=costf(vecb)

		if(eb<ea or random.random()<pow(math.e, -(eb-ea)/T)):
			vec = vecb

		T=T*cool
	return vec

def geneticoptimize(domain, costf, popsize=50, step=1, mutprob=0.2, elite=0.2, maxtier=100):
	
	def mutate(vec):
		i = random.randint(0, len(domain)-1)
		if random.random()<0.5 and vec[i]>domain[i][0]:
			return vec[0:i]+[vec[i]-step]+vec[i+1:]
		elif vec[i]<domain[i][1]:
			return vec[0:i]+[vec[i]+step]+vec[i+1:]

	def crossover(r1, r2):
		i = random.randint(1, len(domain)-2)
		return r1[0:i]+r2[i:]

	pop=[]
	for i in range(popsize):
		vec = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
		pop.append(vec)

	topelite=int(elite*popsize)

	for i in range(maxtier):
		scores=[(costf(v),v) for v in pop]
		scores.sort()
		ranked = [v for (s, v) in scores]

		pop = ranked[0:topelite]

		while len(pop)<popsize:
			if random.random()<mutprob:
				c=random.randint(0, topelite)
				pop.append(mutate(ranked[c]))
			else:
				c1=random.randint(0,topelite)
				c2=random.randint(0,topelite)
				pop.append(crossover(ranked[c1], ranked[c2]))
		print scores[0][0]
	return scores[0][1]

























