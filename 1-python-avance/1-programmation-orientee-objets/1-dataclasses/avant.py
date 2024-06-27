import random
from typing import Final 


def generer_identifiant_session() -> int:
    MIN : Final[int] = 100_000
    MAX : Final[int] = 1_000_000
    
    return random.randint(MIN, MAX)


class Session:
    def __init__(self, *, temps : float) -> None:
        self.__identifiant = generer_identifiant_session()
        self.__temps = temps
        
    
    def get_identifiant(self) -> int:
        return self.__identifiant
    
    
    def get_temps(self) -> float:
        return self.__temps 
    
    
    
class Utilisateur:
    def __init__(self, nom : str, email : str, mot_de_passe : str) -> None:
        self.nom = nom 
        self.email = email 
        self.mot_de_passe = mot_de_passe
        
        self.roles = ["membre"]
        
        
    def __repr__(self) -> str:
        return f"Utilisateur({self.nom}, {self.email}, {self.mot_de_passe}, {self.roles})"
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Utilisateur):
            raise ValueError
        
        return (self.nom, self.email, self.mot_de_passe) == (value.nom, value.email, value.mot_de_passe)
        

    
    
    def connecter(self) -> None:
        session = Session(temps=30)
        print(f"Utilisateur connecté avec succès dans la session {session.get_identifiant()} !")
        
    
if __name__ == '__main__':
    utilisateur = Utilisateur("Jean", "jean@gmail.com", "1234")
    print(utilisateur)
    
    utilisateur.connecter()
    
    utilisateur2 = Utilisateur("Jean", "jean@gmail.com", "1234")
    utilisateur2.connecter()
    
    print(utilisateur == utilisateur2) # True