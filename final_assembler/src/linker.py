import os,sys
import assembler

def mergeFiles(fileNames):
	temp = fileNames[0].split('.')
	completeFile = temp[0]
	linkedFile = completeFile+'.linked.8085'
	with open(linkedFile,'w') as outfile:
		for fileName in fileNames:
			fileName = fileName.split('.')[0]
			with open(fileName+'.pre.s') as infile:
				for line in infile:
					outfile.write(line)
	filehlt = open(linkedFile,'a')
	line = 'hlt'
	filehlt.write(line)
	filehlt.close()
	return linkedFile


def extern_replacer(fileNames , name):
	with open(name, "r") as sources:
				lines = sources.readlines()

	with open(name, "w") as sources:
		for lin in lines:
			if 'extern' in lin:
				inst = lin.strip()
				inst = inst.split()
				tag = inst[2]
				for fileName in fileNames:
					fileName = fileName.split('.')[0]
					for key, value in assembler.variableTable[fileName].items():
						if tag in key:
						 	location = assembler.variableTable[fileName][tag]
				lin = lin.replace(inst[1] ,str(location))
				sources.write(lin.replace(inst[2] ,''))
			else :
				sources.write(lin)

	return


	
