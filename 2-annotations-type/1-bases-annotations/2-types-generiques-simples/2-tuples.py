

# Un tuple est un type de données immuable où chaque élément 
# peut être d'un type différent. Ca veut donc dire que l'on va 
# devoir annoter chaque élément individuellemen. La syntaxe générale
# des annotations d'un tuple est : `tuple[type_elem_1, type_elem_2, ..., type_elem_N]`.  

couleur : tuple[int, int, int] = (124, 12, 0)

# Le type checker comprends quel est le type de chaque élément. 
rouge = couleur[0] 


# Quand on ne peut pas prédire la quantité d'éléments du tuple
# ou qu'il y a juste trop d'éléments, on va utiliser une syntaxe 
# alternative qui est `tuple[type, ...]` qui va simplement dire
# que le tuple possède un nombre non défini d'éléments de type `type`. 
nombres : tuple[int, ...] = (1, 2, 3, 4)



def creer_couleur(rouge : int, vert : int, bleu : int) -> tuple[int, int, int]:
    return (rouge, vert, bleu)


def afficher(couleur : tuple[int, int, int]) -> None:
    print(f"Rouge : {couleur[0]}, Vert : {couleur[1]}, Bleu : {couleur[2]}")
    
    
    
if __name__ == '__main__':
    couleur = creer_couleur(255, 12, 1)
    afficher(couleur)