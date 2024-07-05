


# Quand on veut annoter une fonction, on va pouvoir
# annoter deux choses : ses paramètres et sa valeur de retour. 
# La syntaxe pour annoter ses paramètres est la même que les
# variables. Concernant le type de retour, on va devoir suivre
# la syntaxe `-> type_retour`. 
def ajouter(a : int, b : int) -> int:
    
    # Une fois les annotations ajoutées, le type checker
    # est conscient de ces types. Il comprends donc que
    # les deux paramètres sont des entiers et te donnera
    # des erreurs si ton comportement avec ces paramètres
    # ne correspond pas à celui d'un entier. 
    
    # Si tu retournes une autre valeur qu'un entier, 
    # une erreur sera aussi affichée pour te dire que
    # tu ne suis pas le type que tu avais indiqué dans
    # la signature de la fonction
    return a + b 


# Une fonction qui ne possède de valeur de retour
# retourne malgré tout `None`. C'est pour ça que l'on 
# doit mettre en type de retour `None` quand une fonction 
# ne retourne rien.
def afficher(message : str) -> None:
    print("-----")
    print(message)
    print("-----")
    