from typing import Generic, TypeVar, Iterator

T = TypeVar("T")

class Pile(Generic[T], Iterator[T]):
    def __init__(self, *args: T) -> None:
        self.__elements: list[T] = list(args)
        
    def push(self, element: T) -> None:
        self.__elements.append(element)
        
    def pop(self) -> T:
        if self.est_vide():
            raise ValueError("La pile est vide") 
        
        return self.__elements.pop()
    
    def est_vide(self) -> bool:
        return len(self.__elements) == 0
    
    def __next__(self) -> T:
        if self.est_vide():
            raise StopIteration()
        
        return self.pop()
    
    
    
if __name__ == "__main__":
    pile = Pile(1, 2, 3)
    
    pile.push("4") # type: ignore
    
    for element in pile:
        print(element)
