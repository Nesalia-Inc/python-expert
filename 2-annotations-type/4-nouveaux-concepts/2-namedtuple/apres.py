from typing import NamedTuple



class Point(NamedTuple):
    x : int 
    y : int
    
    
    def produit_scalaire(self, other : "Point") -> int:
        return (self.x * other.x) + (self.y * other.y) 
    
    
if __name__ == '__main__':
    coord = Point(1, 2)
    
    coord2 = (1, 2)
    
    print(coord, coord == coord2, coord.produit_scalaire(Point(2, 3)))