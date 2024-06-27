

class Personnage:
    def __init__(self, nom : str, vie : int, attaque : int) -> None:
        self.__nom = nom 
        self.__vie = vie 
        self.__attaque = attaque     
        
        
    def get_nom(self) -> str:
        return self.__nom
        
        
    def get_attaque(self) -> int:
        return self.__attaque
    
    def set_attaque(self, valeur : int) -> None:
        if valeur < 0:
            raise ValueError("L'attaque ne peut pas être négative")
        self.__attaque = valeur
        
        
    def get_vie(self) -> int:
        return self.__vie
    
    def set_vie(self, valeur : int) -> None:
        if valeur < 0:
            self.__vie = 0
        elif valeur > 100:
            self.__vie = 100
        else:
            self.__vie = valeur
        
        
    def __str__(self) -> str:
        return f"Personnage(nom={self.get_nom()}, vie={self.get_vie()}, attaque={self.get_attaque()})"



if __name__ == "__main__":
    joueur = Personnage(nom="Chevalier", vie=100, attaque=15)
    ennemi = Personnage(nom="Goblin", vie=100, attaque=20)

    print(joueur)
    print(ennemi)

    print(joueur.get_vie())

    joueur.set_vie(80)
    joueur.set_vie(5)
    joueur.set_vie(40)
    
    try:
        joueur.set_attaque(-5)
    except ValueError as e:
        print(e)  

    print(joueur)  