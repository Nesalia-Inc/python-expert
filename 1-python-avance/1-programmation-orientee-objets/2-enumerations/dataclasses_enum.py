from enum import Enum
from dataclasses import dataclass



@dataclass
class MonsterStats:
    life : int 
    attack : int 
    defense : int 
    
    
    
class Monster(MonsterStats, Enum):
    GOBLIN = 30, 5, 2
    TROLL = 100, 15, 10
    DRAGON = 300, 50, 30
    
    
    
if __name__ == "__main__":
    print(Monster.GOBLIN.value)
    print(Monster.TROLL.value)
    print(Monster.DRAGON.value)