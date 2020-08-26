from tkinter import *
# initiallisation of the tkinter widget##################


root = Tk()
root.title("Notepad --")
root.geometry("800x800")



#######################################

def write_append(x,y):
	print("calling Append function")
	file_name =x
	content =y
	f= open(file_name +'.txt',"a")
	f.write(content)
	f.close()
def write_over(x,y):
	print("calling write_over function")
	file_name =x
	content =y
	f = open(file_name+'.txt',"w")
	f.write(content)
	f.close()
#this is the warning box , if file already exists , called from checkvalue()
def warn(x,y):
	file_name =x
	content =y

	window =Tk()
	window.geometry('300x100')
	window.title("Warning!!")
	warn1 = Label(window,text="File Already Exist!" ,font=("Ubuntu bold",10))
	warnbut1=Button(window,text="overwrite",command= lambda: write_over(file_name,content))
	warnbut2=Button(window,text="Append" ,command= lambda: write_append(file_name,content),font=(9))
	warnbut3=Button(window,text="Cancel", command=quit)

	warn1.grid(row=0,column=1)
	warnbut1.grid(row=2,column=0)
	warnbut2.grid(row=2,column=1)
	warnbut3.grid(row=2,column=2)
	window.mainloop()


#this function is to check weather the file already exists or not , of exists it will warn about overwriting , else it creates the file
def checkvalue(x,y):
	file_name =x
	content =y

	try:
		f = open(file_name + '.txt',"x")

	except FileExistsError:
		print()
		warn(file_name,content)


	write_over(file_name,content)
	f.close()




def getvalue():
	file_name = entry1.get()
	content = entry2.get(1.0,"end-1c")
	checkvalue(file_name,content)
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

