from tkinter import*
from tkinter import  messagebox
from PIL import Image, ImageTk
import requests
import webbrowser
from math import*
import pyglet


##MADE BY CYPRIEN DUROY, ARTHUR LECOMTE, BAPTISTE DUDONNÉ TG3 ALBERT SOREL

class home:

    def __init__(self):
        self.window = Tk()
        self.window.title("Carbon Footsprint Calculator")
        #self.window.geometry("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))#("875x650")
        self.window.minsize(850, 650)
        self.window.geometry("1920x1080")
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

""" ! VERSION ENGLISCH ! """


class Carbon_Calculator_en:
    """Class seeking to calculate the carbon footprint of travelling to the JO Scolaire"""

    def __init__(self):
        """Constructor of the Carbon_Carculator_en class"""
        self.window = Tk()
        self.window.title("Carbon Footsprint Calculator")
        self.window.geometry("1920x1280")#("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.minsize(850, 650)
        self.window.config(background='#41B77F')
        self.valeur_buttton=IntVar()#valeur des btns pour le mode de transport; entier
        self.carb_trans=0 #bilan total du transport
        self.km=0 #nbr km
        self.nb=0#le nombre de personnes
        self.tree=0
        self.Destination=""
        self.Current=""
        self.nbr_etape=0 #nbr d'étape demandé
        self.etape=0 #nbr d'étape réalisé
        self.bug="No" #variable détectant les bug de l'Api
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
        """def linking to the github where the project is stored"""
        url="https://github.com/Baltazouu/Projet_JO"
        webbrowser.open_new_tab(url)

    def create_fully_window(self):
        """def for formatting in tkinter, and for the first page (homepage)"""

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



        label_subtitle = Label(self.frame, text="\nMade by albert sorel high school  \n", #create_subtitle :
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

        calc_button = Button(self.frame, text="Calculate now !", font=("Open Sans SemiBold", 26), bg='white', fg='#41B77F',#create_calculate_button
        command=lambda:[label_subtitle.grid_forget(),label_title.grid_forget(),calc_button.grid_forget(),logo_paris.grid_forget(),logo_normandie.grid_forget(),logo_unss.grid_forget(),source_btn.grid_forget(),logo_jones.grid_forget(),logo_albert_sorel.grid_forget(),logo_option_sport.grid_forget(), label_nom.grid_forget(),label_nom2.grid_forget(),self.people_nbr()])#,self.back.pack()

        label_nom = Label(self.frame, text="\nBy : Baptiste Dudonné, Cyprien Duroy and Arthur Lecomte",font=("Courrier", 16), bg='#41B77F', fg='white')
        label_nom2=Label(self.frame,text="From Albert Sorel High School",font=("Courrier", 16), bg='#41B77F', fg='white')
        

        logo_albert_sorel.grid(column=0, row=1,ipadx=4)
        logo_option_sport.grid(column=1, row=1)
        logo_paris.grid(column=2, row=1)
        calc_button.grid(column=1,row=3)
        logo_normandie.grid(column=1,row=4)
        logo_unss.grid(column=2,row=4)
        logo_jones.grid(column=0,row=4,ipadx=4)

        source_btn.grid(column=1,row=5)
        label_nom.grid(column=1,row=6)
        label_nom2.grid(column=1,row=7)


    """///////////////////////////////////////////////// Number Of Peoples ://////////////////////////////////////////////////////////////////////:"""

    def people_nbr(self):
        """def asking for the number of people making this journey"""
        home= (Image.open("images/home.png"))
        resized_home= home.resize((45,45), Image.ANTIALIAS)
        self.new_home= ImageTk.PhotoImage(resized_home)
        logo_normandie=Label(self.frame,image=self.new_home,bg='#41B77F')

        self.back= Button(self.frame,image=self.new_home,bg='#41B77F', command=self.close) #lambda:[self.close(),self.create_fully_window])
        self.back.pack(side=TOP)

        label_subtitle = Label(self.frame, text="How many people are you ?\n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        #Pour actualiser L'entrée et la voir en direct
        def update_label(*args):
            """def transforming the entered answer into an integer"""
            self.nb=int(var_entry.get())

        def verify():
            """def checking that the value entered is greater than 0, then deletes the current display and triggers the next def """
            value=int(var_entry.get())
            if value > 0 :
                label_subtitle.pack_forget(),entry.pack_forget(),label_space.pack_forget(),confirm_btn.pack_forget(),self.number_methods()
            else :
                messagebox.showwarning("ERROR","Please type a number !")

        def verify2(event):
            """def linking the enter key with the Enter button"""
            test_chiffre()

        def test_chiffre():
            """def testing whether the value entered is a number and not a word"""
            l=0
            test=var_entry.get()
            for x in test:
                if x not in "0123456789":
                    l+=1
            if l>0:
                messagebox.showwarning("ERROR","Error enter only numbers!")
            else :
                verify()

        var_entry=StringVar() or IntVar()
        var_entry.trace("w",update_label)

        entry=Entry(self.frame, textvariable=var_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 22))
        label_space=Label(self.frame,font=("Courrier", 20), bg='#41B77F',fg='white')
        confirm_btn = Button(self.frame, text="Confirm", font=("Courrier", 25), bg='white', fg='#41B77F',command=verify)
        #empaquetage
        self.window.bind('<Return>', verify2)

        #back.pack()
        label_subtitle.pack()
        entry.pack()
        label_space.pack()
        confirm_btn.pack()

    """////////////////////////////////////////////////////////////////// USE SEVERAL Stage ?////////////////////////////////////////////////////////"""

    def number_methods(self):
            """def asking if the person is taking steps or not"""
            label_subtitle = Label(self.frame, text="Do you use several stages ?\n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
            btn_1 =Button(self.frame,text="YES",width=10,font=("Courrier", 18),bg='#41B77F', fg='white', command = lambda :[self.cbm_trans(),forget()])
            btn_2 = Button(self.frame, text="NO",width=10, font=("Courrier", 18), bg='#41B77F', fg='white',command=lambda:[self.start_location(),forget()])

            def forget():#to remove the widget
                """def deleting the present display"""
                label_subtitle.pack_forget(),btn_1.pack_forget(),btn_2.pack_forget()

            def verify2(event):
                """def avoiding bugs with the enter key"""
                print()

            self.window.bind('<Return>',verify2)

            label_subtitle.pack()
            btn_2.pack(side=BOTTOM,padx=30,pady=10)
            btn_1.pack(side=BOTTOM,padx=30,pady=10)


    """/////////////////////////////////////////////////////////////////how many times change you methods of transport////////////////////////////////////////////////////////////////////////"""
    def cbm_trans(self):
        """def that is only activated if the person takes steps, and asking how many steps"""
        label_subtitle = Label(self.frame, text="How many stages do you use ? \n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        def verify():
            """def checking the entered answer"""
            value=int(var_entry.get())
            if value > 1 :
                self.nbr_etape = value-1
                label_subtitle.pack_forget(),entry.pack_forget(),label_space.pack_forget(),confirm_btn.pack_forget()
                self.start_location()
            else :
                messagebox.showwarning("ERROR","Please type a number higher than 1 !")

        def verify2(event):
            "def linking the Enter key to the Validate button"""
            test_chiffre()

        def test_chiffre():
            """def testing that the value entered is a number and not letters"""
            l=0
            test=str(var_entry.get())
            for x in test:
                if x not in "0123456789":
                    l+=1
            if l>0:
                messagebox.showwarning("ERROR","Error enter only numbers!")
            else :
                verify()

        var_entry=StringVar()or IntVar()
        entry=Entry(self.frame, textvariable=var_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 22))
        label_space=Label(self.frame,text="\n",bg='#41B77F')
        confirm_btn = Button(self.frame, text="Confirm", font=("Courrier", 25), bg='white', fg='#41B77F',command=test_chiffre)

        self.window.bind('<Return>', verify2)

        label_subtitle.pack()
        entry.pack()
        label_space.pack()
        confirm_btn.pack()



    """/////////////////////////////////////////////////////////////////////////////////////// ENTER DESTINATION AND START LOCATION ////////////////////////////////////////////////////////////////////////////////////"""

    def start_location(self):
        """def requesting the starting location"""

        def verify_current():#in order to verify that an entry has been made
            """def checking the entered answer"""

            if current_entry.get()!="":
                self.Current=current_entry.get()
                self.Current=self.Current.capitalize()
                if self.nbr_etape==self.etape :
                    self.destination_location()
                elif self.nbr_etape>self.etape:
                    self.step_location()


        def forget():
            """def deleting the present tkinter display"""
            label_start.pack_forget(),current.pack_forget(),btn_confirm.pack_forget(),space.pack_forget()

        def test_chiffre():
            """def testant si la valeur saisi est un chiffre"""
            l=0
            test=current_entry.get()
            for x in test:
                if x in "0123456789":
                    l+=1
            if l>0:
                messagebox.showwarning("ERROR","Please do not enter numbers!")
            else :
                forget()
                verify_current()

        def verify2(event):
            """def linking the Enter key with the functions activated by the Enter button"""
            test_chiffre()

        label_start=Label(self.frame, text="Enter your start location :\n", font=("Courrier", 26), bg='#41B77F',fg='white')

        current_entry=StringVar()
        current=Entry(self.frame,textvariable=current_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 20))

        space=Label(self.frame,text="\n",bg='#41B77F')
        btn_confirm= Button(self.frame, text="Confirm your start city", font=("Courrier", 20), bg='white', fg='#41B77F',command = test_chiffre)

        self.window.bind('<Return>', verify2)

        label_start.pack()
        current.pack()
        space.pack()
        btn_confirm.pack()


    def step_location(self):
        """def requesting the location of the steps"""

        if self.etape>=1 and self.bug=="No":
            self.Current=self.Destination
        self.etape=self.etape+1

        def verify_step():#in order to verify that an entry has been made
                """def verifying the entered answer"""

                if step_entry.get()!="":
                    self.Destination=step_entry.get()
                    self.Destination=self.Destination.capitalize()
                    self.API()

        def forget():
                """def deleting the current display"""
                self.bug="No"
                label_step.pack_forget(),step.pack_forget(),btn_confirm.pack_forget(),space.pack_forget()

        def test_chiffre():
            """def testant si la valeur saisi est un chiffre"""
            l=0
            test=step_entry.get()
            for x in test:
                if x in "0123456789":
                    l+=1
            if l>0:
                messagebox.showwarning("ERROR","Please do not enter numbers!")
            else :
                forget()
                verify_step()

        def verify3(event):
            """def linking the Enter key to the function of the Enter button"""
            test_chiffre()
        label_step=Label(self.frame, text=f"Enter your {self.etape} step location : \n", font=("Courrier", 26), bg='#41B77F',fg='white')

        step_entry=StringVar()
        step=Entry(self.frame,textvariable=step_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 20))

        space=Label(self.frame,text="\n",bg='#41B77F')
        btn_confirm= Button(self.frame, text="Confirm your step city", font=("Courrier", 20), bg='white', fg='#41B77F',command = test_chiffre)

        self.window.bind('<Return>', verify3)

        label_step.pack()
        step.pack()
        space.pack()
        btn_confirm.pack()


    def destination_location(self):
        """def requesting the final location between the 4 locations of the School OJ"""
        if self.etape>=1:
            self.Current=self.Destination
        self.etape=self.etape+1
        def city():#To Define the Destination City
            """def offering the 4 cities as 4 buttons"""

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
        label_destination=Label(self.frame,text="\nEnter your city destination:\n", font=("Courrier", 26), bg='#41B77F',fg='white')

        self.valeur_buttton=IntVar()
        radio1 = Radiobutton(self.frame, text="Caen      ",command=city ,value=1,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio2= Radiobutton(self.frame, text="Deauville",command=city,  value=2,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio3=Radiobutton(self.frame, text="Le Havre",command=city , value=3,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)
        radio4=Radiobutton(self.frame, text="Rouen    ", command=city, value=4,variable=self.valeur_buttton,bg='#41B77F', font=("Courrier", 18),borderwidth=0,highlightthickness=0)

        self.label_current=Label(self.frame,text=f'Your travel start from {self.Current}',font=("Courrier", 20), bg='#41B77F',fg='white')

        self.label_current.pack()
        label_destination.pack()
        radio1.pack()
        radio2.pack()
        radio3.pack()
        radio4.pack()

    """/////////////////////////////////////////////////////////////////////API WINDOW///////////////////////////////////////////////////////////////////////////////////////////"""

    def API(self):#to send te request
        """def formatting and searching for km via the Api and checking for any bugs in it"""

        stop="stops="+self.Destination+"|"+self.Current
        url="https://www.distance24.org/route.json?"+stop
        while True:
            try :
                r = requests.get(url)
                break
            except (ConnectionError, requests.exceptions.ConnectionError):
                messagebox.showwarning("ERROR","Please verify your internet connexion")
                break



        rep=r.json()
        self.km=rep['distance']

        if self.km==0:
            messagebox.showwarning("ERROR","An error occurred when entering the cities, please try again!")
            self.etape-=1
            if self.etape==0 :
                self.start_location()
            else :
                self.bug="Yes"
                self.step_location()
        else :
            self.bug="No"
            self.method_transport()

    """//////////////////////////////////////////////////////////////////////////////// Méthod of transport ////////////////////////////////////////////////////////////////////////////////////"""

    def method_transport(self):#in order to know the method of transport you will use
            """def asking for the means of transport for each journey, present only 3 methods of transport: train, bus, plane"""

            label_title = Label(self.frame, text=" \nPlease choose your method of transport:\n  ",font=("Courrier", 20), bg='#41B77F', fg='white')

            btn_1 =Button(self.frame,image=self.new_train,font=("Courrier", 18),bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_train(),forget()])

            btn_2 = Button(self.frame, image=self.new_bus, font=("Courrier", 18), bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_bus(),forget()])

            btn_3 = Button(self.frame, image=self.new_plane, font=("Courrier", 18), bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_plane(),forget()])

            def forget():#to remove the widget
                """def deleting the present tkinter display"""
                label_title.pack_forget(),btn_1.pack_forget(),btn_2.pack_forget(),btn_3.pack_forget(), label_distance.pack_forget()

            def verify2(event):
                """def deleting all bugs when pressing the Enter key"""
                print()

            self.window.bind('<Return>', verify2)
            label_distance = Label(self.frame, text=f"The distance between {self.Current} and {self.Destination} is {self.km} kilometres.", font=("Courrier", 20), bg='#41B77F', fg='white')
            label_distance.pack()
            label_title.pack()
            btn_1.pack(side=LEFT,padx=30,pady=10)
            btn_2.pack(side=RIGHT,padx=30,pady=10)
            btn_3.pack(side=BOTTOM,padx=30,pady=10)


    """///////////////////////////////////////////////////////////////////////////////////Calculate Carbon Footsprint///////////////////////////////////////////////////////////////////////////////"""

    def bilan_trans_train(self): # for train
        """def activated during a train journey, calculating the co2 emission of the train"""
        carb=self.nb*self.km*0.000016
        self.carb_trans=self.carb_trans+carb
        self.next()

    def bilan_trans_bus(self):#for bus-
        "def activated during a bus journey, calculating the co2 emission of the bus"""
        carb=self.nb*self.km*0.000068
        self.carb_trans=self.carb_trans+carb
        self.next()

    def bilan_trans_plane(self):#for plane
        """def activated during a flight, calculating the co2 emission of the flight"""
        carb_plane=self.nb*self.km*0.000187
        self.carb_trans=self.carb_trans+carb_plane
        self.next()

    def next(self):
        """def looking for what the script should do after calculating the last trip, whether there is still a trip or not"""
        self.carb_trans=round(self.carb_trans,2)
        if self.nbr_etape==self.etape :
            self.destination_location()
        elif self.nbr_etape>self.etape :
            self.step_location()
        else :
            self.reveal()


    """/////////////////////////////////////////////////////////////////////////////////////REVEAL//////////////////////////////////////////////////////////////////////////////"""



    def final_background(self):
        """def for tkinter display of images for the end page"""
        tree= (Image.open("images/tree.png"))
        resized_tree= tree.resize((160,120), Image.ANTIALIAS)
        self.new_tree= ImageTk.PhotoImage(resized_tree)
        tree=Label(self.frame,image=self.new_tree,bg='#41B77F')
        tree.pack(side=BOTTOM)

    def reveal(self):
        """def looking for the number of trees to replant and formatting the answer sentence (plural or not)"""
        if self.carb_trans>1:
            ton="tons"
        else :
            ton="ton"
        self.tree=self.carb_trans /2.5
        self.tree=ceil(self.tree)
        self.tree=int(self.tree)
        if self.tree>1:
            self.final_background()
            tree="trees"
        else:
            tree="tree"
            self.final_background()
        label_subtitle = Label(self.frame, text=f"Your carbon footsprint is {self.carb_trans}  {ton} of CO2\n\nfor this travel you should to replant {self.tree} {tree}\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        label_subtitle.pack()

    def close(self):
        """def closing the current window and reopening a new one serving to return to the home via the little house in the script"""
        self.window.destroy()
        frame = Carbon_Calculator_en()


""" ! VERSION FRANCAISE ! """


class Carbon_Calculator_fr:
    """Classe cherchant à calculer l'empreinte carbonne du transport lors du déplacement pour se rendre au JO Scolaire"""

    def __init__(self):
        """Constructeur de la classe Carbon_Carculator_fr"""
        self.window = Tk()
        self.window.title("Carbon Footsprint Calculator")
        self.window.geometry("1600x900")#("{0}x{1}+0+0".format(self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
        self.window.minsize(850, 650)
        self.window.config(background='#41B77F')
        self.valeur_buttton=IntVar()#valeur des btns pour le mode de transport; entier
        self.carb_trans=0 #bilan total du transport
        self.km=0 #nbr km
        self.nb=0#le nombre de personnes
        self.tree=0
        self.Destination=""
        self.Current=""
        self.nbr_etape=0 #nbr d'étape demandé
        self.etape=0 #nbr d'étape réalisé
        self.bug="Non" #variable détectant les bug de l'Api
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
        """def mettant en lien le github où est stocké le projet"""
        url="https://github.com/Baltazouu/Projet_JO"
        webbrowser.open_new_tab(url)

    def create_fully_window(self):
        """def pour la mise en forme en tkinter, et pour la premier page (page d'acceuil)"""

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



        label_subtitle = Label(self.frame, text="\nFait par le Lycée Albert Sorel.\n", #create_subtitle :
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
        command=lambda:[label_subtitle.grid_forget(),label_title.grid_forget(),calc_button.grid_forget(),logo_paris.grid_forget(),logo_normandie.grid_forget(),logo_unss.grid_forget(),source_btn.grid_forget(),logo_jones.grid_forget(),logo_albert_sorel.grid_forget(),logo_option_sport.grid_forget(), label_nom.grid_forget(),label_nom2.grid_forget(),self.people_nbr()])#,self.back.pack()

        label_nom = Label(self.frame, text="\nProjet fait par Baptiste Dudonné, Cyprien Duroy et Arthur Lecomte",font=("Courrier", 16), bg='#41B77F', fg='white')
        label_nom2=Label(self.frame,text=" de la spécialité NSI du Lycée Albert Sorel.",font=("Courrier", 16), bg='#41B77F', fg='white')
        logo_albert_sorel.grid(column=0, row=1,ipadx=4)
        logo_option_sport.grid(column=1, row=1)
        logo_paris.grid(column=2, row=1)
        calc_button.grid(column=1,row=3)
        logo_normandie.grid(column=1,row=4)
        logo_unss.grid(column=2,row=4)
        logo_jones.grid(column=0,row=4,ipadx=4)

        source_btn.grid(column=1,row=5)
        label_nom.grid(column=1,row=6)
        label_nom2.grid(column=1,row=7)

    """///////////////////////////////////////////////// Number Of Peoples ://////////////////////////////////////////////////////////////////////:"""


    def people_nbr(self):
        """def demandant le nombre de personne effectuant ce trajet"""
        home= (Image.open("images/home.png"))
        resized_home= home.resize((45,45), Image.ANTIALIAS)
        self.new_home= ImageTk.PhotoImage(resized_home)
        logo_normandie=Label(self.frame,image=self.new_home,bg='#41B77F')

        self.back= Button(self.frame,image=self.new_home,bg='#41B77F', command=self.close) #lambda:[self.close(),self.create_fully_window])
        self.back.pack(side=TOP)


        label_subtitle = Label(self.frame, text="Combien êtes-vous ?\n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        #Pour actualiser L'entrée et la voir en direct
        def update_label(*args):
            """def transformant la réponse saisi en un entier"""
            self.nb=int(var_entry.get())

        def verify():
            """def vérifiant que la valeur saisi est supérieur à 0, puis supprime l'affichage actuel et déclanche la def suivante """
            value=int(var_entry.get())
            if value > 0 :
                label_subtitle.pack_forget(),entry.pack_forget(),label_space.pack_forget(),confirm_btn.pack_forget(),self.number_methods()
            else :
                messagebox.showwarning("ERREUR","Entrez un nombre !")

        def verify2(event):
            """def mettant en lien la touche entrée avec le bouton Valider"""
            test_chiffre()

        def test_chiffre():
            """def testant si la valeur saisi est bien des chiffres et non un mot"""
            l=0
            test=var_entry.get()
            for x in test:
                if x not in "0123456789":
                    l+=1
            if l>0:
                messagebox.showwarning("ERREUR","Erreur entrez uniquement des nombres !")
            else :
                verify()

        var_entry=StringVar()or IntVar()
        var_entry.trace("w",update_label)

        entry=Entry(self.frame, textvariable=var_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 22))
        label_space=Label(self.frame,font=("Courrier", 20), bg='#41B77F',fg='white')
        confirm_btn = Button(self.frame, text="Valider", font=("Courrier", 25), bg='white', fg='#41B77F',command=test_chiffre)

        #empaquetage
        self.window.bind('<Return>', verify2)

        #back.pack()
        label_subtitle.pack()
        entry.pack()
        label_space.pack()
        confirm_btn.pack()


    """////////////////////////////////////////////////////////////////// USE SEVERAL Stage ?////////////////////////////////////////////////////////"""

    def number_methods(self):
            """def demandant si la personne fait des étapes ou non"""
            label_subtitle = Label(self.frame, text="Faîtes-vous plusieurs étapes ?\n", font=("Courrier", 26), bg='#41B77F',fg='white')
            btn_1 =Button(self.frame,text="OUI",width=10,font=("Courrier", 18),bg='#41B77F', fg='white', command = lambda :[self.cbm_trans(),forget()])
            btn_2 = Button(self.frame, text="NON",width=10, font=("Courrier", 18), bg='#41B77F', fg='white',command=lambda:[self.start_location(),forget()])

            def forget():#to remove the widget
                """def supprimant l'affichage présent"""
                label_subtitle.pack_forget(),btn_1.pack_forget(),btn_2.pack_forget()

            def verify2(event):
                """def evitant les bugs avec la touche entrée"""
                print()

            self.window.bind('<Return>',verify2)

            label_subtitle.pack()
            btn_2.pack(side=BOTTOM,padx=30,pady=10)
            btn_1.pack(side=BOTTOM,padx=30,pady=10)


    """/////////////////////////////////////////////////////////////////how many times change you methods of transport////////////////////////////////////////////////////////////////////////"""
    def cbm_trans(self):
        """def qui est activé uniquement si la personne fait des étapes, et demandant combien d'étapes"""
        label_subtitle = Label(self.frame, text="Combien d'étapes allez-vous faire ?\n\n", font=("Courrier", 26), bg='#41B77F',fg='white')
        def verify():
            """def vérifiant la réponse saisi"""
            resultat=int(var_entry.get())
            if resultat > 1 :
                self.nbr_etape = resultat-1
                label_subtitle.pack_forget(),entry.pack_forget(),label_space.pack_forget(),confirm_btn.pack_forget()
                self.start_location()
            else :
                messagebox.showwarning("ERREUR","Entrez un nombre supérieur à 1 !")

        def verify2(event):
            """def reliant la touche Entrée au bouton Valider"""
            test_chiffre()

        def test_chiffre():
            """def testant que la valeur saisi soit bien un chiffre et non des lettres"""
            l=0
            test=str(var_entry.get())
            for x in test:
                if x not in "0123456789":
                    l+=1
            if l>0:
                messagebox.showwarning("ERREUR","Erreur entrez uniquement des nombres !")
            else :
                verify()

        var_entry=StringVar()or IntVar()
        entry=Entry(self.frame, textvariable=var_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 22))
        label_space=Label(self.frame,text="\n",bg='#41B77F')
        confirm_btn = Button(self.frame, text="Valider", font=("Courrier", 25), bg='white', fg='#41B77F',command=test_chiffre)

        self.window.bind('<Return>', verify2)

        label_subtitle.pack()
        entry.pack()
        label_space.pack()
        confirm_btn.pack()



    """/////////////////////////////////////////////////////////////////////////////////////// ENTER DESTINATION AND START LOCATION ////////////////////////////////////////////////////////////////////////////////////"""

    def start_location(self):
        """def demandant la localisation de départ"""

        def verify_current():#in order to verify that an entry has been made
            """def vérifiant la réponse saisi"""

            if current_entry.get()!="":
                self.Current=current_entry.get()
                self.Current=self.Current.capitalize()
                if self.nbr_etape==self.etape :
                    self.destination_location()
                elif self.nbr_etape>self.etape:
                    self.step_location()


        def forget():
            """def supprimant l'affichage tkinter présent"""
            label_start.pack_forget(),current.pack_forget(),btn_confirm.pack_forget(),space.pack_forget()

        def test_chiffre():
            """def testant si la valeur saisi est un chiffre"""
            l=0
            test=current_entry.get()
            for x in test:
                if x in "0123456789":
                    l+=1
            if l>0:
                messagebox.showwarning("ERREUR","Erreur n'entrez pas des nombres !")
            else :
                forget()
                verify_current()


        def verify2(event):
            """def reliant la touche Entrée avec les fonctions activé par le bouton Valider"""
            test_chiffre()


        label_start=Label(self.frame, text="Entrez votre ville de départ :\n", font=("Courrier", 26), bg='#41B77F',fg='white')

        current_entry=StringVar()
        current=Entry(self.frame,textvariable=current_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 20))

        space=Label(self.frame,text="\n",bg='#41B77F')
        btn_confirm= Button(self.frame, text="Valider", font=("Courrier", 20), bg='white', fg='#41B77F',command = test_chiffre)

        self.window.bind('<Return>', verify2)

        label_start.pack()
        current.pack()
        space.pack()
        btn_confirm.pack()


    def step_location(self):
        """def demandant la localisation de l'étapes"""

        if self.etape>=1 and self.bug=="Non":
            self.Current=self.Destination
        self.etape=self.etape+1

        def verify_step():#in order to verify that an entry has been made
                """def verifiant la réponse saisi"""

                if step_entry.get()!="":
                    self.bug="Non"
                    self.Destination=step_entry.get()
                    self.Destination=self.Destination.capitalize()
                    self.API()

        def forget():
                """def supprimant l'affichage actuel"""
                label_step.pack_forget(),step.pack_forget(),btn_confirm.pack_forget(),space.pack_forget()

        def test_chiffre():
            """def testant si la valeur saisi est un chiffre"""
            l=0
            test=step_entry.get()
            for x in test:
                if x in "0123456789":
                    l+=1
            if l>0:
                messagebox.showwarning("ERREUR","Erreur n'entrez pas des nombres !")
            else :
                forget()
                verify_step()

        def verify3(event):
            """def reliant la touche Entrée au fonction du bouton Valider"""
            test_chiffre()
        label_step=Label(self.frame, text=f"Entrez votre étape {self.etape} :\n", font=("Courrier", 26), bg='#41B77F',fg='white')

        step_entry=StringVar()
        step=Entry(self.frame,textvariable=step_entry,bg="#eeeeee",border=0,borderwidth=0,font=("Courrier", 20))

        space=Label(self.frame,text="\n",bg='#41B77F')
        btn_confirm= Button(self.frame, text="Valider", font=("Courrier", 20), bg='white', fg='#41B77F',command = test_chiffre)

        self.window.bind('<Return>', verify3)

        label_step.pack()
        step.pack()
        space.pack()
        btn_confirm.pack()

    def destination_location(self):
        """def demandant la localisation final entre les 4 emplacements des JO Scolaire"""
        if self.etape>=1:
            self.Current=self.Destination
        self.etape=self.etape+1
        def city():#To Define the Destination City
            """def proposant les 4 villes sous forme de 4 boutons"""

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
        """def mettant en forme et effectuant la recherche de km via l'Api et vérifiant aucun bug de celle-ci"""

        stop="stops="+self.Destination+"|"+self.Current
        url="https://www.distance24.org/route.json?"+stop
        while True:
            try :
                r = requests.get(url)
                break
            except (ConnectionError, requests.exceptions.ConnectionError):
                messagebox.showwarning("ERREUR","Vérifiez votre connexion internet!")
                break

        rep=r.json()
        self.km=rep['distance']

        if self.km==0:
            messagebox.showwarning("ERREUR","Une erreur est survenu lors de la saisi des villes, veuillez recommencer !")
            self.etape-=1
            if self.etape==0 :
                self.start_location()
            else :
                self.bug="Oui"
                self.step_location()
        else :
            self.bug="Non"
            self.method_transport()

    """//////////////////////////////////////////////////////////////////////////////// Méthod of transport ////////////////////////////////////////////////////////////////////////////////////"""

    def method_transport(self):#in order to know the method of transport you will use
            """def demandant le moyen de transport pour chaque trajet, présent d'uniquement 3 méthodes de transport : train, bus, avion"""

            label_title = Label(self.frame, text=" \nChoisissez une méthode de transport:\n  ",font=("Courrier", 20), bg='#41B77F', fg='white')

            btn_1 =Button(self.frame,image=self.new_train,font=("Courrier", 18),bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_train(),forget()])

            btn_2 = Button(self.frame, image=self.new_bus, font=("Courrier", 18), bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_bus(),forget()])

            btn_3 = Button(self.frame, image=self.new_plane, font=("Courrier", 18), bg='#41B77F', fg='#41B77F',command=lambda:[self.bilan_trans_plane(),forget()])

            def forget():#to remove the widget
                """def supprimant l'affichage tkinter présent"""
                label_title.pack_forget(),btn_1.pack_forget(),btn_2.pack_forget(),btn_3.pack_forget(), label_distance.pack_forget()

            def verify2(event):
                """def supprimant tous bug lors de l'appuis sur la touche Entrée"""
                print()

            self.window.bind('<Return>', verify2)
            label_distance = Label (self.frame, text=f"La distance entre {self.Current} et {self.Destination} est de {self.km} kilomètres", font=("Courrier", 20), bg='#41B77F', fg='white')
            label_distance.pack()
            label_title.pack()
            btn_1.pack(side=LEFT,padx=30,pady=10)
            btn_2.pack(side=RIGHT,padx=30,pady=10)
            btn_3.pack(side=BOTTOM,padx=30,pady=10)

    """///////////////////////////////////////////////////////////////////////////////////Calculate Carbon Foots ;///////////////////////////////////////////////////////////////////////////////"""

    def bilan_trans_train(self): # for train
        """def s'activant lors d'un voyage en train, calculant l'émission co2 de celui-ci"""
        carb=self.nb*self.km*0.000016
        self.carb_trans=self.carb_trans+carb
        self.suite()


    def bilan_trans_bus(self):#for bus
        """def s'activant lors d'un voyage en bus, calculant l'émission co2 de ce dernier"""
        carb=self.nb*self.km*0.000068
        self.carb_trans=self.carb_trans+carb
        self.suite()


    def bilan_trans_plane(self):#for plane
        """def s'activant lors d'un voyage en avion, calculant l'émission co2 de ce dernier"""
        carb_plane=self.nb*self.km*0.000187
        self.carb_trans=self.carb_trans+carb_plane
        self.suite()

    def suite(self):
        """def recherchant que doit effectue le script après le calcul du dernier trajet, à savoir si il y a encore un trajet ou non"""
        self.carb_trans=round(self.carb_trans,2)
        if self.nbr_etape==self.etape :
            self.destination_location()
        elif self.nbr_etape>self.etape :
            self.step_location()
        else :
            self.reveal()


    """/////////////////////////////////////////////////////////////////////////////////////REVEAL//////////////////////////////////////////////////////////////////////////////"""



    def final_background(self):
        """def pour l'affichage tkinter des images pour la page de fin"""
        tree= (Image.open("images/tree.png"))
        resized_tree= tree.resize((160,120), Image.ANTIALIAS)
        self.new_tree= ImageTk.PhotoImage(resized_tree)
        tree=Label(self.frame,image=self.new_tree,bg='#41B77F')
        tree.pack(side=BOTTOM)

    def reveal(self):
        """def recherchant le nombre d'arbre à replanter et mettant en forme la phrase de réponse (pluriel ou non)"""
        if self.carb_trans>1:
            ton="tonnes"
        else :
            ton="tonne"
        self.tree=self.carb_trans /2.5
        self.tree=ceil(self.tree)
        self.tree=int(self.tree)
        if self.tree>1:
            self.final_background()
            tree="arbres"
        else:
            tree="arbre"
            self.final_background()
        label_subtitle = Label(self.frame, text=f"Votre empreinte carbone est de {self.carb_trans} {ton} de CO2\n\nPour ce voyage, vous devez replanter {self.tree} {tree}", font=("Courrier", 26), bg='#41B77F',fg='white')
        label_subtitle.pack()

    def close(self):
        """def fermant la fenetre actuelle et en réouvrant une nouvelle servant à revenir à l'acceuil via la petite maison dans le script"""
        self.window.destroy()
        frame = Carbon_Calculator_fr()



frame1 = home()
frame1.window.mainloop()