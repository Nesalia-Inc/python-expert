import re
from typing import Final, Optional


ID_SIZE : Final[int] = 4

# Quand on veut créer une exception personnalisée, on va créer une classe
# qui hérite d'une exception native. Cette exception va jouer le rôle d'exception
# globale dans le contexte de ne pas pouvoir connecter l'utilisateur 
# et sera héritée par des exceptions personnalisées qui donneront plus d'informations
# sur pourquoi on ne peut pas se connecter
class CouldNotConnectUserError(ValueError):
    pass 

# Chaque exception personnalisée à la possibilité de redéfinir le constructeur
# de sa classe mère. Chaque exception native possède un constructeur
# qui a comme seul paramètre un `message` qui est une chaîne de caractères.
class InvalidIDSizeError(CouldNotConnectUserError):
    def __init__(self, message : Optional[str] = None) -> None:
        if message is None:
            message = f"Le mot de passe doit faire {ID_SIZE} caractères"
        
        super().__init__(message)


class InvalidPasswordFormatError(CouldNotConnectUserError):
    def __init__(self, message : Optional[str] = None) -> None:
        if message is None:
            message = "Le mot de passe doit faire au moins 8 caractères avec une majuscule et un caractère spécial"
        
        super().__init__(message)




def check_identifiant(identifiant : str) -> bool:
    IS_SIZE_CORRECT = len(identifiant) == 4
    
    return IS_SIZE_CORRECT
    

def check_password(password : str) -> bool:
    # Vérifie qu'il y a +8 caractères, une majuscule et un caractère spécial
    REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    if not re.match(REGEX, password):
        return False 
    return True


def connecter(identifiant : str, password : str) -> None:
    
    # Quand on veut gérer des exceptions, on va regrouper le code
    # qui peut causer une erreur dans un bloc `try`. 
    try:
        erreurs : list[ValueError] = []
        if not check_identifiant(identifiant):
            erreurs.append(InvalidIDSizeError())
        
        if not check_password(password):
            erreurs.append(InvalidPasswordFormatError())
            
        if erreurs:
            
            # Il est possible de renvoyer des groupes d'exceptions. C'est très utile 
            # lorsque le code peut renvoyer plusieurs exceptions et qu'on veut toutes
            # les avoir renvoyées en même temps. Cette exception va prendre en premier
            # paramètre un message et comme second la liste des exceptions à renvoyer.
            raise ExceptionGroup("Une ou plusieurs erreurs sont arrivées", erreurs)
        
        
    # Si le code à l'intérieur du `try` renvoie une erreur, on va directement aller 
    # dans le bloc `except` qui va prendre en paramètre l'exception en question. 
    # Tu dois comprendre qu'un bloc `except` choisi l'erreur qu'il gère et ignore 
    # toutes les autres. Ici, si l'erreur renvoyée n'est pas un `ExceptionGroup`, 
    # le code va simplement renvoyer l'erreur. Si tu veux gérer l'entièreté des exceptions
    # dans un bloc `except`, tu dois lui mettre en paramètre `Exception` qui est la classe de
    # base pour les exceptions. 
    
    # Tu peux utiliser la syntaxe `Exception as name` pour définir un nom à cette exception
    # et l'utiliser comme une variable. `name` est bien sûr le nom que tu veux, ici on a choisi
    # `e` par convention. 
    except ExceptionGroup as e:
        error = CouldNotConnectUserError("Impossible de connecter l'utilisateur")
        
        # Il est possible de rajouter des notes à nos exceptions à l'aide de la méthode 
        # `add_note` qui prends en paramètre le message de la note. C'est utile quand on veut
        # donner des informations supplémentaires sur les causes de l'erreur.
        error.add_note("Cela est surement à cause d'un identifiant ou mot de passe invalide")
        
        # Si on rajoutes `from exception` à la fin d'un `raise` on va pouvoir créer
        # une chaîne d'exceptions où `exception` va être la cause directe de `error`. 
        # Ca nous permet donc de comprendre que `error` à été renvoyée à cause de `exception`. 
        # Dans ce code `exception` est la variable `e` c'est-à-dire notre groupe d'exceptions.  
        raise error from e
    else:
        print("Utilisateur connecté avec succès")




if __name__ == "__main__":
    connecter("124", "exemple@")