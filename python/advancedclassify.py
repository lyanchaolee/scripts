#! /usr/bin/env python

class matchrow:
	def __init__(self, row, allnum=False):
		if allnum:
			self.data=[float(row[i]) for i in range(len(row)-1)]
		else:
			self.data=row[0:len(row)-1]
		self.match=int(row[len(row)-1])
def loadmatch(f, allnum=False):
	rows=[]
	for line in file(f):
		rows.append(matchrow(line.split(','),allnum))
	return rows
def linertrain(rows):
	averages={}
	counts={}
	for row in rows:
		cl=row.match
		averages.setdefault(cl,[0.0]*(len(row.data)))
		counts.setdefault(cl,0)
		for i in range(len(row.data)):
			averages[cl][i]+=float(row.data[i])
		
		counts[cl]+=1
	for cl, avg in averages.items():
		for i in range(len(avg)):
			avg[i]/=counts[cl]
	return averages
def dotproduct(v1, v2):
	return sum([v1[i]*v2[i] for i in range(len(v1))])
def dpclassify(point, avgs):
	b=(dotproduct(avgs[1],avgs[1])-dotproduct(avgs[0],avgs[0]))/2
	y=dotproduct(point,avgs[0])-dotproduct(point,avgs[1])+b
	if y>0:
		return 0
	else:
		return 1
def yesno(v):
	if v=='yes':
		return 1
	elif v=='no':
		return -1
	else:
		return 0

def matchcount(interest1, interest2):
	l1=interest1.split(':')
	l2=interest2.split(':')
	x=0
	for v in l1:
		if v in l2:
			x+=1
	return x

yahookey="d4wBd0jV34G3aiJID0kx2inyjgZSQ.sTwf8VzDnoraGfvXhcaI9ibT4JvoxIC.Bq13kPFBoqUkJlP5q52el6Ll5vNcNWuks-"

from xml.dom.minidom import parseString
from urllib import urlopen, quote_plus

loc_cache={}
def getlocation(address):
	if address in loc_cache:
		return loc_cache[address]
	data=urlopen('http://api.local.yahoo.com/MapsService/V1/'+\
                 'geocode?appid=%s&location=%s' % (yahookey,quote_plus(address))).read()
	doc=parseString(data)
	lat=doc.getElementsByTagName('Latitude')[0].firstChild.nodeValue
	longg=doc.getElementsByTagName('Longitude')[0].firstChild.nodeValue
	loc_cache[address]=(float(lat),float(longg))
	return loc_cache[address]
def milesdistance(a1, a2):
	lat1,long1=getlocation(a1)
	lat2,long2=getlocation(a2)
	latdif=69.1*(lat2-lat1)
	longdif=53.0*(long2-long1)
	return (latdif**2+longdif**2)**.5
def milesdistance2(a1, a2):
	return 0
def loadnumerical():
	oldrows=loadmatch('matchmaker.csv')
	newrows=[]
	for row in oldrows:
		d=row.data
		data=[float(d[0]),yesno(d[1]),yesno(d[2]),float(d[5]),yesno(d[6]),yesno(d[7]),matchcount(d[3],d[8]),milesdistance2(d[4],d[9]),row.match]
		newrows.append(matchrow(data))
	return newrows






