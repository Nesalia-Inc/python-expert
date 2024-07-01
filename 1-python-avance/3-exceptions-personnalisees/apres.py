

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
class InvalidIDError(CouldNotConnectUserError):
    def __init__(self, message : str, identifiant : int) -> None:
        super().__init__(message)
        self.identifiant = identifiant


class InvalidPasswordError(CouldNotConnectUserError):
    def __init__(self, message : str, mot_de_passe : str) -> None:
        super().__init__(message)
        self.mot_de_passe = mot_de_passe





def verifier_identifiant(identifiant : int) -> bool:
    return False

def verifier_mot_de_passe(mdp : str) -> bool:
    return False


def connecter(identifiant : int, mot_de_passe : str) -> None:
    
    # Quand on veut gérer des exceptions, on va regrouper le code
    # qui peut causer une erreur dans un bloc `try`. 
    try:
        erreurs : list[ValueError] = []
        if not verifier_identifiant(identifiant):
            erreurs.append(InvalidIDError("Identifiant invalide", identifiant))
        
        if not verifier_mot_de_passe(mot_de_passe):
            erreurs.append(InvalidPasswordError("Le mot de passe n'est pas correct", mot_de_passe))
            
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
    connecter(1234, "1234")