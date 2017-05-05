import os,sys

#linkedFile = 'inp.linked.8085'
def offset(linkedFile):
	try:
		location = input('Where to load:')
	except:
		location = input('Where to load:')
	#location = str(location)
	loadedFile = linkedFile.split('.')[0]
	loadedFile = loadedFile+'.loaded.8085'
	with open(linkedFile, "r") as sources:
			lines = sources.readlines()

	with open(loadedFile, "w") as sources:
		for lin in lines:
			#print lin
			#if 'JMP' in lin or 'JP' in lin or 'JNZ' in lin or 'JZ' or 'LDA' in lin or 'STA' in lin: 
			if lin.startswith('JMP') or lin.startswith('JNZ') or lin.startswith('JP') or lin.startswith('JZ')or lin.startswith('LDA') or lin.startswith('STA'):
				inst = lin.strip()
				inst = inst.split()
				#print inst , "i"
				z = inst[1]
				sources.write(lin.replace(inst[1], str(int(inst[1])+int(location))))
			else:
				sources.write(lin)
	return loadedFile

#offset(linkedFile)
