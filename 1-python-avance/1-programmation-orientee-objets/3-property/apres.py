


class Personnage:
    def __init__(self, nom: str, vie: int, attaque: int) -> None:
        self.__nom = nom
        self.__vie = vie
        self.__attaque = attaque
        
    
    # Quand on veut définir une nouvelle propriété, 
    # on va utiliser le décorateur `@property` et c'est tout !
    # Concernant l'implémentation, rien ne change. 
    @property
    def nom(self) -> str:
        
        # Ici, on retourne l'attribut `__nom`, 
        # il faut faire attention à ne pas 
        # retourner `nom` puisque ça va automatiquement
        # appeler la propriété et faire une boucle infinie...
        return self.__nom
    
    
    @property
    def vie(self) -> int:
        return self.__vie

    # Quand on veut avoir la possibilité de modifier une propriété
    # on va définir ce qu'on appelle son setter avec 
    # la syntaxe `@nom_property.setter`. L'implémentation reste
    # la même qu'avant. 
    @vie.setter
    def vie(self, valeur: int) -> None:
        if valeur < 0:
            self.__vie = 0
        elif valeur > 100:
            self.__vie = 100
        else:
            self.__vie = valeur
    
    @property
    def attaque(self) -> int:
        return self.__attaque

    @attaque.setter
    def attaque(self, valeur: int) -> None:
        if valeur < 0:
            raise ValueError("L'attaque ne peut pas être négative")
        
        self.__attaque = valeur
    
    def __str__(self) -> str:
        return f"Personnage(nom={self.nom}, vie={self.vie}, attaque={self.attaque})"



if __name__ == "__main__":
    joueur = Personnage(nom="Chevalier", vie=120, attaque=15)
    ennemi = Personnage(nom="Goblin", vie=100, attaque=20)

    print(joueur)
    print(ennemi)


    # Désormais, il est complètement possible de définir 
    # la valeur de la vie du joueur avec une syntaxe d'attribut
    # c'est beaucoup plus propre puisqu'on a pas besoin d'avoir 
    # une syntaxe d'appel de fonction. 
    joueur.vie = 80
    
    # On peut aussi modifier avec des `-=, +=, /=, ...`. 
    # La propriété se charge de faire le travail en interne 
    # pour que ça fonctionne. 
    joueur.attaque += 5
    
    
    # Comme la propriété reste une fonction qui possède sa propre logique
    # elle peut nous renvoyer des erreurs (c'est incroyable). Ca veut donc 
    # dire qu'une erreur en renvoyée quand l'attaque du joueur est < 0. 
    try:
        joueur.attaque = -5  
    except ValueError as e:
        print(e)  

    print(joueur)  
