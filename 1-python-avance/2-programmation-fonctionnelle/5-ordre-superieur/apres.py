from functools import reduce
from typing import Callable



def mon_map(func : Callable[[int], int], seq : list[int]) -> list[int]:
    resultat : list[int] = []
    
    for element in seq:
        resultat.append(func(element))
        
    return resultat


def mon_filter(func : Callable[[int], int], seq : list[int]) -> list[int]:
    resultat = []
    
    for element in seq:
        if func(element):
            resultat.append(element)
            
    return resultat


def mon_reduce(func : Callable[[int, int], int], seq : list[int]) -> int:
    resultat = 0
    
    for element in seq:
        resultat = func(resultat, element)
        
    return resultat


def get_pairs(nombres : list[int]) -> list[int]:
    # Quand on veut récuper uniquement les éléments d'une séquence qui suivent une condition précise,
    # on peut utiliser la fonction native `filter`. Cette fonction prends en paramètre
    # une fonction et une séquence d'éléments. 
    
    # Elle va renvoyer un objet de type `filter` que l'on peut convertir en liste. 
    # Cette liste possèdera uniquement les éléments qui respectaient cette condition. 
    
    # Si l'on cherche à récupérer uniquement les éléments pairs d'une liste d'entiers, 
    # on va mettre en première paramètre une fonction lambda qui prends en paramètre 
    # un entier et vérifie qu'il est pair. Le second élément est notre liste de nombres
    # On renvoi une conversion en liste de notre objet `filter` et tout fonctionne parfaitement.
    
    return list(filter(lambda x: x % 2 == 0, nombres))


def get_impairs(nombres : list[int]) -> list[int]:
    # Comme tu peux le voir, avoir les nombres impairs est super simple et ne nous demande
    # pas d'avoir une grosse quantité de duplication comparé à l'utilisation de boucles.
    
    return list(filter(lambda x: x % 2 == 1, nombres))


def double(nombres : list[int]) -> list[int]:
    # Quand on veut appliquer une opération à tous les éléments d'une séquence
    # on peut utiliser la fonction native `map`. Cette fonction prends en paramètre
    # une fonction et une séquence d'éléments. 
    
    # Elle va renvoyer un objet de type `map` que l'on peut convertir en liste
    # qui sera la liste de tous les éléments avec cette opération qui est appliquée. 
    
    # Si l'on cherche à retourner une liste qui est le double de celle mise en paramètre,
    # on va devoir définir une fonction qui prends en paramètre un entier et renvoie son double.
    # Dans cet exemple, on va utiliser une fonction lambda. Le second paramètre sera donc notre liste.
    # On renvoi une conversion en liste de notre objet `map` et tout fonctionne parfaitement.
    
    return list(map(lambda x: x * 2, nombres))


def somme(nombres : list[int]) -> list[int]:
    # Le fonctionnement de `reduce` est différent et un peu plus complexe. 
    # Cette fonction va prendre en paramètre une autre fonction qui prends 
    # en paramètre deux éléments puis une séquence d'éléments. 
    
    # Quand on veut faire la somme avec la fonction reduce, elle
    # va faire ((((1 + 2) + 3) + 4) + 5). Elle est donc utilisée pour
    # récupérer un résultat précis d'une séquence d'éléments. 
    return reduce(lambda x, y : x + y, nombres) # type: ignore


if __name__ == '__main__':
    
    print(mon_reduce(lambda x, y : x + y, [1, 2, 3, 4, 5]))