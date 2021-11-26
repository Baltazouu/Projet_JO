from tkinter import*
from tkinter import  messagebox
from PIL import Image, ImageTk
import requests
import webbrowser
from math import*
import pyglet

from jo_en import*
from jo_fr import*


##MADE BY CYPRIEN DUROY, ARTHUR LECOMTE, BAPTISTE DUDONNE TG3 ALBERT SOREL

class home:

    def __init__(self):
        self.window = Tk()
        self.window.title("Carbon Footsprint Calculator")
        self.window.geometry("875x650")
        self.window.minsize(850, 650)
        self.window.config(background='#41B77F')
        self.window.iconbitmap("images/trees.ico")
        pyglet.font.add_file('fonts/OpenSans.ttf')

        self.frame1 = Frame(self.window,bg='#41B77F')# initialization et couleur de fond
        self.create_fully_window()# creation des composants
        #self.frame.pack(expand=YES)# empaquetage


    def create_fully_window(self):


        self.frame1.pack(expand=YES)#now we create the Window
        label_title = Label(self.frame1, text="Choose your language\n",
         font=("Open Sans SemiBold", 28), bg='#41B77F', fg='white')
        label_title.pack()
        label_subtitle = Label(self.frame1, text="Choisis ta langue  \n", #create_subtitle :
        font=("Courrier", 20), bg='#41B77F', fg='white')
        label_subtitle.pack(side=TOP)

        btn_1 =Button(self.frame1,text="English",width=10,font=("Courrier", 18),bg='#41B77F', fg='white', command = self.start_en)
        btn_2 = Button(self.frame1, text="Français",width=10, font=("Courrier", 18), bg='#41B77F', fg='white', command = self.start_fr)

        btn_2.pack(side=BOTTOM,padx=30,pady=10)
        btn_1.pack(side=BOTTOM,padx=30,pady=10)

    def start_en(self):
        self.window.destroy()
        frame = Carbon_Calculator_en()
        frame.window.mainloop()

    def start_fr(self):
        self.window.destroy()
        frame = Carbon_Calculator_fr()
        frame.window.mainloop()

frame1 = home()
frame1.window.mainloop()



