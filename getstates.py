import pandas as pd
import time
import urllib2


fifty_states = pd.read_html('http://www.50states.com/abbreviations.htm')
#return fifty_states[0][0][1:]

#print fifty_states[0][1][1:]
fifty_states.replace("Abbreviation:","")
print fifty_states[0][1][1:]
	
