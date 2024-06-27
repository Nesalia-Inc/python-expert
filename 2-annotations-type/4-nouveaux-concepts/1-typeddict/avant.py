from typing import TypedDict, Required, NotRequired


class Personne(TypedDict):
    nom : str 
    age : Required[int] 
    taille : NotRequired[float]
    


if __name__ == '__main__':
    personne : Personne = {
        "nom" : "Jean",
        "age" : 45
    }
    

    
    
    print(personne)