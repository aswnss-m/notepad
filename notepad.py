from tkinter import *
import pyperclip
# initiallisation of the tkinter widget


class Notepad:
   def __init__(self,width = 800,height=800):
      self.width=width
      self.height =height
      self.root = Tk()
      self.root.geometry("{}x{}".format(self.width,self.height))
      self.root.columnconfigure(1,weight=3)

      entry1 = Text(self.root, width=self.width , height=self.height)
      entry1.pack()

      menubar =Menu(self.root)

      filemenu = Menu(menubar,tearoff=0)
      filemenu.add_command(label='Save',command=save_window)
      menubar.add_cascade(label="File",menu=filemenu)
      self.root.config(menu=menubar)
      self.root.mainloop()

   def savewindow(self):
      window = Tk()
      warn_window.geometry('300x100')
      warn_window.title("Warning!!")
      warn1 = Label(warn_window,text="File Already Exist!" ,font=("Ubuntu bold",10))
      warnbut1=Button(warn_window,text="overwrite",command = self.write_over)
      warnbut2=Button(warn_window,text="Append",command = self.append_over)
      warnbut3=Button(warn_window,text="Close",command=warn_window.destroy())

      warn1.pack()
      warnbut1.pack()
      warnbut2.pack()
      warnbut3.pack()
      warn_window.mainloop()
      window.columnconfigure(0,weight=1)
      window.columnconfigure(1,weight=2)

      label1 = Label(window,test="FileName : ",padx=5,pady=5,sticky=E+W)
      file = Entry(window,sticky=E+W)
      self.filename=file.get() + '.txt'
      self.content = entry1.get(1.0,"end-1c")

      try:
         f = open(self.filename,"x")
         f = open(self.filename,"w") 
      except FileExistsError:
         self.warn()
   def warn(self):
	warn_window =Tk()
	warn_window.configure(padx=10,pady=10)
	warn_window.title("Warning!!")
	warn1 = Label(warn_window,text="File Already Exist!" ,font=("Ubuntu bold",15))
	warnbut1=Button(warn_window,text="overwrite",command = self.write_over)
	warnbut2=Button(warn_window,text="Append",command = self.append_over)
	warnbut3=Button(warn_window,text="Close",command=warn_window.destroy)

	warn1.grid(row=0,column =0,columnspan=3 , ipady=5)
	warnbut1.grid(row=1,column=0)
	warnbut2.grid(row=1,column=1)
	warnbut3.grid(row=1,column=2)
	warn_window.mainloop()
	def write_over(self):
		f = open(self.filename , "w")
		f.write(self.content)
		f.close()
	def append_over(self):
		f = open(self.filename , "a")
		f.write(self.content)
		f.close()





















root = Tk()
root.title("Notepad --")
root.geometry("800x800")
root.columnconfigure(1,weight=3)




#various funtions used in the program

def copy():
	content = entry2.get(1.0,"end-1c")
	pyperclip.copy(content)

def paste():
	content =entry2.get(1.0,"end-1c")
	entry2.delete(1.0,"end-1c")
	entry2.insert(1.0,content + '\n' + pyperclip.paste())
	

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
filemenu.add_separator()
filemenu.add_command(label = "Exit", command=root.quit)

editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label='Copy',command=copy)
editmenu.add_command(label='Paste',command=paste)


menubar.add_cascade(label='File',menu=filemenu)
menubar.add_cascade(label='Edit',menu=editmenu)
root.config(menu=menubar)


label1 = Label(root,text="FileName : ")
label2 = Label(root,text="Content : ")

entry1 = Entry(root)
entry2 = Text(root)

but1 = Button(root , text ='Save',command=getvalue,bg='black',fg='white')


label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
entry1.grid(row=0,column=1,sticky=E+W,ipadx=5,ipady=5)
entry2.grid(row=1,column=1,sticky=E+W+S,ipadx=5,ipady =5)

but1.grid(row=3,column =1 , sticky=E+W+S)




root.mainloop()

