

class Personnage:
    def __init__(self, nom : str, vie : int, attaque : int) -> None:
        self.nom = nom 
        self._vie = vie 
        self._attaque = attaque 
        
        
    def get_vie(self) -> int:
        return self._vie
    
    def get_attaque(self) -> int:
        return self._attaque
    
    
    def set_vie(self, valeur : int) -> None:
        if valeur < 0:
            self._vie = 0
        elif valeur > 100:
            self._vie = 100
        else:
            self._vie = valeur
            
    def set_attaque(self, valeur : int) -> None:
        if valeur < 0:
            raise ValueError("L'attaque ne peut pas être négative")
        self._attaque = valeur
        
        
    def __str__(self) -> str:
        return f"Personnage(nom={self.nom}, vie={self.get_vie()}, attaque={self.get_attaque()})"



if __name__ == "__main__":
    joueur = Personnage(nom="Chevalier", vie=120, attaque=15)
    ennemi = Personnage(nom="Goblin", vie=100, attaque=20)

    print(joueur)
    print(ennemi)


    joueur.set_vie(80)
    try:
        joueur.set_attaque(-5) 
    except ValueError as e:
        print(e)  

    print(joueur)  