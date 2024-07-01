from typing import Self



class Monstre:
    
    # La dunder method `__new__` est appelée lorsque l'on doit créer un objet
    # elle est donc appelée juste avant la méthode `__init__`. Son unique rôle 
    # est de créer l'objet mais elle peut aussi être utilisée pour rajouter des
    # comportements à cet objet, on peut par exemple l'utiliser pour un design pattern
    # appelé Singleton qui est utilisé lorsqu'on veut que tous les objets d'une classe
    # soient la même instance. Cette méthode doit retourner un objet de la classe (`Self`).  
    def __new__(cls, vie : int, attaque : int) -> Self:
        return super().__new__(cls)
    
    # La dunder method `__init__` est la première dunder que tu apprends, elle est appelée 
    # lors de la création de l'objet. Généralement, elle est utilisée pour charger 
    # tous les attributs de l'objet. 
    def __init__(self, vie : int, attaque : int) -> None:
        self.vie = vie 
        self.attaque = attaque 
        
        
    # La dunder method `__str__` est appelée lorsque qu'on 
    # cherche à `print` un objet de la classe ou alors qu'on 
    # essaye de convertir l'objet en chaîne de caractères avec 
    # la fonction `str()`. Elle est utile pour donner une représentation
    # sous forme de chaîne de caractères de notre objet.   
    def __str__(self) -> str:
        return "Je suis un monstre !"
    
    
    # La dunder method `__repr__` est très similaire à `__str__`.
    # Elle est appelée lorsqu'on fait `repr(objet)` mais elle est aussi
    # appelée lors d'un `print` si la dunder method `__str__` n'est pas définie. 
    def __repr__(self) -> str:
        return f"Monstre(vie={self.vie}, attaque={self.attaque})"
    
    
    
    
if __name__ == "__main__":
    monstre = Monstre(100, 10)
    
    
    print(monstre)
    print(repr(monstre))
