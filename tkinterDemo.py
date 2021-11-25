from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser


# create the root window
root = tk.Tk()
root.geometry("1920x1080")
root.title('OSINT and Scraping')
root.iconbitmap(r'C:\Users\RaytheonCAP11\Downloads\Raytheonlogocrop.ico')
root.configure(background='white')

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)


    def exitProgram(self):
        exit()
app = Window(root)


def option1():
    root.destroy()
    import tkinterOSINT

def option2():
    root.destroy()
    import tkinterscrapev3 




# display an image label
photo = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\Raytheonlogo.png',)
image_label = ttk.Label( root, image=photo)
image_label.pack(anchor='n', ipadx=0, ipady=0)



label = Label(root, text="Welcome to The Raytheon Cyber Security Bootcamp", font=("Arial", 24), bg= "white", fg="#d32b3e")
label.pack(ipadx=10, ipady=20)

label = Label(root, text="Please choose a subject for a live demo", font=("Arial", 20), bg= "white", fg="#d32b3e")
label.pack(ipadx=10, ipady=10)


img1 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\osint1.png',)
img2 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\robot.png',)
img3 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\frame.png',)


b0 = Button(root, text="Linkedin",font=("Arial", 16), fg="black", compound="bottom", image=img3, command=option1, bd=3, bg="white", relief="flat").place(x=50, y=5)
b1 = Button(root, text="OSINT",font=("Arial", 16), fg="#d32b3e", compound="bottom", image=img1, command=option1, bd=3, bg="white", relief="flat").place(x=420, y=300)
b2 = Button(root, text="Scraper", font=("Arial", 16), fg="#d32b3e", compound="bottom", image=img2, command=option2, bd=3, bg="white", relief="flat").place(x=700, y=300)


root.mainloop()
