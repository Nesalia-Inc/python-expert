


class Range:
    def __init__(self, start: int, end: int, step : int = 1) -> None:
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.end or self.current < self.start:
            raise StopIteration
        else:
            current = self.current
            self.current += self.step
            return current


for number in Range(1, 5):
    print(number)  


iterator = iter(Range(1, 5))
print(next(iterator))  
print(next(iterator))  
print(next(iterator))  
