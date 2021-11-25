from tkinter import *
import tkinter as tk
import webbrowser
import twint


def scrape1():
    root.destroy()
    import twitteruserscrape 
def scrape2():
    root.destroy()
    import twitterlocationscrape 

def scrape3():
    root.destroy()
    import twitterkeywordscrape 


# create the root window
root = tk.Tk()
root.geometry("1920x1080")
root.title('Twitter scraper')
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
    import tkinterDemo


# display an image label
photo = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\Raytheonlogo.png',)
image_label = tk.Label(
    root,
    image=photo,
    
)
image_label.pack()



label = Label(root, text="Welcome to twitter scraping", font=("Helvetica", 24), bg= "white", fg="#d32b3e")
label.pack(ipadx=10, ipady=10)
label = Label(root, text="Please choose your scraper", font=("Helvetica", 20), bg= "white", fg="#d32b3e")
label.pack(ipadx=10, ipady=10)

img1 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\user.png',)
img2 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\location.png',)
img3 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\keyword.png',)
img4 = tk.PhotoImage(file=r'C:\Users\RaytheonCAP11\Downloads\back.png',)


b1 = Button(root, text="User",font=("Helvetica", 16), fg="#d32b3e", image=img1, compound="bottom", command=scrape1, bd=3, bg="white", relief="flat").place(x=350, y=300)
b2 = Button(root, text="Location", font=("Helvetica", 16), fg="#d32b3e", image=img2, compound="bottom", command=scrape2, bd=3, bg="white", relief="flat").place(x=550, y=300)
b3 = Button(root, text="Keyword",font=("Helvetica", 16), fg="#d32b3e", image=img3, compound="bottom", command=scrape3, bd=3, bg="white", relief="flat").place(x=750, y=300)
b4 = Button(root, text="Go back", font=("Helvetica", 16), fg="#d32b3e", image=img4, compound="bottom", command=option1, bd=3, bg="white", relief="flat").place(x=1070, y=300)



root.mainloop()