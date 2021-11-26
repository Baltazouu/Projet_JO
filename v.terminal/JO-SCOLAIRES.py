# coding=utf-8>
"""
This is a terminal command line version without any graphical window
"""
import json
import requests
from math import*

class Empreinte_Carbone :
    def __init__ (self,nbre_personne):
        """constructeur """
        self.pays=""
        self.pers=nbre_personne
        self.trans=""
        self.E_C=0
        self.bilan_carb=0
        self.site=""
        self.NB_Jour=0
    #unité : CO2 par tonne

    def carb_avion (self, km): 
        """by cyprien
        calcul la pollution du transport aérienne pour un nbr de personne et de km
        https://www.greenly.earth/blog/empreinte-carbone-comparaison-avion-vs-voiture
        https://www.greenly.earth/blog/empreinte-carbone-comparatif-transports"""
        co2_avion= 0.000187 *self.pers*km
        return co2_avion


    def carb_bus (self,km):
        """by cyprien
        calcule le rejet co2 du bus suivant le nbr de personne et de km"""
        co2_bus=0.000068*self.pers*km
        return co2_bus

    def carb_train (self,km):
        """by cyprien
        calcule le rejet co2 du train suivant le nbr de personne et de km"""
        co2_train =0.000016*self.pers*km
        return co2_train

    def bilan_carb_trans(self):
        """by cyprien
        calcule le rejet co2 du transport"""
        nbr_km =self.Api() #calcul du nbr de km par l'api
        continuer = True #vérifie que c'est bien un chiffre
        while continuer ==True :
                    try :
                        self.trans=int(input("Wich Method Of Transport You Will Use:\nFor Plane : 1\nFor Bus : 2\nFor Train : 3\nEnter the number of your method of transport :"))
                        break
                    except ValueError :
                        print("Oops! That was no valid number. Type Number Between 1 and 3")

        self.trans=int(self.trans)
        if self.trans not in (1,2,3): #vérifie que ce chiffre est entre 1 et 3 
                    print ("Oops! That was no valid number. Type Number Between 1 and 3 :")
                    while continuer ==True :
                        try :
                            print("Wich Method Of Transport You Will Use\nFor Plane : 1\nFor Bus : 2\nFor Train : 3")
                            self.trans=int(input("Enter the number of your method of transport :"))
                            break
                        except ValueError :


                            print("Oops! That was no valid number. Type Number Between 1 and 3")
                    continuer = True
        else :
                if self.trans==1: #pour l'avion
                            self.bilan_carb=self.carb_avion(nbr_km) #renvoie à la def de calcul pour l'avion
                            continuer = False
                elif self.trans==3: #pour le train
                            self.bilan_carb=self.carb_train(nbr_km) #renvoie à la def de calcul pour le train
                            continuer = False
                elif self.trans ==2 : #pour le bus
                            self.bilan_carb=self.carb_bus(nbr_km) #renvoie à la def de calcul pour le bus
                            continuer = False
                

        print ("The carbon footprint is ", round(self.bilan_carb,2)) 
        return round(self.bilan_carb,2) #renvoie la bilan carbonne du transport


    def equivalent_carbone(self):
        """by rose
        Source CO2 desorbé: https://ecotree.green/combien-de-co2-absorbe-un-arbre
            Ce site nous apprend qu'arbre en une année consome environ 25kg de CO2.
            Source durée de vie: https://www.rustica.fr/arbres-et-arbustes/arbres-combien-temps-vont-ils-vivre,2003.html
                                 https://www.lovethegarden.com/fr-fr/article/jusqua-quel-age-vivent-les-arbres
            Un Arbre vit au moins 100ans

            Donc le calcul est simple: notre variable bilan_carb_trans (qui calcule le totale du CO2 en T)
            fois 1 arbre et le tous diviser par 2,5 T (qui est la tonne de CO2 absorbée dans un vie par un arbre):
            (bilan_carb_trans*1)/2,5=bilan_carb_trans/2,5 (uniter en nombre d'Arbre)"""
        self.E_C=(self.bilan_carb_trans()+self.carb_total_pers())/2.5 #calcul permettant de regrouper la def de calcul de la pollution du transport et celle de la pollution sur sites
        self.E_C=ceil(self.E_C)# on arrondie à la valeur supérieur
        return "It is therefore necessary to replant "+ str(self.E_C) + " trees" #retourne à l'utilisateur le nbr d'arbre à planter

    def Api(self):
        """Made By Arthur Lecomte & Baptiste Dudonné TG3 Nsi in Albert Sorel High School"""
        Dest=0
        Current=input("Enter Your Travel Start City :")                  #Pour Obtenir la ville de départ
        print("Enter Your Destination :\nFor Pont-l'évèque type 1\nFor Deauville type 2\nFor Le Havre type 3\nFor Rouen type 4")        #Which site u want to go?

        continuer = True
        while continuer:
        # gestion des erreurs on oblige que la valeur soit un entier et compris entre 1 et 4
                    while True:
                            try:
                                Destination = int(input("Enter Your Destination : "))
                                break
                            except ValueError:
                                print("Oops!  That was no valid number.  Try again...")


                    Destination=int(Destination)
                    if Destination not in (1,2,3,4):
                            print("Oops!  That was no valid number.  Type Number Between 1 and 5")
                            continuer = True
                    elif Destination==1:
                            Dest="Caen" #il n'y as pas pont l'évèque dans les sites"Pont-l'évèque(49.282793557255886, 0.18484314531409504)"
                            continuer=False
                    elif Destination==2:
                            Dest="Deauville"
                            continuer=False
                    elif Destination==3:
                            Dest="Le Havre"
                            continuer=False
                    elif Destination==4:
                            Dest="Rouen"
                            continuer=False

        self.site=Dest
        stop='stops='+Current+"|"+Dest
        url="https://www.distance24.org/route.json?"+stop # le lien que l'on va rechercher

        r = requests.get(url)# à l'aide du module requests on envoie une requete web
        rep=r.json()#on définit la requete au format json
        Km=rep['distance']#on récupère la valeur de distance dans la réponse en json
        print("The range between the two Points is ",Km,"Kilometers")

        return Km

    def carb_total_pers(self): #pollution de la personne sur place
        """made by esteban with help cyprien"""
        continuer = True #vérifie que le nbr de jour rentré est bien un chiffre
        while continuer==True :
                    try:
                        self.NB_Jour = int(input("Enter the number of days :"))
                        break
                    except ValueError :
                        print("Oops! Enter a valid number please!")
        co2 = 0.0008*self.pers*self.NB_Jour #calcul la pollution final du grp de personne sur le site
        print (round(co2,3))
        return round(co2,3)#retourne en tonnes par co2 pour etre convertie en arbre

C=Empreinte_Carbone(int(input("How many people are you ? :")))
print(C.equivalent_carbone())
