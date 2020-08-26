from tkinter import *
# initiallisation of the tkinter widget##################

class notepad(self,file_name,content):
	def __init__(self):
		
		self.file_name = file_name
		self.content = content


root = Tk()
root.title("Notepad --")
root.geometry("800x800")

#######################################
global file_name
global content
file_name,content = str(),str()

def write_append():
	print(content)
	f= open(file_name +'.txt',"a")
	f.write(content)
	f.close()
def write_over():
	f = open(file_name+'.txt',"w")
	f.write(content)
	f.close()
#this is the warning box , if file already exists , called from checkvalue()
def warn():
	print(content)

	window =Tk()
	window.geometry('300x100')
	window.title("Warning!!")
	warn1 = Label(window,text="File Already Exist!" ,font=("Ubuntu bold",20))
	warnbut1=Button(window,text="overwrite",command=write_over)
	warnbut2=Button(window,text="Append" ,command=write_append,font=(10))
	warnbut3=Button(window,text="Cancel", command=quit)

	warn1.grid(row=0,column=1)
	warnbut1.grid(row=2,column=0)
	warnbut2.grid(row=2,column=1)
	warnbut3.grid(row=2,column=2)
	window.mainloop()


#this function is to check weather the file already exists or not , of exists it will warn about overwriting , else it creates the file
def checkvalue():
	print(content)

	try:
		f = open(file_name + '.txt',"x")
		f.close()
		write_over()
	except FileExistsError:
		warn()



def getvalue():
	file_name =entry1.get()
	content = entry2.get(1.0,"end-1c")
	checkvalue()
	# f = open(file_name + '.txt',"a")
	# f.write(content)

	

# The Frame of the tkinter
label1 = Label(root,text="FileName : ")
entry1 = Entry(root,width='800')

label2 = Label(root,text="Content : ")
entry2 = Text(root,width="800")

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

but1 = Button(root , text ='Save',command=getvalue)
but1.grid(row=2)
#############################################

root.mainloop()

