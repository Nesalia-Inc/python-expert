from dataclasses import dataclass, field, KW_ONLY
import random 


def generer_identifiant_session() -> int:
    min = 100_000
    max = 1_000_000
    
    return random.randint(min, max)


@dataclass(frozen=True)
class Session:
    temps : int 
    identifiant : int = field(default_factory=generer_identifiant_session)



@dataclass
class Utilisateur:
    nom : str
    
    _ : KW_ONLY
    email : str 
    mot_de_passe : str 
    
    roles : list[str] = field(default_factory=list)
    

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
    
    
    
    
    
    
    
    