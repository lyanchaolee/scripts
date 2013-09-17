#! /usr/bin/env python

critics = {
	'Lisa Rose':{'Lady in the Water':2.5, 'Snakes on a Plane':3.5, 'Just My Luck':3.0, 
			'Just My Luck':3.0, 'Superman Returns':3.5, 'You, Me and Dupree':2.5, 
			'The Night Listener':3.0},
	'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
      'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
      'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
      'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
      'The Night Listener': 4.5, 'Superman Returns': 4.0,
      'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
      'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
      'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
     'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

def sim_distance(person1, person2, pref=critics):
	si = {}
	for item in pref[person1]:
		if item in pref[person2]:
			si[item]=1
	if len(si)==0:
		return 0
	sum_of_squres=sum([pow(pref[person1][item]-pref[person2][item],2)
					   for item in pref[person1] if item in pref[person2]])
	return 1/(1+sum_of_squres)

sortset=[]

for k1 in critics.keys():
	for k2 in critics.keys():
		if k1!=k2:
			keyappend = k1+k2 if k1>k2 else k2+k1
			if keyappend in sortset:
				continue
			sortset.append(keyappend)
			print 'score between', k1, k2, 'is', sim_distance(k1, k2)


