from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser


# create the root window
root = tk.Tk()
root.geometry("1920x1080")
root.title('OSINT')
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

# display an image label
photo = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\Raytheonlogo.png',)
image_label = ttk.Label( root, image=photo)
image_label.pack(anchor='n', ipadx=0, ipady=0)


def openweb1():
    webbrowser.open("https://www.exploit-db.com/google-hacking-database")

def openweb2():
    webbrowser.open("https://www.shodan.io/")

def openweb3():
    webbrowser.open("https://www.hunter.io/")

def openweb4():
    webbrowser.open("https://archive.org/web/")

def option1():
    root.destroy()
    import tkinterDemo 


label = Label(root, text="Welcome to OSINT", font=("Helvetica", 24), bg= "white", fg="#d32b3e")
label.pack(ipadx=10, ipady=10)


img1 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\spiderblack.png',)
img2 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\shodanlogo4.png',)
img3 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\Hunteriologo.png',)
img4 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\internetarchive.png',)
img5 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\back.png',)


b1 = Button(root, text="Google Dorks",font=("Helvetica", 16), fg="#d32b3e", image=img1, compound="bottom", command=openweb1, bd=3, bg="white", relief="flat").place(x=200, y=300)
b2 = Button(root, text="Showdan", font=("Helvetica", 16), fg="#d32b3e", image=img2, compound="bottom", command=openweb2, bd=3, bg="white", relief="flat").place(x=400, y=300)
b3 = Button(root, text="Hunter",font=("Helvetica", 16), fg="#d32b3e", image=img3, compound="bottom", command=openweb3, bd=3, bg="white", relief="flat").place(x=600, y=300)
b4 = Button(root, text="Waybackmachine", font=("Helvetica", 16), fg="#d32b3e", image=img4, compound="bottom", command=openweb4, bd=3, bg="white", relief="flat").place(x=800, y=300)
b5 = Button(root, text="Go back", font=("Helvetica", 16), fg="#d32b3e", image=img5, compound="bottom", command=option1, bd=3, bg="white", relief="flat").place(x=1070, y=300)


root.mainloop()
