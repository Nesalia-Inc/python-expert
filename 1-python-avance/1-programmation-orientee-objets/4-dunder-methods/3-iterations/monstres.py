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
    
    
    for monstre in monstres:
        print("Vie :", monstre.vie, "Attaque :", monstre.attaque)