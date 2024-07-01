from functools import reduce


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
    return reduce(lambda x, y : x + y, nombres) # type: ignore



print(somme([1, 2, 3, 4, 5]))