


def afficher(n : int) -> None:
    for i in range(n):
        print(i)


def afficher_recursif(n : int) -> None:
    
    # Chaque fonction récursive doit avoir ce que l'on appelle
    # un "cas de base" qui est utilisé pour stocker les appels
    # successifs. Ici, on veut afficher les nombres de n à 0.
    # La condition pour que le code s'arrête est donc que `n`
    # soit inférieur ou égal à 0.
    if n <= 0:
        
        # Quand on retourne une valeur dans une fonction récursive,
        # on ne sort pas directement de la fonction. On retourne
        # à l'appel précédent. Ici, on va retourner à `afficher_recursif(1)`
        return 
    
    
    print(n)
    
    # C'est ici que tout fonctionne. Après avoir affiché la valeur, 
    # on va appeler cette même fonction avec la valeur `n-1`. 
    # La même logique va donc être executée encore et encore tant que
    # le cas de base n'est pas vrai. Une fois qu'il est vrai, on remonte 
    # tous les appels jusqu'à retourner au premier qui va sortir de la fonction.
    return afficher_recursif(n-1)



# Les algorithmes récursifs un peu plus poussés demandent un raisonnement
# approfondi. On cherche ici à faire la somme d'une liste d'entiers. Si
# l'on prends par exemple `[1, 2, 3, 4, 5]`, la somme est 1 + 2 + 3 + 4 + 5. 
# Donc, on a juste à créer une fonction qui récupère le premier élement d'une liste
# et appelle à nouveau cette fonction avec la même liste sans sa tête. On aurait donc
# `1 + fonction([2, 3, 4, 5]) + fonction([3, 4, 5]) + fonction([4, 5]) + fonction([5])`
# `1 + 2 + fonction([3, 4, 5]) + fonction([4, 5]) + fonction([5])`
# `1 + 2 + 3 + fonction([4, 5]) + fonction([5])`
# `1 + 2 + 3 + 4 + fonction([5])`
# `1 + 2 + 3 + 4 + 5`
def somme(liste : list[int]) -> int:
    
    # Si on récupère le premier élement d'une liste encore et encore
    # la condition pour que le code s'arrête est que cette fonction soit vide. 
    # Vu qu'on fait la somme, on doit renvoyer `0` qui sera la valeur de base
    # pour la somme.
    if len(liste) <= 0:
        return 0
    
    
    # Cette syntaxe est très simple mais aussi très efficace, `head`
    # représente le premier élement de la liste et `*tail` et l'ensemble
    # des éléments qu'il reste dans la liste (possiblement `[]`).
    head, *tail = liste 
    
    # On appelle de nouveau la fonction en faisant l'addition avec 
    # le premier élément de la liste.
    return head + somme(tail)



if __name__ == '__main__':
    afficher_recursif(5)
    print(somme([1, 2, 3, 4, 5]))