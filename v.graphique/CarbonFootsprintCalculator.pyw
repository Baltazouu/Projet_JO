from tkinter import*
from tkinter import  messagebox
from PIL import Image, ImageTk
import requests
import webbrowser
from math import*
import pyglet


##MADE BY CYPRIEN DUROY, ARTHUR LECOMTE, BAPTISTE DUDONNE TG3 ALBERT SOREL

class home:

    def __init__(self):
        self.window = Tk()
        self.window.title("Carbon Footsprint Calculator")
        #self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))#("875x650")
        self.window.minsize(850, 650)
        self.window.geometry("1920x1280")
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


class Carbon_Calculator_en:

    def __init__(self):
        self.window = Tk()
        self.window.title("Carbon Footsprint Calculator")
        self.window.geometry("1920x1280")#("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.minsize(850, 650)
        self.window.config(background='#41B77F')
        self.valeur_buttton=IntVar()#valeur des btns pour le mode de transport; entier
        self.carb_trans=0 #bilan total du transport
        self.km=0 #nbr km
        self.nb=""#le nombre de personnes
        self.tree=0
        self.Destination=""
        self.Current=""
        self.nbr_etape=0 #nbr d'étape demandé
        self.etape=0 #nbr d'étape réalisé
        self.window.iconbitmap("images/trees.ico")
        pyglet.font.add_file('fonts/OpenSans.ttf')

        """////////////////Images///////////"""
        #home (back to menue)
        home= (Image.open("images/home.png"))
        resized_home= home.resize((160,140), Image.ANTIALIAS)
        self.new_home= ImageTk.PhotoImage(resized_home)
        #train image
        train= (Image.open("images/train.png"))
        resized_train= train.resize((160,140), Image.ANTIALIAS)
        self.new_train= ImageTk.PhotoImage(resized_train)
        #bus image
        bus= (Image.open("images/bus.png"))
        resized_bus= bus.resize((160,140), Image.ANTIALIAS)
        self.new_bus= ImageTk.PhotoImage(resized_bus)
        #plane image
        plane= (Image.open("images/plane.png"))
        resized_plane= plane.resize((160,140), Image.ANTIALIAS)
        self.new_plane= ImageTk.PhotoImage(resized_plane)

        self.frame = Frame(self.window,bg='#41B77F')# initialization et couleur de fond
        self.create_fully_window()# creation des composants
        #self.frame.pack(expand=YES)# empaquetage



    def source(self):
        url="https://github.com/Baltazouu/Projet_JO"
        webbrowser.open_new_tab(url)

    def create_fully_window(self):

        """
        self.frame.pack(expand=YES)#now we create the Window
        label_title = Label(self.frame, text="Carbon Footsprint Calculator\n",
         font=("Open Sans SemiBold", 28), bg='#41B77F', fg='white')
        label_title.pack()
        label_subtitle = Label(self.frame, text="Made By Albert Sorel High School  \n", #create_subtitle :
        font=("Courrier", 20), bg='#41B77F', fg='white')
        label_subtitle.pack(side=TOP)

        normandie= (Image.open("images/normandie.png"))
        resized_normandie= normandie.resize((200,85), Image.ANTIALIAS)
        self.new_normandie= ImageTk.PhotoImage(resized_normandie)
        logo_normandie=Label(self.frame,image=self.new_normandie,bg='#41B77F')

        paris2024= (Image.open("images/paris2024.png"))
        resized_paris= paris2024.resize((200,160), Image.ANTIALIAS)
        self.new_paris= ImageTk.PhotoImage(resized_paris)
        logo_paris=Label(self.frame,image=self.new_paris,bg='#41B77F')

        unss= (Image.open("images/unss.png"))
        resized_unss= unss.resize((110,60), Image.ANTIALIAS)
        self.new_unss= ImageTk.PhotoImage(resized_unss)
        logo_unss=Label(self.frame,image=self.new_unss,bg='#41B77F')

        source_btn = Button(self.frame,text='Source Code', command=self.source,width=10, font=("Open Sans SemiBold", 12), bg='white', fg='#41B77F')

        calc_button = Button(self.frame, text="Calculate Now !", font=("Open Sans SemiBold", 26), bg='white', fg='#41B77F',#create_calculate_button
        command=lambda:[label_subtitle.pack_forget(),label_title.pack_forget(),calc_button.pack_forget(),self.people_nbr(),logo_paris.pack_forget(),logo_normandie.pack_forget(),logo_unss.pack_forget(),source_btn.pack_forget()])#,self.back.pack()

        calc_button.pack()
        logo_normandie.pack(side=LEFT)
        logo_unss.pack(side=RIGHT,padx=30,pady=10)
        logo_paris.pack(side=BOTTOM,padx=30,pady=10)
        source_btn.pack(side=BOTTOM,padx=30,pady=10)
        """
        self.frame.pack(expand=YES)#now we create the Window
        label_title = Label(self.frame, text="Carbon Footsprint Calculator\n",
         font=("Open Sans SemiBold", 28), bg='#41B77F', fg='white')
        label_title.grid(row=0, column=1)

        albert_sorel =(Image.open("images/sorel_refait.png"))
        resized_albert_sorel = albert_sorel.resize((110,110), Image.ANTIALIAS)
        self.albert_sorel=ImageTk.PhotoImage(resized_albert_sorel)
        logo_albert_sorel=Label(self.frame,image=self.albert_sorel, bg='#41B77F')

        option_sport=(Image.open("images/option_sport-removebg-preview.png"))
        resized_option_sport = option_sport.resize((110,110), Image.ANTIALIAS)
        self.option_sport=ImageTk.PhotoImage(resized_option_sport)
        logo_option_sport=Label(self.frame,image=self.option_sport,bg='#41B77F')

        jones=(Image.open("images/jones-removebg-preview.png"))
        resized_jones =jones.resize((110,110), Image.ANTIALIAS)
        self.jones=ImageTk.PhotoImage(resized_jones)
        logo_jones=Label(self.frame, image=self.jones, bg='#41B77F')



        label_subtitle = Label(self.frame, text="\nMade By Albert Sorel High School  \n", #create_subtitle :
        font=("Courrier", 20), bg='#41B77F', fg='white')
        label_subtitle.grid(column=1,row=2)

        normandie= (Image.open("images/normandie.png"))
        resized_normandie= normandie.resize((200,85), Image.ANTIALIAS)
        self.new_normandie= ImageTk.PhotoImage(resized_normandie)
        logo_normandie=Label(self.frame,image=self.new_normandie,bg='#41B77F')

        paris2024= (Image.open("images/paris2024.png"))
        resized_paris= paris2024.resize((200,160), Image.ANTIALIAS)
        self.new_paris= ImageTk.PhotoImage(resized_paris)
        logo_paris=Label(self.frame,image=self.new_paris,bg='#41B77F')

        unss= (Image.open("images/unss.png"))
        resized_unss= unss.resize((110,60), Image.ANTIALIAS)
        self.new_unss= ImageTk.PhotoImage(resized_unss)
        logo_unss=Label(self.frame,image=self.new_unss,bg='#41B77F')



        source_btn = Button(self.frame,text='Source Code', command=self.source,width=10, font=("Open Sans SemiBold", 12), bg='white', fg='#41B77F')

        calc_button = Button(self.frame, text="Calculate Now !", font=("Open Sans SemiBold", 26), bg='white', fg='#41B77F',#create_calculate_button
        command=lambda:[label_subtitle.grid_forget(),label_title.grid_forget(),calc_button.grid_forget(),logo_paris.grid_forget(),logo_normandie.grid_forget(),logo_unss.grid_forget(),source_btn.grid_forget(),logo_jones.grid_forget(),logo_albert_sorel.grid_forget(),logo_option_sport.grid_forget(), label_nom.grid_forget(),self.people_nbr()])#,self.back.pack()

        label_nom = Label(self.frame, text="\nBy : Baptiste Dudonné, Cyprien Duroy, Arthur Lecomte From Lycée Albert Sorel  ", #create_subtitle :
        font=("Courrier", 16), bg='#41B77F', fg='white')

        logo_albert_sorel.grid(column=0, row=1,ipadx=4)
        logo_option_sport.grid(column=1, row=1)
        logo_paris.grid(column=2, row=1)
        calc_button.grid(column=1,row=3)
        logo_normandie.grid(column=1,row=4)
        logo_unss.grid(column=2,row=4)
        logo_jones.grid(column=0,row=4,ipadx=4)

        source_btn.grid(column=1,row=5)
        label_nom.grid(column=1,row=6)


    """///////////////////////////////////////////////// Number Of Peoples ://////////////////////////////////////////////////////////////////////:"""

    def people_nbr(self):
        home= (Image.open("images/home.png"))
        resized_home= home.resize((45,45), Image.ANTIALIAS)
        self.new_home= ImageTk.PhotoImage(resized_home)
        logo_normandie=Label(self.frame,image=self.new_home,bg='#41B77F')

        self.back= Button(self.frame,image=self.new_home,bg='#41B77F', command=self.close) #lambda:[self.close(),self.create_fully_window])
        self.back.pack(side=TOP)

        """
        back=Button(self.frame,image=new_home)
        back =Button(self.frame,image=new_home,bg='#41B77F', fg='#41B77F')
        """

        label_subtitle = Label(self.frame, text="How Many People Are You ?\n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        #Pour actualiser L'entrée et la voir en direct
        def update_label(*args):
            var_retour.set(var_entry.get())
            self.nb=var_entry.get()

        def verify():
            if var_entry.get() > 0 :
                label_subtitle.pack_forget(),entry.pack_forget(),label_space.pack_forget(),confirm_btn.pack_forget(),self.number_methods()
            else :
                messagebox.showwarning("ERROR","Please Type A Number !")

        var_entry=IntVar(value="")
        var_entry.trace("w",update_label)
        entry=Entry(self.frame, textvariable=var_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 22))
        var_retour=IntVar()
        label_space=Label(self.frame,textvariable=var_retour,font=("Courrier", 20), bg='#41B77F',fg='white')
        #retour = Label(self.frame,textvariable=var_retour,font=("Courrier", 20), bg='#41B77F',fg='white')
        confirm_btn = Button(self.frame, text="Confirm", font=("Courrier", 25), bg='white', fg='#41B77F',command=verify)
        #empaquetage


        #back.pack()
        label_subtitle.pack()
        entry.pack()
        label_space.pack()
        confirm_btn.pack()

    """////////////////////////////////////////////////////////////////// USE SEVERAL Stage ?////////////////////////////////////////////////////////"""

    def number_methods(self):
            label_subtitle = Label(self.frame, text="Do You Use Several Stages ?\n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
            btn_1 =Button(self.frame,text="YES",width=10,font=("Courrier", 18),bg='#41B77F', fg='white', command = lambda :[self.cbm_trans(),forget()])
            btn_2 = Button(self.frame, text="NO",width=10, font=("Courrier", 18), bg='#41B77F', fg='white',command=lambda:[self.start_location(),forget()])

            def forget():#to remove the widget
                label_subtitle.pack_forget(),btn_1.pack_forget(),btn_2.pack_forget()


            label_subtitle.pack()
            btn_2.pack(side=BOTTOM,padx=30,pady=10)
            btn_1.pack(side=BOTTOM,padx=30,pady=10)


    """/////////////////////////////////////////////////////////////////how many times change you methods of transport////////////////////////////////////////////////////////////////////////"""
    def cbm_trans(self):
        label_subtitle = Label(self.frame, text="How many Stages do you use ? \n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        def verify():
            if var_entry.get() > 1 :
                self.nbr_etape = var_entry.get()-1
                label_subtitle.pack_forget(),entry.pack_forget(),label_space.pack_forget(),confirm_btn.pack_forget()
                self.start_location()
            else :
                messagebox.showwarning("ERROR","Please Type A Number higher than 1 !")

        var_entry=IntVar(value="")
        entry=Entry(self.frame, textvariable=var_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 22))
        label_space=Label(self.frame,text="\n",bg='#41B77F')
        confirm_btn = Button(self.frame, text="Confirm", font=("Courrier", 25), bg='white', fg='#41B77F',command=verify)

        label_subtitle.pack()
        entry.pack()
        label_space.pack()
        confirm_btn.pack()



    """/////////////////////////////////////////////////////////////////////////////////////// ENTER DESTINATION AND START LOCATION ////////////////////////////////////////////////////////////////////////////////////"""

    def start_location(self):

        def verify_current():#in order to verify that an entry has been made

            if current_entry.get()!="":
                self.Current=current_entry.get()
                if self.nbr_etape==self.etape :
                    self.destination_location()
                elif self.nbr_etape>self.etape:
                    self.step_location()


        def forget():
            label_start.pack_forget(),current.pack_forget(),btn_confirm.pack_forget(),space.pack_forget()


        label_start=Label(self.frame, text="Enter Your Start Location :\n", font=("Courrier", 26), bg='#41B77F',fg='white')

        current_entry=StringVar()
        current=Entry(self.frame,textvariable=current_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 20))

        self.label_current=Label
        space=Label(self.frame,text="\n",bg='#41B77F')
        btn_confirm= Button(self.frame, text="Confirm Your Start City", font=("Courrier", 20), bg='white', fg='#41B77F',command = lambda :[verify_current(),forget()])

        label_start.pack()
        current.pack()
        space.pack()
        btn_confirm.pack()


    def step_location(self):

        if self.etape>=1:
            self.Current=self.Destination
        self.etape=self.etape+1
        def verify_step():#in order to verify that an entry has been made

                if step_entry.get()!="":
                    self.Destination=step_entry.get()
                    self.API()

        def forget():
                label_step.pack_forget(),step.pack_forget(),btn_confirm.pack_forget(),space.pack_forget(),self.label_current.pack_forget()

        label_step=Label(self.frame, text=f"Enter your {self.etape} Step Location : \n", font=("Courrier", 26), bg='#41B77F',fg='white')

        step_entry=StringVar()
        step=Entry(self.frame,textvariable=step_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 20))

        self.label_current=Label
        space=Label(self.frame,text="\n",bg='#41B77F')
        btn_confirm= Button(self.frame, text="Confirm Your Step City", font=("Courrier", 20), bg='white', fg='#41B77F',command = lambda :[verify_step(),forget()])

        label_step.pack()
        step.pack()
        space.pack()
        btn_confirm.pack()


    def destination_location(self):
        if self.etape>=1:
            self.Current=self.Destination
        self.etape=self.etape+1
        def city():#To Define the Destination City

            if self.valeur_buttton.get()==1:
                self.Destination="Caen"#Pont-l'évèque(49.282793557255886, 0.18484314531409504)
                label_destination.pack_forget(),radio1.pack_forget(),
                radio2.pack_forget(),radio3.pack_forget(),radio4.pack_forget(), self.label_current.pack_forget()
                self.API()
            elif self.valeur_buttton.get()==2:
                self.Destination="Deauville"
                label_destination.pack_forget(),radio1.pack_forget(),
                radio2.pack_forget(),radio3.pack_forget(),radio4.pack_forget(), self.label_current.pack_forget()
                self.API()
            elif self.valeur_buttton.get()==3:
                self.Destination="Le Havre"
                label_destination.pack_forget(),radio1.pack_forget(),
                radio2.pack_forget(),radio3.pack_forget(),radio4.pack_forget(), self.label_current.pack_forget()
                self.API()
            elif self.valeur_buttton.get()==4:
                self.Destination="Rouen"
                label_destination.pack_forget(),radio1.pack_forget(),
                radio2.pack_forget(),radio3.pack_forget(),radio4.pack_forget(), self.label_current.pack_forget()
                self.API()
        label_destination=Label(self.frame,text="\nEnter Your City Destination:\n", font=("Courrier", 26), bg='#41B77F',fg='white')

        self.valeur_buttton=IntVar()
        radio1 = Radiobutton(self.frame, text="Caen      ",command=city ,value=1,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio2= Radiobutton(self.frame, text="Deauville",command=city,  value=2,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio3=Radiobutton(self.frame, text="Le Havre",command=city , value=3,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio4=Radiobutton(self.frame, text="Rouen    ", command=city, value=4,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)

        self.label_current=Label(self.frame,text=f'Your Travel Start From {self.Current}',font=("Courrier", 20), bg='#41B77F',fg='white')
        self.label_current.pack()
        label_destination.pack()
        radio1.pack()
        radio2.pack()
        radio3.pack()
        radio4.pack()

    """/////////////////////////////////////////////////////////////////////API WINDOW///////////////////////////////////////////////////////////////////////////////////////////"""

    def API(self):#to send te request

        stop="stops="+self.Destination+"|"+self.Current
        url="https://www.distance24.org/route.json?"+stop
        while True:
            try :
                r = requests.get(url)
                break
            except (ConnectionError, requests.exceptions.ConnectionError):
                messagebox.showwarning("ERROR","Please Verify Your Internet Connexion")
                break



        rep=r.json()
        self.km=rep['distance']
        self.label_current = Label(self.frame, text=f"The Distance Between {self.Current} and {self.Destination} is of {self.km} Kilometers", font=("Courrier", 20), bg='#41B77F', fg='white')
        self.label_current.pack()
        self.method_transport()

    """//////////////////////////////////////////////////////////////////////////////// Méthod of transport ////////////////////////////////////////////////////////////////////////////////////"""

    def method_transport(self):#in order to know the method of transport you will use
            label_title = Label(self.frame, text=" \nPlease Choose Your Method Of Transport:\n  ",font=("Courrier", 20), bg='#41B77F', fg='white')

            btn_1 =Button(self.frame,image=self.new_train,font=("Courrier", 18),bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_train(),forget()])

            btn_2 = Button(self.frame, image=self.new_bus, font=("Courrier", 18), bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_bus(),forget()])

            btn_3 = Button(self.frame, image=self.new_plane, font=("Courrier", 18), bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_plane(),forget()])

            def forget():#to remove the widget
                label_title.pack_forget(),btn_1.pack_forget(),btn_2.pack_forget(),btn_3.pack_forget(), self.label_current.pack_forget()
            label_title.pack()
            btn_1.pack(side=LEFT,padx=30,pady=10)
            btn_2.pack(side=RIGHT,padx=30,pady=10)
            btn_3.pack(side=BOTTOM,padx=30,pady=10)


    """///////////////////////////////////////////////////////////////////////////////////Calculate Carbon Footsprint///////////////////////////////////////////////////////////////////////////////"""

    def bilan_trans_train(self): # for train

        carb=self.nb*self.km*0.000016
        self.carb_trans=self.carb_trans+carb
        self.carb_trans=round(self.carb_trans,2)
        if self.nbr_etape==self.etape :
            self.destination_location()
        elif self.nbr_etape>self.etape :
            self.step_location()
        else :
            self.reveal()


    def bilan_trans_bus(self):#for bus-
        carb=self.nb*self.km*0.000068
        self.carb_trans=self.carb_trans+carb
        self.carb_trans=round(self.carb_trans,2)
        if self.nbr_etape==self.etape :
            self.destination_location()
        elif self.nbr_etape>self.etape :
            self.step_location()
        else :
            self.reveal()


    def bilan_trans_plane(self):#for plane
        print(self.etape)
        print(self.nbr_etape)
        carb_plane=self.nb*self.km*0.000187
        self.carb_trans=self.carb_trans+carb_plane
        self.carb_trans=round(self.carb_trans,2)
        if self.nbr_etape==self.etape :
            self.destination_location()
        elif self.nbr_etape>self.etape :
            self.step_location()
        else :
            self.reveal()


    """/////////////////////////////////////////////////////////////////////////////////////REVEAL//////////////////////////////////////////////////////////////////////////////"""



    def final_background(self):
        tree= (Image.open("images/tree.png"))
        resized_tree= tree.resize((160,120), Image.ANTIALIAS)
        self.new_tree= ImageTk.PhotoImage(resized_tree)
        tree=Label(self.frame,image=self.new_tree,bg='#41B77F')
        tree.pack(side=BOTTOM)

    def reveal(self):
        self.tree=self.carb_trans /2.5
        self.tree=ceil(self.tree)
        self.tree=int(self.tree)
        if self.tree>1:
            self.final_background()
            tree="Trees"
        else:
            tree="Tree"
            self.final_background()
        label_subtitle = Label(self.frame, text=f"Your carbon footsprint is {self.carb_trans}  Ton of CO2\n\nFor This Travel You Should to replant {self.tree} {tree}\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        label_subtitle.pack()

    def close(self):
        self.window.destroy()
        frame = Carbon_Calculator_en()



class Carbon_Calculator_fr:

    def __init__(self):
        self.window = Tk()
        self.window.title("Carbon Footsprint Calculator")
        #self.window.attributes("-fullscreen", True)
        self.window.geometry("1920x1280")#("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.minsize(850, 650)
        self.window.config(background='#41B77F')
        self.valeur_buttton=IntVar()#valeur des btns pour le mode de transport; entier
        self.carb_trans=0 #bilan total du transport
        self.km=0 #nbr km
        self.nb=""#le nombre de personnes
        self.tree=0
        self.Destination=""
        self.Current=""
        self.nbr_etape=0 #nbr d'étape demandé
        self.etape=0 #nbr d'étape réalisé
        self.window.iconbitmap("images/trees.ico")
        pyglet.font.add_file('fonts/OpenSans.ttf')

        """////////////////Images///////////"""
        #home (back to menue)
        home= (Image.open("images/home.png"))
        resized_home= home.resize((160,140), Image.ANTIALIAS)
        self.new_home= ImageTk.PhotoImage(resized_home)
        #train image
        train= (Image.open("images/train.png"))
        resized_train= train.resize((160,140), Image.ANTIALIAS)
        self.new_train= ImageTk.PhotoImage(resized_train)
        #bus image
        bus= (Image.open("images/bus.png"))
        resized_bus= bus.resize((160,140), Image.ANTIALIAS)
        self.new_bus= ImageTk.PhotoImage(resized_bus)
        #plane image
        plane= (Image.open("images/plane.png"))
        resized_plane= plane.resize((160,140), Image.ANTIALIAS)
        self.new_plane= ImageTk.PhotoImage(resized_plane)

        self.frame = Frame(self.window,bg='#41B77F')# initialization et couleur de fond
        self.create_fully_window()# creation des composants
        #self.frame.pack(expand=YES)# empaquetage



    def source(self):
        url="https://github.com/Baltazouu/Projet_JO"
        webbrowser.open_new_tab(url)

    def create_fully_window(self):


        self.frame.pack(expand=YES)#now we create the Window
        label_title = Label(self.frame, text="Calculateur d'Empreinte Carbone\n",
         font=("Open Sans SemiBold", 28), bg='#41B77F', fg='white')
        label_title.grid(row=0, column=1)

        albert_sorel =(Image.open("images/sorel_refait.png"))
        resized_albert_sorel = albert_sorel.resize((110,110), Image.ANTIALIAS)
        self.albert_sorel=ImageTk.PhotoImage(resized_albert_sorel)
        logo_albert_sorel=Label(self.frame,image=self.albert_sorel, bg='#41B77F')

        option_sport=(Image.open("images/option_sport-removebg-preview.png"))
        resized_option_sport = option_sport.resize((110,110), Image.ANTIALIAS)
        self.option_sport=ImageTk.PhotoImage(resized_option_sport)
        logo_option_sport=Label(self.frame,image=self.option_sport,bg='#41B77F')

        jones=(Image.open("images/jones-removebg-preview.png"))
        resized_jones =jones.resize((110,110), Image.ANTIALIAS)
        self.jones=ImageTk.PhotoImage(resized_jones)
        logo_jones=Label(self.frame, image=self.jones, bg='#41B77F')



        label_subtitle = Label(self.frame, text="\nFait par le Lycée Albert Sorel  \n", #create_subtitle :
        font=("Courrier", 20), bg='#41B77F', fg='white')
        label_subtitle.grid(column=1,row=2)

        normandie= (Image.open("images/normandie.png"))
        resized_normandie= normandie.resize((200,85), Image.ANTIALIAS)
        self.new_normandie= ImageTk.PhotoImage(resized_normandie)
        logo_normandie=Label(self.frame,image=self.new_normandie,bg='#41B77F')

        paris2024= (Image.open("images/paris2024.png"))
        resized_paris= paris2024.resize((200,160), Image.ANTIALIAS)
        self.new_paris= ImageTk.PhotoImage(resized_paris)
        logo_paris=Label(self.frame,image=self.new_paris,bg='#41B77F')

        unss= (Image.open("images/unss.png"))
        resized_unss= unss.resize((110,60), Image.ANTIALIAS)
        self.new_unss= ImageTk.PhotoImage(resized_unss)
        logo_unss=Label(self.frame,image=self.new_unss,bg='#41B77F')



        source_btn = Button(self.frame,text='Code Source', command=self.source,width=10, font=("Open Sans SemiBold", 12), bg='white', fg='#41B77F')

        calc_button = Button(self.frame, text="Calculez maintenant !", font=("Open Sans SemiBold", 26), bg='white', fg='#41B77F',#create_calculate_button
        command=lambda:[label_subtitle.grid_forget(),label_title.grid_forget(),calc_button.grid_forget(),logo_paris.grid_forget(),logo_normandie.grid_forget(),logo_unss.grid_forget(),source_btn.grid_forget(),logo_jones.grid_forget(),logo_albert_sorel.grid_forget(),logo_option_sport.grid_forget(), label_nom.grid_forget(),self.people_nbr()])#,self.back.pack()

        label_nom = Label(self.frame, text="\nFait par : Baptiste Dudonné, Cyprien Duroy, Arthur Lecomte du Lycée Albert Sorel  ", #create_subtitle :
        font=("Courrier", 16), bg='#41B77F', fg='white')

        logo_albert_sorel.grid(column=0, row=1,ipadx=4)
        logo_option_sport.grid(column=1, row=1)
        logo_paris.grid(column=2, row=1)
        calc_button.grid(column=1,row=3)
        logo_normandie.grid(column=1,row=4)
        logo_unss.grid(column=2,row=4)
        logo_jones.grid(column=0,row=4,ipadx=4)

        source_btn.grid(column=1,row=5)
        label_nom.grid(column=1,row=6)

    """///////////////////////////////////////////////// Number Of Peoples ://////////////////////////////////////////////////////////////////////:"""

    def people_nbr(self):
        home= (Image.open("images/home.png"))
        resized_home= home.resize((45,45), Image.ANTIALIAS)
        self.new_home= ImageTk.PhotoImage(resized_home)
        logo_normandie=Label(self.frame,image=self.new_home,bg='#41B77F')

        self.back= Button(self.frame,image=self.new_home,bg='#41B77F', command=self.close) #lambda:[self.close(),self.create_fully_window])
        self.back.pack(side=TOP)

        """
        back=Button(self.frame,image=new_home)
        back =Button(self.frame,image=new_home,bg='#41B77F', fg='#41B77F')
        """

        label_subtitle = Label(self.frame, text="Combien Etes-vous ?\n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        #Pour actualiser L'entrée et la voir en direct
        def update_label(*args):
            var_retour.set(var_entry.get())
            self.nb=var_entry.get()

        def verify():
            if var_entry.get() > 0 :
                label_subtitle.pack_forget(),entry.pack_forget(),label_space.pack_forget(),confirm_btn.pack_forget(),self.number_methods()
            else :
                messagebox.showwarning("ERREUR","Entrez un nombre !")

        var_entry=IntVar(value="")
        var_entry.trace("w",update_label)
        entry=Entry(self.frame, textvariable=var_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 22))
        var_retour=IntVar()
        label_space=Label(self.frame,textvariable=var_retour,font=("Courrier", 20), bg='#41B77F',fg='white')
        #retour = Label(self.frame,textvariable=var_retour,font=("Courrier", 20), bg='#41B77F',fg='white')
        confirm_btn = Button(self.frame, text="Valider", font=("Courrier", 25), bg='white', fg='#41B77F',command=verify)
        #empaquetage


        #back.pack()
        label_subtitle.pack()
        entry.pack()
        label_space.pack()
        confirm_btn.pack()

    """////////////////////////////////////////////////////////////////// USE SEVERAL Stage ?////////////////////////////////////////////////////////"""

    def number_methods(self):
            label_subtitle = Label(self.frame, text="Y Aura-t'il Plusieurs Etapes ?\n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
            btn_1 =Button(self.frame,text="OUI",width=10,font=("Courrier", 18),bg='#41B77F', fg='white', command = lambda :[self.cbm_trans(),forget()])
            btn_2 = Button(self.frame, text="NON",width=10, font=("Courrier", 18), bg='#41B77F', fg='white',command=lambda:[self.start_location(),forget()])

            def forget():#to remove the widget
                label_subtitle.pack_forget(),btn_1.pack_forget(),btn_2.pack_forget()


            label_subtitle.pack()
            btn_2.pack(side=BOTTOM,padx=30,pady=10)
            btn_1.pack(side=BOTTOM,padx=30,pady=10)


    """/////////////////////////////////////////////////////////////////how many times change you methods of transport////////////////////////////////////////////////////////////////////////"""
    def cbm_trans(self):
        label_subtitle = Label(self.frame, text="Combien d'étapes allez-vous faire ? \n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        def verify():
            if var_entry.get() > 1 :
                self.nbr_etape = var_entry.get()-1
                label_subtitle.pack_forget(),entry.pack_forget(),label_space.pack_forget(),confirm_btn.pack_forget()
                self.start_location()
            else :
                messagebox.showwarning("ERREUR","Entrez un nombre supérieur à 1 !")

        var_entry=IntVar(value="")
        entry=Entry(self.frame, textvariable=var_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 22))
        label_space=Label(self.frame,text="\n",bg='#41B77F')
        confirm_btn = Button(self.frame, text="Valider", font=("Courrier", 25), bg='white', fg='#41B77F',command=verify)

        label_subtitle.pack()
        entry.pack()
        label_space.pack()
        confirm_btn.pack()



    """/////////////////////////////////////////////////////////////////////////////////////// ENTER DESTINATION AND START LOCATION ////////////////////////////////////////////////////////////////////////////////////"""

    def start_location(self):

        def verify_current():#in order to verify that an entry has been made

            if current_entry.get()!="":
                self.Current=current_entry.get()
                if self.nbr_etape==self.etape :
                    self.destination_location()
                elif self.nbr_etape>self.etape:
                    self.step_location()


        def forget():
            label_start.pack_forget(),current.pack_forget(),btn_confirm.pack_forget(),space.pack_forget()


        label_start=Label(self.frame, text="Entrez votre ville de départ :\n", font=("Courrier", 26), bg='#41B77F',fg='white')

        current_entry=StringVar()
        current=Entry(self.frame,textvariable=current_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 20))

        self.label_current=Label
        space=Label(self.frame,text="\n",bg='#41B77F')
        btn_confirm= Button(self.frame, text="Valider", font=("Courrier", 20), bg='white', fg='#41B77F',command = lambda :[verify_current(),forget()])

        label_start.pack()
        current.pack()
        space.pack()
        btn_confirm.pack()


    def step_location(self):

        if self.etape>=1:
            self.Current=self.Destination
        self.etape=self.etape+1
        def verify_step():#in order to verify that an entry has been made

                if step_entry.get()!="":
                    self.Destination=step_entry.get()
                    self.API()

        def forget():
                label_step.pack_forget(),step.pack_forget(),btn_confirm.pack_forget(),space.pack_forget(),self.label_current.pack_forget()

        label_step=Label(self.frame, text=f"Entrez votre étape {self.etape} : \n", font=("Courrier", 26), bg='#41B77F',fg='white')

        step_entry=StringVar()
        step=Entry(self.frame,textvariable=step_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 20))

        self.label_current=Label
        space=Label(self.frame,text="\n",bg='#41B77F')
        btn_confirm= Button(self.frame, text="Valider", font=("Courrier", 20), bg='white', fg='#41B77F',command = lambda :[verify_step(),forget()])

        label_step.pack()
        step.pack()
        space.pack()
        btn_confirm.pack()


    def destination_location(self):
        if self.etape>=1:
            self.Current=self.Destination
        self.etape=self.etape+1
        def city():#To Define the Destination City

            if self.valeur_buttton.get()==1:
                self.Destination="Caen"#Pont-l'évèque(49.282793557255886, 0.18484314531409504)
                label_destination.pack_forget(),radio1.pack_forget(),
                radio2.pack_forget(),radio3.pack_forget(),radio4.pack_forget(), self.label_current.pack_forget()
                self.API()
            elif self.valeur_buttton.get()==2:
                self.Destination="Deauville"
                label_destination.pack_forget(),radio1.pack_forget(),
                radio2.pack_forget(),radio3.pack_forget(),radio4.pack_forget(), self.label_current.pack_forget()
                self.API()
            elif self.valeur_buttton.get()==3:
                self.Destination="Le Havre"
                label_destination.pack_forget(),radio1.pack_forget(),
                radio2.pack_forget(),radio3.pack_forget(),radio4.pack_forget(), self.label_current.pack_forget()
                self.API()
            elif self.valeur_buttton.get()==4:
                self.Destination="Rouen"
                label_destination.pack_forget(),radio1.pack_forget(),
                radio2.pack_forget(),radio3.pack_forget(),radio4.pack_forget(), self.label_current.pack_forget()
                self.API()
        label_destination=Label(self.frame,text="\nEntrez votre destination:\n", font=("Courrier", 26), bg='#41B77F',fg='white')

        self.valeur_buttton=IntVar()
        radio1 = Radiobutton(self.frame, text="Caen      ",command=city ,value=1,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio2= Radiobutton(self.frame, text="Deauville",command=city,  value=2,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio3=Radiobutton(self.frame, text="Le Havre",command=city , value=3,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio4=Radiobutton(self.frame, text="Rouen    ", command=city, value=4,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)

        self.label_current=Label(self.frame,text=f'Votre voyage commence de {self.Current}',font=("Courrier", 20), bg='#41B77F',fg='white')
        self.label_current.pack()
        label_destination.pack()
        radio1.pack()
        radio2.pack()
        radio3.pack()
        radio4.pack()

    """/////////////////////////////////////////////////////////////////////API WINDOW///////////////////////////////////////////////////////////////////////////////////////////"""

    def API(self):#to send te request

        stop="stops="+self.Destination+"|"+self.Current
        url="https://www.distance24.org/route.json?"+stop
        while True:
            try :
                r = requests.get(url)
                break
            except (ConnectionError, requests.exceptions.ConnectionError):
                messagebox.showwarning("ERREUR","Vérifiez Votre Connection Internet")
                break

        rep=r.json()
        self.km=rep['distance']
        self.label_current = Label(self.frame, text=f"La distance entre {self.Current} et {self.Destination} est de {self.km} Kilomètres", font=("Courrier", 20), bg='#41B77F', fg='white')
        self.label_current.pack()
        self.method_transport()

    """//////////////////////////////////////////////////////////////////////////////// Méthod of transport ////////////////////////////////////////////////////////////////////////////////////"""

    def method_transport(self):#in order to know the method of transport you will use
            label_title = Label(self.frame, text=" \nChoisissez une méthode de Transport:\n  ",font=("Courrier", 20), bg='#41B77F', fg='white')

            btn_1 =Button(self.frame,image=self.new_train,font=("Courrier", 18),bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_train(),forget()])

            btn_2 = Button(self.frame, image=self.new_bus, font=("Courrier", 18), bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_bus(),forget()])

            btn_3 = Button(self.frame, image=self.new_plane, font=("Courrier", 18), bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_plane(),forget()])

            def forget():#to remove the widget
                label_title.pack_forget(),btn_1.pack_forget(),btn_2.pack_forget(),btn_3.pack_forget(), self.label_current.pack_forget()
            label_title.pack()
            btn_1.pack(side=LEFT,padx=30,pady=10)
            btn_2.pack(side=RIGHT,padx=30,pady=10)
            btn_3.pack(side=BOTTOM,padx=30,pady=10)


    """///////////////////////////////////////////////////////////////////////////////////Calculate Carbon Footsprint///////////////////////////////////////////////////////////////////////////////"""

    def bilan_trans_train(self): # for train

        carb=self.nb*self.km*0.000016
        self.carb_trans=self.carb_trans+carb
        self.carb_trans=round(self.carb_trans,2)
        if self.nbr_etape==self.etape :
            self.destination_location()
        elif self.nbr_etape>self.etape :
            self.step_location()
        else :
            self.reveal()


    def bilan_trans_bus(self):#for bus-
        carb=self.nb*self.km*0.000068
        self.carb_trans=self.carb_trans+carb
        self.carb_trans=round(self.carb_trans,2)
        if self.nbr_etape==self.etape :
            self.destination_location()
        elif self.nbr_etape>self.etape :
            self.step_location()
        else :
            self.reveal()


    def bilan_trans_plane(self):#for plane
        print(self.etape)
        print(self.nbr_etape)
        carb_plane=self.nb*self.km*0.000187
        self.carb_trans=self.carb_trans+carb_plane
        self.carb_trans=round(self.carb_trans,2)
        if self.nbr_etape==self.etape :
            self.destination_location()
        elif self.nbr_etape>self.etape :
            self.step_location()
        else :
            self.reveal()


    """/////////////////////////////////////////////////////////////////////////////////////REVEAL//////////////////////////////////////////////////////////////////////////////"""



    def final_background(self):
        tree= (Image.open("images/tree.png"))
        resized_tree= tree.resize((160,120), Image.ANTIALIAS)
        self.new_tree= ImageTk.PhotoImage(resized_tree)
        tree=Label(self.frame,image=self.new_tree,bg='#41B77F')
        tree.pack(side=BOTTOM)

    def reveal(self):
        self.tree=self.carb_trans /2.5
        self.tree=ceil(self.tree)
        self.tree=int(self.tree)
        if self.tree>1:
            self.final_background()
            tree="Arbres"
        else:
            tree="Arbre"
            self.final_background()
        label_subtitle = Label(self.frame, text=f"Votre Empreinte Carbone est de {self.carb_trans}  Tonne de CO2\n\nPour ce voyage, vous devez replanter {self.tree} {tree}", font=("Courrier", 26), bg='#41B77F',fg='white')
        label_subtitle.pack()

    def close(self):
        self.window.destroy()
        frame = Carbon_Calculator_fr()



frame1 = home()
frame1.window.mainloop()



