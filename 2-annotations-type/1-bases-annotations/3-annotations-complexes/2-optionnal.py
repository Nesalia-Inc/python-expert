from typing import Optional




def afficher(logs : list[str], separateur : Optional[str] = None) -> None:
    if separateur is None:
        separateur = "\n"
        
    for log in logs:
        print(log, end=separateur) 
        
        
        
afficher([
    "Erreur1",
    "Avertissement",
    "Informations"
])