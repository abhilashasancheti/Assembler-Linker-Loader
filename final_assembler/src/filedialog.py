import Tkinter,tkFileDialog

fileNames = []

def fileChooser():

	fileNames = []

	root = Tkinter.Tk()
	root.resizable(width=False, height=False)
	#root.geometry("500x500+200+300")
	filez = tkFileDialog.askopenfilenames(parent=root,title='Choose Input files ')
	#print filez[-1],filez[-2]
	#print root.tk.splitlist(filez)
	for f in filez:
		#print f
		fileNames.append(f)


	return fileNames

#fileChooser()