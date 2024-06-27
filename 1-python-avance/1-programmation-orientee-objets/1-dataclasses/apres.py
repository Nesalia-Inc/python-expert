from dataclasses import dataclass, field
import random
from typing import Final


def generer_identifiant_session() -> int:
    MIN : Final[int] = 100_000
    MAX : Final[int] = 1_000_000
    
    return random.randint(MIN, MAX)



# On transforme une classe en dataclass en utilisant
# le décorateur `@dataclass`. Ici, `frozen` veut qu'on 
# ne peut pas modifier les valeurs des attributs. 
# `kw_only` implique qu'on devra uniquement définir nos 
# attributs avec la syntaxe `Session(temps=...)`
@dataclass(frozen=True, kw_only=True)
class Session:
    
    # Comme tu peux le voir, une dataclasse ne possède pas de constructeur
    # On défini les attributs de chaque objet à l'aide de variables d'instances
    # La dataclasse va automatiquement les convertir en attributs
    temps : int 
    
    # `field` est une fonction spéciale qui permet de déterminer des comportements complexes
    # pour un attribut. Ici, `default_factory` nous permet d'appeler une fonction pour définir
    # la valeur par défaut de l'attribut. Le rôle de `init` est de définir si oui non l'attribut
    # sera mis en paramètre du constructeur. Ici, ce n'est pas le cas. 
    identifiant : int = field(default_factory=generer_identifiant_session, init=False)



# Les dataclasses redéfinissent en internes les méthodes
# `__str__` et `__eq__`, il n'est donc plus nécessaire de 
# les définir manuellement. 
@dataclass
class Utilisateur:
    """Classe de base pour représenter un utilisateur"""
    
    nom : str 
    email : str 
    password : str 
    
    roles : list[str] = field(default_factory=list, init=False)
    
    # Quand tu veux malgré tout avoir une, tu peux utiliser la dunder method
    # `__post_init__` qui est appelée au moment de la création de l'objet.
    def __post_init__(self) -> None:
        self.roles.append("membre")
    
    
    # Une dataclasse reste une classe, tu es donc complètement libre de rajouter
    # tes propres méthodes
    def connecter(self) -> None:
        session = Session(temps=30)
        print(f"Utilisateur connecté avec succès dans la session {session.identifiant} !")

    
    
    
if __name__ == '__main__':
    utilisateur = Utilisateur("Jean", "jean@gmail.com", "1234")
    print(utilisateur)
    
    utilisateur.connecter()
    
    utilisateur2 = Utilisateur("Jean", "jean@gmail.com", "1234")
    utilisateur2.connecter()
    
    print(utilisateur == utilisateur2) # True
    