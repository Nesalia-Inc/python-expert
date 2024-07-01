
# Quand on veut créer une classe abstraite, on va importer 
# depuis le module `abc` la classe `ABC` et le décorateur `abstractmethod`
from abc import ABC, abstractmethod


# Pour créer une classe abstraite, on va faire hériter une classe
# de `ABC`, c'est tout !
class Animal(ABC):
    
    # Une classe abstraite reste une classe, elle peut donc contenir 
    # des méthodes concrètes ainsi que des attributs. 
    def __init__(self, nom : str, age : int, taille : int) -> None:
        self.nom = nom 
        self.age = age 
        self.taille = taille 
        
        
    # Quand on veut créer une méthode abstraite, on va créer une méthode
    # qui est décorée par `@abstractmethod`. Une méthode abstraite ne possède pas
    # de documentation donc on lui mets uniquement `pass` 
    # ou alors `raise NotImplementedError`
    @abstractmethod
    def bruit(self) -> str: 
        pass 
    
    
    def vieillir(self) -> None:
        self.age += 1 
        
        
        
# On va faire hériter nos classes concrètes de la classe abstraite. 
# Ca va nous donner accès à toutes les méthodes concrètes de la classe mère
# mais on va être obligé d'implémenter l'entièreté des méthodes abstraites
class Chien(Animal):
    
    # Implémenter une méthode abstraite n'a rien de spécial, il suffit
    # de créer une méthode qui possède la même signature et de lui définir
    # une implémentation
    def bruit(self) -> str:
        return "Woof"
    
    
class Chat(Animal):
    def bruit(self) -> str:
        return "Miaou"
    
    
    
if __name__ == '__main__':
    
    # Comme tu peux le voir ici, le code fonctionne parfaitement 
    # sans avoir besoin d'un quelconque changement. Le code est donc
    # identique pour l'utilisateur mais est bien plus propre (et sans duplication)
    # pour le développeur.
    
    chien = Chien("Medor", 4, 85)
    
    print(chien.bruit())
    
    chat = Chat("Garfield", 12, 40)
    chat.vieillir()
    print(chat.age)