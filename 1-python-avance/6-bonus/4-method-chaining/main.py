from typing import Self


class Calculator:
    def __init__(self, value : int) -> None:
        self.__value = value
        
    
    def __str__(self) -> str:
        return str(self.value)
        
    @property
    def value(self) -> int:
        return self.__value
    
    
    def add(self, number : int) -> Self:
        self.__value += number
        return self
        
    def substract(self, number : int) -> Self:
        self.__value -= number
        return self
        
    def multiply(self, number : int) -> Self:
        self.__value *= number
        return self
        
    def divide(self, number : int) -> Self:
        self.__value //= number 
        return self
    
    
    
if __name__ == '__main__':
    c = Calculator(4)
    
    c.multiply(4).divide(2)
    
    print(c)