from math import*


circuit = input("saisie le nom du circuit: ")
voiture = input("saisie la voiture que tu as choisis: ")
conso_tour = input("saisie en litres ta consommation moyenne par tour: ")
plein = input("saisie en litres la capacité du plein du véhicule: ")
tps_tour = input("saisie maintenant ton temps moyen au tour en min: ")
tps_course = input("saisie le temps de la course en min: ")

class DONNEES:
    def __init__(self, nom_circuit : str, nom_voiture, valeur_conso_tour, valeur_plein, valeur_tps_tour, valeur_tps_course):
        self.nom_circuit = nom_circuit
        self.nom_voiture = nom_voiture
        self.valeur_conso_tour = valeur_conso_tour
        self.valeur_plein = valeur_plein
        self.valeur_tps_tour = valeur_tps_tour
        self.valeur_tps_course = valeur_tps_course
        valeur_nbr_tour = float(self.valeur_tps_course)/float(self.valeur_tps_tour)
        self.valeur_nbr_tour = str(valeur_nbr_tour)
        valeur_quantite_essence_course = float(self.valeur_nbr_tour)*float(self.valeur_conso_tour)
        self.valeur_quantite_essence_course = str(valeur_quantite_essence_course)
        valeur_nbr_tour_plein = float(self.valeur_plein)/float(self.valeur_conso_tour)
        self.valeur_nbr_tour_plein = valeur_nbr_tour_plein
     
                   
    def Calculer_stint(self):
        if float(self.valeur_nbr_tour) > float(self.valeur_nbr_tour_plein):

            valeur_nbr_stint = float(self.valeur_quantite_essence_course)/float(self.valeur_plein)
            valeur_nbr_stint = ceil(valeur_nbr_stint)
            self.valeur_nbr_stint = valeur_nbr_stint

            valeur_essence_stint = float(self.valeur_quantite_essence_course)/float(self.valeur_nbr_stint)
            self.valeur_essence_stint = valeur_essence_stint

        else:
            valeur_nbr_stint  = 0
            self.valeur_nbr_stint = valeur_nbr_stint

            valeur_essence_stint = 0
            self.valeur_essence_stint = valeur_essence_stint
        
        
    def Presenter_strat(self):
        course_sans_arret = ("le circuit ou tu vas rouler est " + self.nom_circuit + " avec la voiture "  + self.nom_voiture + "\nta conso au tour est de " + self.valeur_conso_tour + " litres, le maximum d'essence que tu puisses emporter est " + self.valeur_plein +  " litres" + "\nton temps moyen au tour est de " + self.valeur_tps_tour + " min, le temps de la course est de " + self.valeur_tps_course + " min\n\nsur la base des renseignements que tu nous a apporté, on peut calculer les données suivantes:\nle nombre de tours pour cette course sera de " + self.valeur_nbr_tour + "\nla quantité d'essence nécessaire pour la course sera de " + self.valeur_quantite_essence_course + " litres")

        if float(self.valeur_nbr_tour) > float(self.valeur_nbr_tour_plein):
            print(course_sans_arret + "\n\nle nombre d'arrêt pour cette course sera de " + str(self.valeur_nbr_stint) + "\nl'essence nécessaire par stint sera de " + str(self.valeur_essence_stint))
            
                            
        else:
            print(course_sans_arret) 
            

        
strat01 = DONNEES(circuit, voiture, conso_tour, plein, tps_tour, tps_course)
strat01.Calculer_stint()
strat01.Presenter_strat() 


