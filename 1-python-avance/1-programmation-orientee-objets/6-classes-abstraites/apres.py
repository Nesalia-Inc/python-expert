from abc import ABC, abstractmethod



class Animal(ABC):
    def __init__(self, nom : str, age : int, taille : int) -> None:
        self.nom = nom 
        self.age = age 
        self.taille = taille 
        
        
    @abstractmethod
    def bruit(self) -> str: 
        pass 
    
    
    def vieillir(self) -> None:
        self.age += 1 
        
        
        
class Chien(Animal):
    def bruit(self) -> str:
        return "Woof"
    
    
class Chat(Animal):
    def bruit(self) -> str:
        return "Miaou"
    
    
    
if __name__ == '__main__':
    chien = Chien("Medor", 4, 85)
    
    print(chien.bruit())
    
    chat = Chat("Garfield", 12, 40)
    chat.vieillir()
    print(chat.age)