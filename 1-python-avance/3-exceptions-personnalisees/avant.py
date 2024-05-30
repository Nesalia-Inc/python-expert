

def check_identifiant(identifiant : int) -> bool:
    return False 

def check_password(password : str) -> bool:
    return False


def connecter(identifiant : int, password : str) -> None:
    if not check_identifiant(identifiant) or not check_password(password):
        raise ValueError
    
    print("Utilisateur connecté avec Succès")
    
    
    
if __name__ == '__main__':
    connecter(1234, "1234")