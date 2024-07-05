from typing import final 



# Quand on ne veut pas qu'une classe soit héritée par
# une quelconque autre classe, on a la possibilité 
# d'utiliser le décorateur `@final`. Une fois 
# ajouté à la classe, il n'est plus possible 
# de l'hériter.

# @final
class Vehicule:
    def demarrer_moteur(self) -> None:
        print("Moteur démarré")
        
        
        
    # Dans un contexte similaire, si on ne veut pas
    # qu'une méthode puisse être redéfinie dans une 
    # classe fille, on a la possibilité d'utiliser
    # ce même décorateur pour bloquer ce comportement.
    @final
    def arreter_moteur(self) -> None:
        print("Moteur arrêté")
        
        
        
        
class Voiture(Vehicule):
    def demarrer_moteur(self) -> None:
        print("Moteur voiture allumé") 
        