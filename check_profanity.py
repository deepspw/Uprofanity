# Check Profanity | 11 May 2015 | v01

import urllib

def read_text(inputtext):
	with open(inputtext) as quotes:
		textout = quotes.read()
	quotes.close()
	return textout.split('\n')


def check_profanity(inputtext):

	textin = read_text(inputtext)
	linecount = 0
	offenders = []
	
	print "Checking text for profanity..."

	for e in textin:
		wdyl = urllib.urlopen("http://www.wdyl.com/profanity?q=%r" % e)
		if 'true' in wdyl.read():
			offenders.append("Offence at line " + str(linecount) + ' | ' + e)
		linecount += 1
	if len(offenders) < 1:
		print "None found!"
	else:
		for e in offenders:
			print e
	

check_profanity(raw_input('Enter text file > '))

# Sources used
# http://www.wdyl.com/profanity?q