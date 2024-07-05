import re



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
    if not check_identifiant(identifiant) or not check_password(password):
        raise ValueError
    
    print("Utilisateur connecté avec Succès")
    
    
    
if __name__ == '__main__':
    connecter("123", "1234")

