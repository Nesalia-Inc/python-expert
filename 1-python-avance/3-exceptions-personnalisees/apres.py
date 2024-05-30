


class InvalidIDError(ValueError):
    def __init__(self, message : str, identifiant : int) -> None:
        super().__init__(message)
        self.identifiant = identifiant


class InvalidPasswordError(ValueError):
    def __init__(self, message : str, mot_de_passe : str) -> None:
        super().__init__(message)
        self.mot_de_passe = mot_de_passe


class CouldNotConnectUserError(ValueError):
    pass 


def verifier_identifiant(identifiant : int) -> bool:
    return False 

def verifier_mot_de_passe(mdp : str) -> bool:
    return False 


def connecter(identifiant : int, mot_de_passe : str) -> None:
    try:
        erreurs : list[ValueError] = []
        if not verifier_identifiant(identifiant):
            erreurs.append(InvalidIDError("Identifiant invalide", identifiant))
        
        if not verifier_mot_de_passe(mot_de_passe):
            erreurs.append(InvalidPasswordError("Le mot de passe n'est pas correct", mot_de_passe))
            
        if erreurs:
            raise ExceptionGroup("Une ou plusieurs erreurs sont arrivées", erreurs)
        
    except ExceptionGroup as e:
        error = CouldNotConnectUserError("Impossible de connecter l'utilisateur")
        error.add_note("Cela est surement à cause d'un identifiant ou mot de passe invalide")
        raise error from e
    else:
        print("Utilisateur connecté avec succès")




if __name__ == "__main__":
    connecter(1234, "1234")