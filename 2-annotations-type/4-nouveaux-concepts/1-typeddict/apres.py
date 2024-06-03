from typing import TypedDict, NotRequired



class Personne(TypedDict):
    nom : str 
    age : int 
    taille : float 
    adresse : NotRequired[str] 
    
    
    
if __name__ == '__main__':
    personne : Personne = {
        "nom" : "Jean",
        "age" : 45,
        "taille" : 1.78
    }
    
    personne["moteur"] = "Diesel" # Wow 
    personne["age"] = 1.25
    
    print(personne)