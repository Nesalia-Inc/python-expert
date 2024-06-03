


def afficher(n : int) -> None:
    if n <= 0:
        return 
    print(n)
    return afficher(n-1)


def somme(liste : list[int]) -> int:
    if len(liste) <= 0:
        return 0
    
    head, *tail = liste 
    return head + somme(tail)



if __name__ == '__main__':
    afficher(5)
    print(somme([1, 2, 3, 4, 5]))