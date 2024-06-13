



def somme(*nombres : int) -> int:
    resultat = 0 
    
    for nombre in nombres:
        resultat += nombre 
        
    return resultat



def afficher(**kwargs : str | int) -> None:
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
        
        
if __name__ == '__main__':
    print(somme(1, 2, 3, 4, 5))
    afficher(prenom="Jean", nom="Doe", age=45)