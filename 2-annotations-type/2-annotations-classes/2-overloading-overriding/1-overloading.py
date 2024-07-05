from typing import overload



# On peut utiliser le concept d'overloading 
# pour régler ce problème. Ce concept nous
# permet de définir plusieurs signatures
# pour une même fonction. Ici, on a la signature
# dans le cas où la fonction prends en paramètre 
# un entier et la signature dans le cas où 
# il prends en paramètre une liste d'entiers. 

# Dans son fonctionnement, il suffit de créer
# un ensemble de fonctions sans implémentations
# avec les annotations que l'on veut et leur 
# ajouter le décorateur `@overload`. 
@overload
def doubler(valeur : int) -> int: ...
@overload
def doubler(valeur : list[int]) -> list[int]: ... 


# Supposons que l'on ait une fonction doubler 
# qui peut prendre en paramètre soit un entier
# soit une liste d'entiers. Elle retoure aussi
# un union entre un entier et une liste d'entiers.

# Il n'y a aucun soucis à implémenter cette fonction.
# Le problème vient de l'utilisation, on utilises un
# union de type. Le problème avec ça est que le type
# checker n'est pas conscient que la liste renvoie une 
# liste lorsque c'est le cas. 
def doubler(valeur : int | list[int]) -> int | list[int]:
    match valeur:
        case int():
            return valeur * 2
        case list():
            return [v * 2 for v in valeur]
        case _:
            raise ValueError
        
        

# Si on stocke le résultat de cette fonction dans une variable
# et que l'on essaye d'appeller une méthode de liste, on aura
# une erreur qui nous dit que le type est potentiellement un
# entier et que cette méthode n'est pas présente sur les entiers.   

# Une fois que l'overloading est ajouté, le type checker va être 
# conscient du raisonnement en fonction du type mis en paramètre 
# et ne vas plus nous renvoyer d'erreur. 
v = doubler([1, 2, 3, 4, 5])
v.append(2) 
