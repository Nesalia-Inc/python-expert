from typing import final, override



class Vehicule:
    def demarrer_moteur(self) -> None:
        print("Moteur démarré")
        
        
    @final
    def arreter_moteur(self) -> None:
        print("Moteur arrêté")
        
        
        
        
class Voiture(Vehicule):
    @override
    def demarrer_moteur(self) -> None:
        print("Moteur voiture allumé") 
        
