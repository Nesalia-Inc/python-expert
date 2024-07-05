from typing import Optional



# Il y a certains cas où l'on veut qu'on paramètre soit considéré comme
# optionnel c'est-à-dire qu'il a une valeur par défaut de `None`. 
# Cette annotation est donc équivalent à un type | None. 
# Comme dans cette fonction, l'annotation de séparateur est `str | None`. 

# Il existe malgré tout une annotation générique pour définir qu'une valeur
# est optionnelle. Cette annotation est `Optional` et possède la syntaxe
# `Optional[type]`. 
def afficher(logs : list[str], separateur : Optional[str] = None) -> None:
    if separateur is None:
        separateur = "\n"
        
    for log in logs:
        print(log, end=separateur) 
        
        
        
afficher([
    "Erreur1",
    "Avertissement",
    "Informations"
])