

class Chien:
    def __init__(self, nom : str, age : int, taille : int) -> None:
        self.nom = nom 
        self.age = age 
        self.taille = taille 
        
        
    def bruit(self) -> str:
        return "Woof"
    
    
    def vieillir(self) -> None:
        self.age += 1
        
        
        
class Chat:
    def __init__(self, nom : str, age : int, taille : int) -> None:
        self.nom = nom 
        self.age = age 
        self.taille = taille 
        
        
    def bruit(self) -> str:
        return "Miaou"
    
    
    def vieillir(self) -> None:
        self.age += 1
        
        
        
if __name__ == '__main__':
    chien = Chien("Medor", 4, 85)
    
    print(chien.bruit())
    
    chat = Chat("Garfield", 12, 40)
    chat.vieillir()
    print(chat.age)