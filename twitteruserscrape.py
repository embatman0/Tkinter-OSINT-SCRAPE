#Import tkinter library
from tkinter import *
from tkinter import ttk
import tkinter as tk

import twint
import time


#Create an instance of tkinter frame or window
#win= Tk()
win = tk.Tk()
#Set the geometry of tkinter frame
win.geometry("900x600")
win.title('Twitter User Scrape')
win.iconbitmap(r'C:\Users\RaytheonCAP11\Downloads\Raytheonlogocrop.ico')
win.configure(background='white')

label2 = Label(win, text="Choose how many tweets to return", font=("Helvetica", 20), bg= "white", fg="#d32b3e")
label2.pack(ipadx=10, ipady=10)

w1 = Scale(win, from_=20, to=50, orient=HORIZONTAL, bg ="white")
w1.pack()

def get_value():
   e_text=entry.get()
   print(e_text)

def scrape():
    
    c = twint.Config()
    c.Username = entry.get()
    c.Limit = w1.get()
    print(w1.get())
    c.Output = (entry.get() + '.txt')
    # Run   
    twint.run.Search(c)

def openfile():
    win.destroy()
    import tkinteropenprogram

def callboth():
    get_value()
    scrape()
    openfile()
    win.destroy()


label3 = Label(win, text="Type in twitter handle", font=("Helvetica", 20), bg= "white", fg="#d32b3e")
label3.pack(ipadx=1, ipady=1)
label4 = Label(win, text="HOSTSalford", font=("Helvetica", 14), bg= "white", fg="#d32b3e")
label4.pack(ipadx=1, ipady=1)
#Create an Entry Widget
entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 10)

#Create a button to display the text of entry widget
button= ttk.Button(win, text="Enter", command= callboth)
button.pack()

bg = PhotoImage(file = "twitter.png")
label1= Label(win, image = bg)
label1.pack()

win.mainloop()
