from typing import NamedTuple


# On crée un NamedTuple en faisant hériter une classe
# de `NamedTuple`. 
class Point(NamedTuple):
    
    # Chaque élément du tuple est défini ici comme dans 
    # une dataclasse ou un TypedDict. Chaque élément est 
    # automatiquement immuable et n'est accessible qu'en lecture.
    x : int 
    y : int
    
    # Il est possible de créer des méthodes dans un NamedTuple.
    def produit_scalaire(self, other : "Point") -> int:
        return (self.x * other.x) + (self.y * other.y) 
    
    
if __name__ == '__main__':
    coord = Point(1, 2)
    
    coord2 = (1, 2)
    
    print(coord, coord == coord2, coord.produit_scalaire(Point(2, 3)))