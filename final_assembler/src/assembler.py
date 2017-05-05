
import re
import os,sys

opcodeLengthTable = {}
symbolTable = {}
variableScopeTable = {}
variableTable = {}
fileLength = {}
opcodeLengthTable = {}
offset_if = {}
offset = []
#Function to cacluate the no. of addresses consumed by each segment of code
def createLengthTable():
	configFile = open('opcodeslength.config', 'r')
	opcode = configFile.read()
	lines = opcode.split('\n')	
	for line in lines :
		line = line.lstrip().rstrip()
		if (line!='') :
			tags = line.split(' ')
			opcodeLengthTable[tags[0]]=tags[1]
	configFile.close()

createLengthTable()

#Function to find if the declared variable has 'GLOBAL' or 'LOCAL' scope
def scopeVariable( line ):
	if 'GLOBAL' in line :
		return 'GLOBAL'			
	else : 
		return 'LOCAL'

#fileNames = ['inp.txt']
#function to pass1 assembler
def pass1_assembler(fileNames):
	byteCount =0
	for fileName in fileNames :

		
		inputFile = open(fileName, 'r')
		fileName = fileName.split('.')[0]
		#fileLength[fileName] = i		
		i = 0
		j = 0
		k = 0
		t = 0
		offset_if[fileName] = {}
		symbolTable[fileName] = {}
		variableTable[fileName] = {}		
		variableScopeTable[fileName] = {}

		 #variableValue[fileName] = {}
		code = inputFile.read()
		lines = code.split('\n')
		tableFile = open(fileName+'.pre', 'a')	
		for line in lines :
			line = line.lstrip().rstrip()
			# tag = ''
			# if len(line.split(':')) > 1:
			# 	tag = line.split(':')[0].rstrip().lstrip()
			# 	symbolTable[fileName][tag] = i
			if 'extern' in line:
				line = str(line)
				words = line.split()
				variableTable[fileName][words[1]] = 'extern ' + words[1]
			if 'var' in line:
				line = str(line)
				words = line.split()
				
				variableScopeTable[fileName][words[1]] = scopeVariable(line)
				#what about tag[2]
				byteCount = byteCount+3
				variableTable[fileName][words[1]] = byteCount
				byteCount = byteCount+1
				translates= ['JMP '+str(byteCount) , 'db ' + words[3]]
				for translate in translates:
					tableFile.write(translate + '\n')
				
			elif '=' in line and '+' in line:
				line = str(line)
				words = line.split(' ')
				if re.match('\d' , words[2]) and re.match('\d' , words[4]):
					translates = [ 'MVI A, '+ words[2] , 'ADI '+ words[4], 'STA '+ str(variableTable[fileName][words[0]])]
				elif re.match('\d' , words[2]) and words[4].isalpha():
					translates = ['LDA '+str(variableTable[fileName][words[4]]), 'ADI '+ words[2], 'STA '+ str(variableTable[fileName][words[0]])]
				elif re.match('\d' , words[4]) and words[2].isalpha():
					translates = ['LDA '+str(variableTable[fileName][words[2]]), 'ADI '+ words[4], 'STA '+ str(variableTable[fileName][words[0]])]
				elif words[2].isalpha() and words[4].isalpha():
					translates = [ 'LDA '+ str(variableTable[fileName][words[2]]) ,'MOV B, A', 'LDA '+ str(variableTable[fileName][words[4]]),'ADD B','STA '+ str(variableTable[fileName][words[0]]) ]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')
			elif '=' in line and '-' in line:
				line = str(line)
				words = line.split()
				if re.match('\d' , words[2]) and re.match('\d' , words[4]):
					translates = [ 'MVI A, '+words[2] , 'SUI '+ words[4], 'STA '+ str(variableTable[fileName][words[0]]) ]
				elif re.match('\d' , words[2]) and words[4].isalpha():
					translates = [ 'LDA '+ str(variableTable[fileName][words[4]]), 'MOV B, A' , 'MVI A, '+ words[2], 'SUB B', 'STA '+ str(variableTable[fileName][words[0]])]
				elif re.match('\d' , words[4]) and words[2].isalpha():
					translates = ['LDA '+ str(variableTable[fileName][words[2]]), 'SUI '+words[4], 'STA '+ str(variableTable[fileName][words[0]])]
				elif words[2].isalpha() and words[4].isalpha():
					translates = [ 'LDA '+str(variableTable[fileName][words[4]]) ,'MOV B, A', 'LDA '+str(variableTable[fileName][words[2]]),'SUB B','STA '+str(variableTable[fileName][words[0]])]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')
			elif '|' in line:
				line = str(line)
				words = line.split(' ')
				translates = ['LDA '+str(variableTable[fileName][words[2]]) ,'MOV B, A', 'LDA '+str(variableTable[fileName][words[0]]),'ORA B','STA '+str(variableTable[fileName][words[0]])]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')
			elif '&' in line:
				line = str(line)
				words = line.split(' ')
				translates = ['LDA '+str(variableTable[fileName][words[2]]) ,'MOV B, A', 'LDA '+str(variableTable[fileName][words[0]]),'ANA B','STA '+str(variableTable[fileName][words[0]])]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')
			elif  re.match('[A-Za-z]\s[=]\s[0-9]' , line) :
				line = str(line)
				words = line.split()
				translates = [ 'MVI A, '+words[2] , 'STA '+str(variableTable[fileName][words[0]]) ]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')	

			elif  re.match('[A-Za-z]\s[=]\s[A-Za-z]' , line) :
				line = str(line)
				words = line.split()
				translates = ['LDA '+str(variableTable[fileName][words[2]]) ,'STA '+str(variableTable[fileName][words[0]])]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')

			elif  'if' in line and '>' in line:
				line = str(line)
				words = line.split()
				j= j+1
				translates = ['LDA '+str(variableTable[fileName][words[2]]) ,'MOV B, A','LDA '+str(variableTable[fileName][words[4]]),'SUB B','JP ' + 'x_'+str(j),'JZ '+'x_'+ str(j)]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')

			elif  'if' in line and '=' in line:
				line = str(line)
				words = line.split()
				j = j+1
				translates = ['LDA '+str(variableTable[fileName][words[2]]),'MOV B, A','LDA '+str(variableTable[fileName][words[4]]) ,'SUB B','JNZ ' +'x_'+str(j)]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')
			elif 'endif' in line:
				z = 'x_'+str(j)
				offset_if[fileName][z] = byteCount
				

			elif 'loop' in line :
				#print line, " l"

				line = str(line)
				words = line.split()
				print words[1]
				translates = [ 'PUSH D' ,'MVI D, ' + words[1]]
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
						if tag == 'MVI':
							offset.append(byteCount)
						k=len(offset)
						print k , 'loop'
					tableFile.write(translate + '\n')
			elif 'end' in line:
				
				line = str(line)
				words = line.split()
				print k , 'end'
				print k-1 , str(offset[k-1]) 
				translates = [ 'MOV A, D','SUI 1' , 'MOV D, A', 'JNZ ' + str(offset[k-1])  , 'POP D']
				k=k-1
				for translate in translates:
					tags = translate.split(' ')
					tag = tags[0]
					#print line[0]
					if tag in opcodeLengthTable:
						byteCount = byteCount + int(opcodeLengthTable[tag])
					tableFile.write(translate + '\n')
		inputFile.close()
		tableFile.close()
	return 

	# symbolTable = {}
	# variableScopeTable = {}
	# variableTable = {}
	# fileLength = {}
	# opcodeLengthTable = {}

#pass1_assembler(fileNames)

def pass2_assembler(fileNames):
	for fileName in fileNames:
		fileName = fileName.split('.')[0]

		with open(fileName+'.pre', "r") as sources:
			lines = sources.readlines()

		with open(fileName+'.pre.s', "w") as sources:
			for lin in lines:
				if 'x_' in lin:
					inst = lin.strip()
					inst = inst.split()
					z = inst[1]
					sources.write(lin.replace(inst[1],str(offset_if[fileName][z])))
				else:
					sources.write(lin)
	return

#pass2_assembler(fileNames)

