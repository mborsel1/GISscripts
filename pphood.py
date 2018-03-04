import time
import urllib2
import pandas as pd
import csv
from itertools import chain
import sys
from bs4 import BeautifulSoup, NavigableString, Comment


ladd = []
lcity = []
lstate = []
lzip = []

def state_list():

	#fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	#return fifty_states[0][0][1:]
	fifty_states = pd.read_html('http://www.50states.com/abbreviations.htm')
	return fifty_states[0][1][1:]
	


def pploc():
	states = state_list()
	
	#print states
	for state in states:
	

		try:
			site = 'https://www.plannedparenthood.org/health-center/'+state
			hdr = {'User-Agent': 'Mozilla/5.0'}
			req = urllib2.Request(site, headers=hdr)
			page = urllib2.urlopen(req)
			soup = BeautifulSoup(page, 'lxml')
			
			
			for hit in soup.findAll(attrs={'class':'center_address'}):
				peas = ''.join(unicode(child) for child in hit.children 
					if isinstance(child, NavigableString) and not isinstance(child, Comment))
				ladd.append(peas.encode('ascii','replace'))
					

			for hit in soup.findAll(attrs={'class':'center_city'}):
				peas = ''.join(unicode(child) for child in hit.children 
					if isinstance(child, NavigableString) and not isinstance(child, Comment))
				lcity.append(peas.encode('ascii','replace'))
					

			for hit in soup.findAll(attrs={'class':'center_zip'}):
				peas = ''.join(unicode(child) for child in hit.children 
					if isinstance(child, NavigableString) and not isinstance(child, Comment))
				lzip.append(peas.encode('ascii','replace'))
				lstate.append(state.encode('ascii','recplace'))


			
			#lstate.append(state)
		

		except Exception, e:
			print "failed in the main loop", str(e)
pploc()

ladd = ladd[:-9] #removes the 9 Maryland addresses that are included on the DC page
lcity = lcity[:-9]
lstate = lstate[:-9]
lzip = lzip[:-9]

with open("pphood.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerow(['Address', 'City', 'State', 'ZipCode'])
	rows = zip(ladd, lcity, lstate, lzip)
	for row in rows:
		writer.writerow(row)

			
