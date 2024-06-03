


def somme(nombres : list[int]) -> int:
    match len(nombres):
        case 0:
            return 0
        case _:
            head, *tail = nombres 
            return head + somme(tail)
        
        

if __name__ == '__main__':
    print(somme([1, 2, 3, 4, 5]))