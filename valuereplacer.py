#!/usr/bin/python

import subprocess,os,sys,fileinput

def dataError(errorType,value):
	if (errorType == 1):
		print 'ERROR: The file does not exist'
	elif (errorType == 2):
		print "ERROR: Can't find the value '"+value+"'"
	elif (errorType == 3):
		print "ERROR: Missing parameters"		
	os.execl('valuereplacer.py', '')

def modifyValue(filename,value,sep,newValue):
	with open(filename) as searchfilename:
	    for line in searchfilename:
	        left,sep2,right = line.partition(value+sep)   
	        if sep2: 
	            oldValue = right[:1000]
	for line in fileinput.input(filename, inplace=True):
	     print line.replace(value+sep+oldValue,value+sep+newValue),   
	print "----------Done !----------"
	
print '-- Value Replacer'
print '-- Type help for the commands'

commands = raw_input("Commands: ").split()

for i in range(len(commands)):
	if commands[i]=='help':
		print '- The syntax should be the following: '
		print '- [1] Is the name of the file'
		print '- [2] Is the variable to look for'
		print '- [3] Is the separator between the variable and the value'
		print '- [4] Is the new value'
		print '- Example: test.txt apple = 1'
		os.execl('valuereplacer.py', '')


	if commands[i]=='exit':
		sys.exit()

if len(commands)>=4:
	filename = commands[0]
	value = commands[1]
	sep = commands[2]
	newValue = commands[3]
else:
	dataError(3,'')

if (os.path.isfile(filename) == False):
	dataError(1,'')
elif value not in open(filename).read():
	dataError(2,value)	
else:
	modifyValue(filename,value,sep,newValue)

#By Charles-Erick Tremblay
