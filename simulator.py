opcodeLengthTable = {}
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


memory = {}
reg = {}
pc = 0
sp = 100
flag = {}
code = {}
#memory['3'] = 4
reg['C'] = 0
reg['A'] = 0
reg['B'] = 0
reg['D'] = 0
reg['E'] = 0
reg['H'] = 0
reg['L'] = 0
flag['S'] = 0
flag['Z'] = 0
flag['P'] = 0
flag['CY'] = 0
flag['AC'] = 0
bytecount = 0
offset = 0
pc1 = 0
def allocate (filename):
	offset = raw_input("Where to Load in memory?")
	inputFile = open(filename , "r")
	inp = inputFile.read()
	lines = inp.split('\n') 
	pc = 0
	sp = 100
	pc1 = 0
	bytecount=int(offset)
	#lines = [ 'JMP 4 ','db 4', 'JMP 8','db 6','LDA 3' ,'MVI C, 3' ,'MOV B, A' ,'STA 4']
	for line in lines :
		line = line.lstrip().rstrip()
		print line
		# if not 'db' in line:
		# 	print 'pc = ' , pc 
		# 	print 'sp = ' , sp
		# 	print 'A = ' , reg['A']
		# 	print 'B = ' , reg['B']
		# 	print 'C = ' , reg['C']
		# 	print 'D = ' , reg['D']
		# 	print 'E = ' , reg['E']
		# 	print 'H = ' , reg['H']
		# 	print 'L = ' , reg['L']
		# 	print 'S = ' , flag['S']
		# 	print 'Z = ' , flag['Z']
		# 	print 'AC = ' , flag['AC']
		# 	print 'P = ' , flag['P']
		# 	print 'CY = ' , flag['CY']
		# 	for key , value  in memory.items():
		# 		print key  , value
		
		if 'db' in line:
			line = str(line)
			words = line.split()
			memory[str(bytecount)]= int(words[1]) 
			 
		elif 'JMP' in line :
			print "imahere"
			line = str(line)
			words = line.split()
			code[bytecount] = line
			#pc1 = int(words[1])
		elif  'JP' in line :
			line = str(line)
			words = line.split()
			code[bytecount] = line
			#if flag['S'] == 0:
			#	pc1 = int(words[1])
			#else:
			#pc1 = byteCount + int(opcodeLengthTable[inst])

		elif 'JNZ' in line :
			line = str(line)
			words = line.split()
			code[bytecount] = line
			#if flag['Z'] == 0:
			#	pc1 = int(words[1])
			#else:
			#pc1 = byteCount + int(opcodeLengthTable[inst])

		elif  'JZ' in line :
			line = str(line)
			words = line.split()
			code[bytecount] = line
			#if flag['Z'] == 1:
			#	pc1 = int(words[1])
			#else:
			#pc1 = byteCount + int(opcodeLengthTable[inst])

		elif line.startswith('LDA'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			#reg['A'] = memory[words[1]]
		 
		elif line.startswith('STA'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			#memory[words[1]] = reg['A']
		elif line.startswith('MOV'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			#dest = words[1].replace(',','')
			#src = words[2]
			#reg[dest] = reg [src]
		elif line.startswith('MVI'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			#dest = words[1].replace(',','')
			#reg[dest] = int(words[2])
		elif line.startswith('SUI'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			# if reg['A'] < int(words[1]):
			# 	flag['CY'] = 1
			# else:
			# 	flag['CY'] = 0
			# reg['A'] = reg['A'] - int(words[1])
			# c = '{0:08b}'.format(reg['A']).count("1") % 2
			# s = int('{0:08b}'.format(reg['A'])[0])
			# if  c == 0 :
			# 	flag['P'] = 1
			# else: 
			# 	flag['P'] = 0
			# if reg['A'] == 0:
			# 	flag['Z'] = 1
			# else:
			# 	flag['Z'] = 0
			
			# if s == 0:
			# 	flag['S'] = 0
			# elif s == 1:
			# 	flag['S'] = 1
			# flag['AC'] = 0
		elif line.startswith('ADD'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			# reg['A'] = reg['A'] + reg[words[1]]
			# if reg['A'] > 255:
			# 	flag['CY'] = 1
			# else:
			# 	flag['CY'] = 0
			# c = '{0:08b}'.format(reg['A']).count("1") % 2
			# s = int('{0:08b}'.format(reg['A'])[0])

			# if  c == 0 :
			# 	flag['P'] = 1
			# else: 
			# 	flag['P'] = 0
			# if reg['A'] == 0:
			# 	flag['Z'] = 1
			# else:
			# 	flag['Z'] = 0
			
			# if s == 0:
			# 	flag['S'] = 0
			# elif s == 1:
			# 	flag['S'] = 1
			# if int('{0:08b}'.format(reg['A'])[4:8],2) + int('{0:08b}'.format(reg[words[1]])[4:8],2) > 16:
			# 	flag['AC'] = 1
			# else:
			# 	flag['AC'] = 0


		elif line.startswith('SUB'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			# if reg['A'] < reg[words[1]]:
			# 	flag['CY'] = 1
			# else:
			# 	flag['CY'] = 0
			# reg['A'] = reg['A'] - reg[words[1]]
			# c = '{0:08b}'.format(reg['A']).count("1") % 2
			# s = int('{0:08b}'.format(reg['A'])[0])
			# if  c == 0 :
			# 	flag['P'] = 1
			# else: 
			# 	flag['P'] = 0
			# if reg['A'] == 0:
			# 	flag['Z'] = 1
			# else:
			# 	flag['Z'] = 0
			
			# if s == 0:
			# 	flag['S'] = 0
			# elif s == 1:
			# 	flag['S'] = 1
			# flag['AC'] = 0
		elif line.startswith('ADI'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			# reg['A'] = reg['A'] + int(words[1])
			# if reg['A'] > 255:
			# 	flag['CY'] = 1
			# else:
			# 	flag['CY'] = 0
			# c = '{0:08b}'.format(reg['A']).count("1") % 2
			# s = int('{0:08b}'.format(reg['A'])[0])
			# if  c == 0 :
			# 	flag['P'] = 1
			# else: 
			# 	flag['P'] = 0
			# if reg['A'] == 0:
			# 	flag['Z'] = 1
			# else:
			# 	flag['Z'] = 0
			
			# if s == 0:
			# 	flag['S'] = 0
			# elif s == 1:
			# 	flag['S'] = 1	
			# if int('{0:08b}'.format(reg['A'])[4:8],2) + int('{0:08b}'.format(int(words[1]))[4:8],2) > 16:
			# 	flag['AC'] = 1
			# else:
			# 	flag['AC'] = 0
		elif line.startswith('ORA'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			# reg['A'] = reg['A'] |reg[words[1]]
			# c = '{0:08b}'.format(reg['A']).count("1") % 2
			# s = int('{0:08b}'.format(reg['A'])[0])
			# if  c == 0 :
			# 	flag['P'] = 1
			# else: 
			# 	flag['P'] = 0
			# if reg['A'] == 0:
			# 	flag['Z'] = 1
			# else:
			# 	flag['Z'] = 0
			
			# if s == 0:
			# 	flag['S'] = 0
			# elif s == 1:
			# 	flag['S'] = 1
			# flag['AC'] = 0
			# flag['CY'] = 0
		elif line.startswith('ANA'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			# reg['A'] = reg['A'] & reg[words[1]]
			# c = '{0:08b}'.format(reg['A']).count("1") % 2
			# s = int('{0:08b}'.format(reg['A'])[0])
			# if  c == 0 :
			# 	flag['P'] = 1
			# else: 
			# 	flag['P'] = 0
			# if reg['A'] == 0:
			# 	flag['Z'] = 1
			# else:
			# 	flag['Z'] = 0  
			
			# if s == 0:
			# 	flag['S'] = 0
			# elif s == 1:
			# 	flag['S'] = 1
			# flag['AC'] = 1
			# flag['CY'] = 0
		elif line.startswith('PUSH'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			# memory[str(sp)] = reg[words[1]]
			# sp = sp - 1
			# if words[1] == 'D':
			# 	memory[str(sp)] = reg['E']
			# elif words[1] == 'B':
			# 	memory[str(sp)] = reg['C']
			# elif words[1] == 'H':
			# 	memory[str(sp)] = reg['L']			
			# sp = sp - 1
		elif line.startswith('POP'):
			line = str(line)
			words = line.split()
			code[bytecount] = line
			# sp = sp + 1
			# if words[1] == 'D':
			# 	reg['E'] = memory[str(sp)] 
			# elif words[1] == 'B':
			# 	reg['C'] = memory[str(sp)]  
			# elif words[1] == 'H':
			# 	reg['L'] = memory[str(sp)] 
			# sp = sp + 1
			# reg[words[1]] = memory[str(sp)] 
		elif 'hlt' in line:
			code[bytecount] = line
			break
		inst = line.split()[0]
		print inst
		if not 'db' in line:
			print int(opcodeLengthTable[inst])
			bytecount = bytecount + int(opcodeLengthTable[inst])
		else: 
			bytecount = bytecount + 1
		
		# if 'JMP' in line or 'JP' in line or 'JNZ' in line or 'JZ' in line:
		# 	pc = pc1
		# elif 'db' in line:
		# 	pc = pc1
		# else:
		# 	pc = byteCount
	for key , value  in code.items():
			print key  , value
	print "memory          "
	for key , value  in memory.items():
			print key  , value

	return


allocate('inp.loaded.8085')



reg = {}

sp = 100
flag = {}
#memory['3'] = 4
reg['C'] = 0
reg['A'] = 0
reg['B'] = 0
reg['D'] = 0
reg['E'] = 0
reg['H'] = 0
reg['L'] = 0
flag['S'] = 0
flag['Z'] = 0
flag['P'] = 0
flag['CY'] = 0
flag['AC'] = 0


pc1 = 0
def simulate (filename):
	#offset = raw_input("Where to Load in memory?")
	#inputFile = open(filename , "r")
	#code = inputFile.read()
	pc=0
	sp = 100
	pc1 = 0
	#byteCount=int(offset)
	choice = 'Y'
	while ( choice == 'y' or choice == 'Y'):
		line = code[pc] 
		
		#lines = [ 'JMP 4 ','db 4', 'JMP 8','db 6','LDA 3' ,'MVI C, 3' ,'MOV B, A' ,'STA 4']
		#for line in lines :
		line = line.lstrip().rstrip()
		if not 'db' in line:
			print 'pc = ' , pc 
			print 'sp = ' , sp
			print 'A = ' , reg['A']
			print 'B = ' , reg['B']
			print 'C = ' , reg['C']
			print 'D = ' , reg['D']
			print 'E = ' , reg['E']
			print 'H = ' , reg['H']
			print 'L = ' , reg['L']
			print 'S = ' , flag['S']
			print 'Z = ' , flag['Z']
			print 'AC = ' , flag['AC']
			print 'P = ' , flag['P']
			print 'CY = ' , flag['CY']
			for key , value  in memory.items():
				print key  , value
		
		if 'db' in line:
			line = str(line)
			words = line.split()
			memory[str(byteCount)]= int(words[1]) 
			 
		elif 'JMP' in line :
			line = str(line)
			words = line.split()
			pc1 = int(words[1])
		elif  'JP' in line :
			line = str(line)
			words = line.split()
			if flag['S'] == 0:
				pc1 = int(words[1])
			else:
				pc1 = pc + int(opcodeLengthTable[words[0]])

		elif 'JNZ' in line :
			line = str(line)
			words = line.split()
			if flag['Z'] == 0:
				pc1 = int(words[1])
			else:
				pc1 = pc + int(opcodeLengthTable[words[0]])

		elif  'JZ' in line :
			line = str(line)
			words = line.split()
			if flag['Z'] == 1:
				pc1 = int(words[1])
			else:
				pc1 = pc + int(opcodeLengthTable[words[0]])

		elif line.startswith('LDA'):
			line = str(line)
			words = line.split()
			reg['A'] = memory[words[1]]
		 
		elif line.startswith('STA'):
			line = str(line)
			words = line.split()
			memory[words[1]] = reg['A']
		elif line.startswith('MOV'):
			line = str(line)
			words = line.split()
			dest = words[1].replace(',','')
			src = words[2]
			reg[dest] = reg [src]
		elif line.startswith('MVI'):
			line = str(line)
			words = line.split()
			dest = words[1].replace(',','')
			reg[dest] = int(words[2])
		elif line.startswith('SUI'):
			line = str(line)
			words = line.split()
			if reg['A'] < int(words[1]):
				flag['CY'] = 1
			else:
				flag['CY'] = 0
			reg['A'] = reg['A'] - int(words[1])
			c = '{0:08b}'.format(reg['A']).count("1") % 2
			s = int('{0:08b}'.format(reg['A'])[0])
			if  c == 0 :
				flag['P'] = 1
			else: 
				flag['P'] = 0
			if reg['A'] == 0:
				flag['Z'] = 1
			else:
				flag['Z'] = 0
			
			if s == 0:
				flag['S'] = 0
			elif s == 1:
				flag['S'] = 1
			flag['AC'] = 0
		elif line.startswith('ADD'):
			line = str(line)
			words = line.split()
			reg['A'] = reg['A'] + reg[words[1]]
			if reg['A'] > 255:
				flag['CY'] = 1
			else:
				flag['CY'] = 0
			c = '{0:08b}'.format(reg['A']).count("1") % 2
			s = int('{0:08b}'.format(reg['A'])[0])

			if  c == 0 :
				flag['P'] = 1
			else: 
				flag['P'] = 0
			if reg['A'] == 0:
				flag['Z'] = 1
			else:
				flag['Z'] = 0
			
			if s == 0:
				flag['S'] = 0
			elif s == 1:
				flag['S'] = 1
			if int('{0:08b}'.format(reg['A'])[4:8],2) + int('{0:08b}'.format(reg[words[1]])[4:8],2) > 16:
				flag['AC'] = 1
			else:
				flag['AC'] = 0


		elif line.startswith('SUB'):
			line = str(line)
			words = line.split()
			if reg['A'] < reg[words[1]]:
				flag['CY'] = 1
			else:
				flag['CY'] = 0
			reg['A'] = reg['A'] - reg[words[1]]
			c = '{0:08b}'.format(reg['A']).count("1") % 2
			s = int('{0:08b}'.format(reg['A'])[0])
			if  c == 0 :
				flag['P'] = 1
			else: 
				flag['P'] = 0
			if reg['A'] == 0:
				flag['Z'] = 1
			else:
				flag['Z'] = 0
			
			if s == 0:
				flag['S'] = 0
			elif s == 1:
				flag['S'] = 1
			flag['AC'] = 0
		elif line.startswith('ADI'):
			line = str(line)
			words = line.split()
			reg['A'] = reg['A'] + int(words[1])
			if reg['A'] > 255:
				flag['CY'] = 1
			else:
				flag['CY'] = 0
			c = '{0:08b}'.format(reg['A']).count("1") % 2
			s = int('{0:08b}'.format(reg['A'])[0])
			if  c == 0 :
				flag['P'] = 1
			else: 
				flag['P'] = 0
			if reg['A'] == 0:
				flag['Z'] = 1
			else:
				flag['Z'] = 0
			
			if s == 0:
				flag['S'] = 0
			elif s == 1:
				flag['S'] = 1	
			if int('{0:08b}'.format(reg['A'])[4:8],2) + int('{0:08b}'.format(int(words[1]))[4:8],2) > 16:
				flag['AC'] = 1
			else:
				flag['AC'] = 0
		elif line.startswith('ORA'):
			line = str(line)
			words = line.split()
			reg['A'] = reg['A'] |reg[words[1]]
			c = '{0:08b}'.format(reg['A']).count("1") % 2
			s = int('{0:08b}'.format(reg['A'])[0])
			if  c == 0 :
				flag['P'] = 1
			else: 
				flag['P'] = 0
			if reg['A'] == 0:
				flag['Z'] = 1
			else:
				flag['Z'] = 0
			
			if s == 0:
				flag['S'] = 0
			elif s == 1:
				flag['S'] = 1
			flag['AC'] = 0
			flag['CY'] = 0
		elif line.startswith('ANA'):
			line = str(line)
			words = line.split()
			reg['A'] = reg['A'] & reg[words[1]]
			c = '{0:08b}'.format(reg['A']).count("1") % 2
			s = int('{0:08b}'.format(reg['A'])[0])
			if  c == 0 :
				flag['P'] = 1
			else: 
				flag['P'] = 0
			if reg['A'] == 0:
				flag['Z'] = 1
			else:
				flag['Z'] = 0  
			
			if s == 0:
				flag['S'] = 0
			elif s == 1:
				flag['S'] = 1
			flag['AC'] = 1
			flag['CY'] = 0
		elif line.startswith('PUSH'):
			line = str(line)
			words = line.split()
			memory[str(sp)] = reg[words[1]]
			sp = sp - 1
			if words[1] == 'D':
				memory[str(sp)] = reg['E']
			elif words[1] == 'B':
				memory[str(sp)] = reg['C']
			elif words[1] == 'H':
				memory[str(sp)] = reg['L']			
			sp = sp - 1
		elif line.startswith('POP'):
			line = str(line)
			words = line.split()
			sp = sp + 1
			if words[1] == 'D':
				reg['E'] = memory[str(sp)] 
			elif words[1] == 'B':
				reg['C'] = memory[str(sp)]  
			elif words[1] == 'H':
				reg['L'] = memory[str(sp)] 
			sp = sp + 1
			reg[words[1]] = memory[str(sp)] 
		elif 'hlt' in line:
			print "done"
		inst = line.split()[0]
		# if not 'db' in line:
		# 	byteCount = byteCount + int(opcodeLengthTable[inst])
		# else: 
		#		byteCount = byteCount + 1
		# if not 'db' in line:
		# 	print 'pc = ' , pc 
		# 	print 'sp = ' , sp
		# 	print 'A = ' , reg['A']
		# 	print 'B = ' , reg['B']
		# 	print 'C = ' , reg['C']
		# 	print 'D = ' , reg['D']
		# 	print 'E = ' , reg['E']
		# 	print 'H = ' , reg['H']
		# 	print 'L = ' , reg['L']
		# 	print 'S = ' , flag['S']
		# 	print 'Z = ' , flag['Z']
		# 	print 'AC = ' , flag['AC']
		# 	print 'P = ' , flag['P']
		# 	print 'CY = ' , flag['CY']
		# 	for key , value  in memory.items():
		# 		print key  , value
		if   'JMP' in line or 'JP' in line or 'JNZ' in line or 'JZ' in line:
			pc = pc1
		elif not 'hlt' in line:
			pc = pc + int(opcodeLengthTable[inst])

		# elif 'db' in line:
		# 	pc = pc1
		# else:
		# 	pc = byteCount
		if not 'db' in line and not 'hlt' in line:
			choice = raw_input("Want to Proceed to next Step[Y/N]?")
			# if choice == 'N' or choice == 'n':
			# 	break
			# elif choice == 'Y' or choice == 'y':
			# 	continue
			# else:
			# 	print "wrong choice entered"
	return 

#simulate('inp.loaded.8085')
# print 'A = ' , reg['A']
# print  ' memory[3]= ',  memory['3']
# print  ' memory[4]= ' , memory['4']
# print  ' memory[7]= ' , memory['7']

# if dest == 'B' :
# 	destination = 1
# elif dest == 'A' :
# 	destination = 0
# elif dest == 'C' :
# 	destination = 2
# elif dest == 'D' :
# 	destination = 3
# elif dest == 'E' :
# 	destination = 4
# elif dest == 'H' :
# 	destination = 5
# elif dest == 'L' :
# 	destination = 6
# if src == 'A' :
# 	source = 0
# elif src == 'B' :
# 	source = 1
# elif src == 'C' :
# 	source = 2
# elif src == 'D' :
# 	source = 3
# elif src == 'E' :
# 	source = 4
# elif src == 'H' :
# 	source = 5
# elif src == 'L' :
# 	source = 6
# if dest == 'B' :
# 	destination = 1
# elif dest == 'A' :
# 	destination = 0
# elif dest == 'C' :
# 	destination = 2
# elif dest == 'D' :
# 	destination = 3
# elif dest == 'E' :
# 	destination = 4
# elif dest == 'H' :
# 	destination = 5
# elif dest == 'L' :
# 	destination = 6

