from functools import partial


# La syntaxe avec la fonction interne est bien 
# mais elle nous prive de la syntaxe où les deux
# paramètres se trouvent dans la même fonction. 
def ajouter(a : int, b : int) -> int:
    return a + b 



if __name__ == '__main__':
    
    # C'est ici que les partials vont vraiment être utiles. 
    # On va pouvoir lui mettre en paramètre une fonction 
    # ainsi que la valeur de premier paramètre. Elle va nous
    # renvoyer un objet de type `Partial` que l'on pourra de 
    # nouveau appeler pour avoir le même résultat qu'avant.
    ajouter_3 = partial(ajouter, 3)
    
    print(ajouter_3(5))
    
    # Malgré tout, on peut appeler la fonction normalement
    # si on le souhaite. 
    print(ajouter(1, 2))