from typing import final, override



class Vehicule:
    def demarrer_moteur(self) -> None:
        print("Moteur démarré")
        
        
    @final
    def arreter_moteur(self) -> None:
        print("Moteur arrêté")
        
        
        
        
class Voiture(Vehicule):
    
    # Quand on veut définir explicitement qu'une méthode
    # est une redéfinition d'une méthode de la classe mère, 
    # on a la possibilité d'utiliser le décorateur `@override`.
    # Ce décorateur va renvoyer une erreur si la méthode n'est pas 
    # présente dans la classe mère et rend le code plus clair. 
    @override
    def demarrer_moteur(self) -> None:
        print("Moteur voiture allumé") 
        
