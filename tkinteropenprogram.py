# Import the required Libraries
from tkinter import *
from tkinter import filedialog
import os

#Create an instance of tkinter frame
win= Tk()

#Set the geometry for the window or frame
win.geometry("600x400")

#Define a function to open the application

def app():
   file= filedialog.askopenfilename()
   text.config(text= file)
   #Open the program
   os.system('"%s"' %file)

#Create a button
Button(win, text='Click to Open a Program',font=('Poppins bold', 10),
command=app).pack(pady=20)

#Create a Label after button event
text= Label(win, text= "", font= ('Poppins bold', 10))
text.pack(pady=20)

#Keep running the window or frame
win.mainloop()