




def produit_scalaire(u : tuple[int, int], v : tuple[int, int]) -> int:
    return (u[0] * v[0]) + (u[1] * v[1]) 



if __name__ == '__main__':
    p1 = (1, 2)
    p2 = (2, 3)

    print(produit_scalaire(p1, p2))