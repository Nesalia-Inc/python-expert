from typing import TypeAlias


# Quand certaines annotations sont trop complexes,
# qu'elles peuvent être dupliquée ou qu'elles sont
# un contexte particulier, il est possible de créer
# ce qu'on appelle un Alias de Type. Un alias est 
# simplement une annotation de type stockée dans une
# variable.

# Par convention, on va mettre en majuscule la première
# lettre de la variable lorsque c'est un alias. Pour créer
# un alias, on va utiliser l'annotation `TypeAlias` et 
# mettre l'annotation en valeur de la variable. 
Couleur : TypeAlias = tuple[int, int, int]

Primitive : TypeAlias = int | str | float | bool


# Les alias peuvent être utilisés comme des annotations classiques
# Le type checker va automatiquement les considérer comme les types
# mis en valeur de l'alias. 
def ajouter(a : Primitive, b : Primitive) -> Primitive:
    return a + b #type: ignore


def creer_couleur(r : int, g : int, b : int) -> Couleur:
    return (r, g, b)