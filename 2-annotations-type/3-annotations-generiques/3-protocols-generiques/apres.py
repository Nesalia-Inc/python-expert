from dataclasses import dataclass, field
from typing import TypeVar, Protocol


T = TypeVar("T", contravariant=True)


class Comparable(Protocol[T]):
    def compare(self, other : T) -> int: ...
    
    
    

@dataclass
class Entity:
    vie : int 
    attaque : int 
    defense : int
    
    
    
@dataclass
class Joueur(Entity):
    competences : list[str] = field(default_factory=list)
    
    
    
class Monstres(Comparable[Joueur]):
    def __init__(self) -> None:
        self.monstres : list[Entity] = []
        
        
        
    def compare(self, other: Joueur) -> int:
        pass