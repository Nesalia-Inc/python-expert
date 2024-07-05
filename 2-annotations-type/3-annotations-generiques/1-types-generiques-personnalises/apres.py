from typing import Generic, TypeVar


# Cette variable représente ce que l'on appelle une 
# variable de type. Globalement, elle représente un type
# quelconque. Elle est utilisée par le type checker pour
# la remplacer par un type concret. 
T = TypeVar("T")


# Quand on veut transformer une classe en type générique,
# on va utiliser l'annotation de type `Generic` qui est 
# elle aussi générique. Elle va prendre en paramètre une
# variable de type. 
class Pile(Generic[T]):
    
    # Concernant l'implémentation de la structure de données,
    # on doit comprendre que le type de ses éléments est désormais
    # `T`. Même si ça ne veut pas dire grand chose, ce type sera remplacé
    # par un type concret lors de la création d'un objet. 
    def __init__(self, *args: T) -> None:
        
        # Les éléments sont donc une liste de type `T`
        self.__elements: list[T] = list(args)
        
    # Quand on ajoute un nouvel élément dans une liste
    # de type `T`, cet élément est de type `T`. 
    def push(self, element: T) -> None:
        self.__elements.append(element)
        
    # Quand on retire un élément, on récupère un objet de type `T`
    def pop(self) -> T:
        if self.est_vide():
            raise ValueError("La pile est vide") 
        
        return self.__elements.pop()
    
    def est_vide(self) -> bool:
        return len(self.__elements) == 0
    
    
    
if __name__ == "__main__":
    
    # C'est là que la magie arrive. Désormais, dès qu'on crée une pile
    # avec des éléments de type concret dans son constructeur, il transforme
    # toutes les apparitions de `T` par ce type concret. Désormais, on ajoute
    # des entiers dans la pile et on retire des entiers de la pile. 
    pile = Pile(1, 2, 3)
    
    # Il n'est donc pas possible d'ajouter des éléments d'un type différent
    # dans le pile, une erreur est renvoyée.
    pile.push("4")
    
    # On peut aussi définir une pile vide avec une annotation générique pour définir
    # le type de ses éléments. 
    p2 : Pile[float] = Pile()
    
    
