from typing import Iterator


class Monstre:
    def __init__(self, vie : int, attaque : int) -> None:
        self.vie = vie 
        self.attaque = attaque 


class Monstres:
    def __init__(self) -> None:
        self.__monstres : list[Monstre] = []
        
    def append(self, monstre : Monstre) -> None:
        self.__monstres.append(monstre)
        
        
    def __iter__(self) -> Iterator[Monstre]:
        return iter(self.__monstres)
    

if __name__ == '__main__':
    monstres = Monstres()
    monstres.append(Monstre(100, 10))
    monstres.append(Monstre(50, 10))
    monstres.append(Monstre(100, 5))
    
    
    # Une fois cette méthode définie, tu peux directement itérer dans ton objet 
    # pour récupérer chaque élément de ton ensemble d'éléments. 
    for monstre in monstres:
        
        # Vu que la boucle est consciente que chaque élément est de type monstre, 
        # on peut directement récupérer les informations de cet élément. 
        print("Vie :", monstre.vie, "Attaque :", monstre.attaque)