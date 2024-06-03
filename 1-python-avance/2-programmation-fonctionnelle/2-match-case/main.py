

def get_couleur(couleur : str) -> tuple[int, int, int]:
    match couleur:
        case "rouge": 
            return (255, 0, 0)
        case "vert":
            return (0, 255, 0)
        case "bleu":
            return (0, 0, 255)
        case _:
            raise ValueError("Couleur non supportée")



def somme(nombres : list[int]) -> int:
    match len(nombres):
        case 0:
            return 0
        case _:
            head, *tail = nombres 
            return head + somme(tail)
        
        

if __name__ == '__main__':
    print(somme([1, 2, 3, 4, 5]))
    
    
    print(get_couleur("rouge"))