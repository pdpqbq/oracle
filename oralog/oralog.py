import os
import re

# BEGIN SETUP

includeWords = '''fatal
aborting
warning
error
streams_pool'''

excludeWords = '''vktm detected
TNS
NI
LICENSE
ALLOCATED_PAGES'''

sourceLog = 'alert.log' # input file
#workDir = '' # set working dir manually or get from .py file path
workDir = os.path.dirname(os.path.abspath(__file__))
saveFile = ''.join([workDir, '/', 'last_event.txt'])
saveState = True # save last timestamp

# END SETUP

includeRegexp = re.compile('|'.join(includeWords.split('\n')), re.IGNORECASE)
excludeRegexp = re.compile('|'.join(excludeWords.split('\n')), re.IGNORECASE)

#print(sourceLog)
#print(workDir)
#print(saveFile)
#print(includeRegexp)
#print(excludeRegexp)

msg = ['XXXX-XX-XX LOG CUT', '', False] # time message flag

try:
	saveTime = open(saveFile, 'r')
	lastEventSaved = saveTime.read()
	saveTime.close()
except FileNotFoundError:
	lastEventSaved = ''

with open(sourceLog) as logFile:
	for line in logFile:
		rez = re.search(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}', line)
		if rez:
			if msg[1] and msg[2]:
				print('\n'.join(msg[0:2]) + '-'*50)
			msg = [rez.group(), '', False]
		elif msg[0] > lastEventSaved:
			msg[1] += line
		if re.search(includeRegexp, line.strip('\n')) and not re.search(excludeRegexp, line.strip('\n')):
			msg[2] = True

if saveState and msg[0][0] != 'X': # save state
	saveTime = open(saveFile, 'w')
	saveTime.write(msg[0])
	saveTime.close()

