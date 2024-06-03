


couleur : tuple[int, int, int] = (124, 12, 0)



def creer_couleur(rouge : int, vert : int, bleu : int) -> tuple[int, int, int]:
    return (rouge, vert, bleu)


def afficher(couleur : tuple[int, int, int]) -> None:
    print(f"Rouge : {couleur[0]}, Vert : {couleur[1]}, Bleu : {couleur[2]}")
    
    
    
if __name__ == '__main__':
    couleur = creer_couleur(255, 12, 1)
    afficher(couleur)