from typing import TypeVar, Protocol


T = TypeVar("T", contravariant=True)
G = TypeVar("G", covariant=True)

# `Protocol` est aussi une annotation de type générique
# qui peut être utilisée pour créer des protocols génériques. 
class Operation(Protocol[T, G]):
    def operation(self, elements : T) -> G: ...
    
    
    
class SommeEntiers(Operation[list[int], int]):
    def operation(self, elements : list[int]) -> int:
        return sum(elements)
    

class ConcatenerChaines(Operation[list[str], str]):
    def operation(self, elements : list[str]) -> str:
        return ''.join(elements)
    
    
    
    
if __name__ == '__main__':
    print(SommeEntiers().operation([1, 2, 3]))
    print(ConcatenerChaines().operation(["1", "2", "3"]))
    