import os,sys
from src.assembler import *
from src.linker import *
from src.loader import *
from src.filedialog import *
from src.simulator import *

#open file dialog
fileNames = fileChooser()
#print fileNames

if len(fileNames) < 1:
	#sys.exit()
	print 'No file selected !! \nChoose atleast one file'
	quit()

#Assembler 
raw_input('Start processing the code..... ')
pass1_assembler(fileNames)
raw_input('Pass 1 Assembling Done ......\nPress Enter to Coninue..... ')
pass2_assembler(fileNames)
raw_input('Pass 2 Assembling Done ......\nPress Enter to Coninue..... ')

#Linker
linkedFile = mergeFiles(fileNames)
extern_replacer(fileNames , linkedFile)
raw_input('Linking Done ......\nPress Enter to Coninue..... ')

#Loader
loadedFile = offset(linkedFile)
raw_input('Loading Done ......\nPress Enter to Coninue..... ')

#simulating
simulate(loadedFile)
print 'Simulating Done ......'

print 'Terminating the processing.... '
