from typing import NamedTuple


class Point(NamedTuple):
    x : int
    y : int  

    def produit_scalaire(self, v : "Point") -> int:
        return (self.x * v.x) + (self.y * v.y) 

def produit_scalaire(u : Point, v : Point) -> int:
    return (u.x * v.x) + (u.y * v.y) 



if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(2, 3)
    
    print(produit_scalaire(p1, p2))
    print(p1.produit_scalaire(p2))