from tkinter import *
# initiallisation of the tkinter widget


root = Tk()
root.title("Notepad --")
root.geometry("800x800")
root.columnconfigure(1,weight=3)




#various funtions used in the program

#this function adds the content to an existing file ; the file with which the filename and location suites ; called from warn()
def write_append(x,y):
	print("calling Append function")
	file_name , content = x,y
	f= open(file_name +'.txt',"a")
	f.write(content)
	f.close()

#this funtion deletes all the previous content in the file and overwrites with new content ; the file with which the filename and location suites ; called from warn()
def write_over(x,y):
	print("calling write_over function")
	file_name , content = x,y
	f = open(file_name+'.txt',"w")
	f.write(content)
	f.close()

#this is the warning box , if file already exists ; called from checkvalue()
def warn(x,y):
	file_name , content = x,y

	#this is a new tkinter window for the warning box
	warn_window =Tk()
	warn_window.geometry('300x100')
	warn_window.title("Warning!!")
	

	warn1 = Label(warn_window,text="File Already Exist!" ,font=("Ubuntu bold",10))
	warnbut1=Button(warn_window,text="overwrite",command= lambda: write_over(file_name,content))
	warnbut2=Button(warn_window,text="Append" ,command= lambda: write_append(file_name,content),font=(9))
	warnbut3=Button(warn_window,text="Close", command= lambda: warn_window.destroy())

	warn1.grid(row=0,column=1)
	warnbut1.grid(row=2,column=0)
	warnbut2.grid(row=2,column=1)
	warnbut3.grid(row=2,column=2)
	warn_window.mainloop()


#this function is to check weather the file already exists or not , If exists it will warn about overwriting , else it creates the file
def checkvalue(x,y):
	file_name , content = x,y
	if content == "" and file_name == "":
		return False

	try:
		f = open(file_name + '.txt',"x")
		write_over(file_name,content)

	except FileExistsError:
		warn(file_name,content)



#this funtion is used to collect data from the tkinter entries
def getvalue():
	file_name = entry1.get()
	content = entry2.get(1.0,"end-1c")
	checkvalue(file_name,content)


	

# The Frame of the tkinter

#main menubar
menubar = Menu(root)

#drop-down menus inside menubar
filemenu = Menu(menubar,tearoff =0)
filemenu.add_command(label = 'Save',command = getvalue)


label1 = Label(root,text="FileName : ")
label2 = Label(root,text="Content : ")

entry1 = Entry(root)
entry2 = Text(root)

but1 = Button(root , text ='Save',command=getvalue,bg='black',fg='white')


label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
entry1.grid(row=0,column=1,sticky=E+W,ipadx=5,ipady=5)
entry2.grid(row=1,column=1,sticky=E+W,ipadx=5,ipady =5)

but1.grid(row=3,column =1 , sticky=E+W+S)




root.mainloop()

