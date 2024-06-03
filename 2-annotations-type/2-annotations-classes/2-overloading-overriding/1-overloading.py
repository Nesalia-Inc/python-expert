from typing import overload



@overload
def afficher(valeur : int) -> None: ...
@overload
def afficher(valeur : list[int]) -> None: ... 




def afficher(valeur : int | list[int]) -> None:
    match valeur:
        case int():
            print("Voici ma valeur", valeur)
        case list():
            for element in valeur:
                print("Voici ma valeur", element)
        case _:
            raise ValueError
        
        
        
afficher([1, 2, 3, 4, 5])