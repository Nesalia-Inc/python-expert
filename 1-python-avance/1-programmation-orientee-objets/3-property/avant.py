

class Personnage:
    def __init__(self, nom : str, vie : int, attaque : int) -> None:
        self.nom = nom 
        self.__vie = vie 
        self.__attaque = attaque     
        
    @property
    def attaque(self) -> int:
        return self.__attaque
    
    @attaque.setter
    def attaque(self, valeur : int) -> None:
        if valeur < 0:
            raise ValueError("L'attaque ne peut pas être négative")
        self.__attaque = valeur
        
        
    @property 
    def vie(self) -> int:
        return self.__vie
    
    @vie.setter 
    def vie(self, valeur : int) -> None:
        if valeur < 0:
            self.__vie = 0
        elif valeur > 100:
            self.__vie = 100
        else:
            self.__vie = valeur
        
        
    def __str__(self) -> str:
        return f"Personnage(nom={self.nom}, vie={self.vie}, attaque={self.attaque})"



if __name__ == "__main__":
    joueur = Personnage(nom="Chevalier", vie=100, attaque=15)
    ennemi = Personnage(nom="Goblin", vie=100, attaque=20)

    print(joueur)
    print(ennemi)

    print(joueur.vie)

    joueur.vie = 80
    joueur.vie += 5
    joueur.vie -= 40
    
    try:
        joueur.attaque = -5
    except ValueError as e:
        print(e)  

    print(joueur)  