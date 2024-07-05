from typing import TypedDict, NotRequired


# Pour créer un TypedDict, on va simplement créer une classe
# qui hérite de `TypedDict`. Quand on veut que l'ensemble des clés
# soient optionnelles, on peut rajouter juste après `TypeDict` : `total=False`.
# Ce qui donnerait `class Personne(TypedDict, total=False)`.
class Personne(TypedDict):
    
    # Chaque élément défini ci-dessous sera une clé avec 
    # le type de sa valeur. Chaque clé est une chaîne de 
    # caractères 
    nom : str 
    age : int 
    taille : float 
    
    # Quand on veut qu'uniquement une clé soit optionnelle
    # on peut utiliser l'annotation de type générique `NotRequired`.
    adresse : NotRequired[str] 
    
    # Il n'est pas possible de rajouter des méthodes dans un TypedDict
    # car ils sont uniquements utilisés pour donner des annotations complexes
    # à un dictionnaire. 
    
    
    
if __name__ == '__main__':
    
    # Quand on veut utiliser un TypedDict, on doit simplement
    # ajouter le type en annotation d'un dictionnaire. Le type checker
    # s'occupera automatiquement de vérifier si les clés sont correctes ou non.
    personne : Personne = {
        "nom" : "Jean",
        "age" : 45,
        "taille" : 1.78
    }
    
    # Il n'est pas possible de rajouter de nouvelles clés
    # dans un dictionnaire. Ca nous évite donc des erreurs bêtes.
    personne["moteur"] = "Diesel" # Wow 
    
    # Le type checker est désormais conscient du type de chaque élément 
    # et est capable de nous donner des erreurs si on se trompe.
    personne["age"] = 1.25
    
    print(personne)