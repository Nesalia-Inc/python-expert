from typing import final 



class Vehicule:
    def demarrer_moteur(self) -> None:
        print("Moteur démarré")
        
        
    @final
    def arreter_moteur(self) -> None:
        print("Moteur arrêté")
        
        
        
        
class Voiture(Vehicule):
    def demarrer_moteur(self) -> None:
        print("Moteur voiture allumé") 
        
