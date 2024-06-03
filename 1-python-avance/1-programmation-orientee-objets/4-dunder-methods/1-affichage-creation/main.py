from typing import Self



class Monstre:
    def __new__(cls, vie : int, attaque : int) -> Self:
        return super().__new__(cls)
    
    def __init__(self, vie : int, attaque : int) -> None:
        self.vie = vie 
        self.attaque = attaque 
        
        
    def __str__(self) -> str:
        return "Je suis un monstre !"
    
    
    def __repr__(self) -> str:
        return f"Monstre(vie={self.vie}, attaque={self.attaque})"
    
    
    
    
if __name__ == "__main__":
    monstre = Monstre(100, 10)
    
    
    print(monstre)
    print(repr(monstre))
    