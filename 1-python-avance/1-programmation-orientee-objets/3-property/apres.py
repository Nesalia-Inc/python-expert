


class Personnage:
    def __init__(self, nom: str, vie: int, attaque: int) -> None:
        self.nom = nom
        self._vie = vie
        self._attaque = attaque
    
    @property
    def vie(self) -> int:
        return self._vie

    @vie.setter
    def vie(self, valeur: int) -> None:
        if valeur < 0:
            self._vie = 0
        elif valeur > 100:
            self._vie = 100
        else:
            self._vie = valeur
    
    @property
    def attaque(self) -> int:
        return self._attaque

    @attaque.setter
    def attaque(self, valeur: int) -> None:
        if valeur < 0:
            raise ValueError("L'attaque ne peut pas être négative")
        self._attaque = valeur
    
    def __str__(self) -> str:
        return f"Personnage(nom={self.nom}, vie={self.vie}, attaque={self.attaque})"



if __name__ == "__main__":
    joueur = Personnage(nom="Chevalier", vie=120, attaque=15)
    ennemi = Personnage(nom="Goblin", vie=100, attaque=20)

    print(joueur)
    print(ennemi)


    joueur.vie = 80
    try:
        joueur.attaque = -5  
    except ValueError as e:
        print(e)  

    print(joueur)  
