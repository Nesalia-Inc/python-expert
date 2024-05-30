import random 


def generer_identifiant_session() -> int:
    min = 100_000
    max = 1_000_000
    
    return random.randint(min, max)


class Session:
    def __init__(self, temps : float) -> None:
        self.__identifiant = generer_identifiant_session()
        self.__temps = temps
        
    @property
    def identifiant(self) -> int:
        return self.__identifiant
    
    @property
    def temps(self) -> float:
        return self.__temps 


class Utilisateur:
    def __init__(self, nom : str, *, email : str, mot_de_passe : str, roles : list[str]) -> None:
        self.nom = nom 
        self.email = email 
        self.mot_de_passe = mot_de_passe
        
        self.roles = roles
        
        
    def __repr__(self) -> str:
        return f"Utilisateur({self.nom}, {self.email}, {self.mot_de_passe}, {self.roles})"
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Utilisateur):
            raise ValueError
        
        return self.nom == value.nom \
               and self.email == value.email \
               and self.mot_de_passe == value.mot_de_passe \
               and self.roles == value.roles 
    
    
    def connecter(self) -> None:
        print("Utilisateur connecté avec succès !")
        
        
    
    
if __name__ == "__main__":
    u1 = Utilisateur("Jean", 
                     email="jean@gmail.com", 
                     mot_de_passe="jean1234", 
                     roles=["redacteur", "moderateur"]
                    )
    
    session = Session(30)
    u1.connecter()
    
    u2 = Utilisateur("Jean", 
                     email="jean@gmail.com", 
                     mot_de_passe="jean1234", 
                     roles=["redacteur", "moderateur"]
                    )
    
    session = Session(30)
    u2.connecter()
    
    if u1 == u2:
        print("Deux utilisateur identiques connectés actuellement !")