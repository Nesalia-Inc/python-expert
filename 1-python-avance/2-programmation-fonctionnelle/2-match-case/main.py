from enum import Enum


def get_couleur(couleur : str) -> tuple[int, int, int]:

    # Le match-case est une syntaxe alternative aux conditions 
    # qui est largement utilisé dans les langages fonctionnels. 
    # On va commencer avec un bloc `match` qui prends en paramètre 
    # une valeur quelconque. Ici, c'est notre couleur.
    match couleur:
        
        # On va ensuite suivre avec un ensemble de blocs `case` qui
        # vont prendre en paramètre une valeur. Le code va regarder si 
        # la valeur mise en paramètre du `match` correspond à la valeur
        # qui est mise en paramètre du `case`. Si c'est le cas, on rentre
        # dans le code de ce `case`. Sinon, on passe au suivant. 
        case "rouge": 
            return (255, 0, 0)
        case "vert":
            return (0, 255, 0)
        case "bleu":
            return (0, 0, 255)
        
        # Quand un `case` prends en paramètre `_`, il accèptera toutes les valeurs
        # qui ne se trouvaient pas dans les `case` précédents. 
        case _:
            raise ValueError("Couleur non supportée")
        
    # Ce code est équivalent au code suivant 
    # 
    # if couleur == "rouge":
    #     return (255, 0, 0)
    # elif couleur == "rouge":
    #     return (0, 255, 0)
    # elif couleur == "rouge":
    #     return (0, 0, 255)
    # else:
    #     raise ValueError("Couleur non supportée")
        
        
        
class Couleur(Enum):
    ROUGE = (255, 0, 0)
    VERT = (0, 255, 0)
    BLEU = (0, 0, 255)
    
    
def message_couleur(couleur : Couleur) -> str:

    # Quelque chose de très puissant avec le `match-case` 
    # est que l'on peut vérifier les valeurs d'une énumération
    # dans les `case`. Le vrai gros avantage est que si l'on oublie
    # une valeur, le code renverra une erreur. Ca veut donc dire que l'on 
    # est sûr de gérer tous les cas. 
    match couleur:
        case Couleur.ROUGE:
            return "Je suis la couleur rouge"
        case Couleur.VERT:
            return "Je suis la couleur verte"
        case Couleur.BLEU:
            return "Je suis la couleur bleue"




        
def somme(nombres : list[int]) -> int:
    
    # C'est dans ce genre de cas que les langages fonctionnels utilisent 
    # le plus souvent des `match-case`. On veut faire la somme d'une liste, 
    # on va donc faire un `match` avec la liste elle-même. Dans le cas où
    # cette liste est vide, on renvoie simplement `0`. Sinon, dans le cas
    # où l'on peut faire un `head, *tail` c'est-à-dire que la liste possède
    # au moins un élément et bien on va faire l'appel récursif. Si un tombe
    # sur un cas différent, un problème est arrivé et on renvoie une erreur.
    
    # C'est ici que l'on peut voir la grande différence entre les conditions
    # et la pattern-matching. Les conditions sont uniquement là pour vérifier 
    # une condition et c'est tout. Le pattern matching nous donne aussi la 
    # possibilité de définir des variables quand on regarde un cas précis 
    # comme on peut le voir dans le second `case`. 
    match nombres:
        case []:
            return 0
        case head, *tail:
            return head + somme(tail)
        case _:
            raise ValueError
        

if __name__ == '__main__':
    print(somme([1, 2, 3, 4, 5]))
    
    
    print(get_couleur("rouge"))