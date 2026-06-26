
class myRange:
    def __init__(self, start, end, increment_step):
        self.start = start
        self.end = end
        self.increment_step = increment_step

    def __iter__(self):
        return MyRangeIterator(self)
    
class MyRangeIterator:
    def __init__(self, obj):
        self.start = obj.start
        self.end = obj.end
        self.increment_step = obj.increment_step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < self.end:
            x = self.start
            self.start += self.increment_step
            return x
        else:
            raise StopIteration
        
range = myRange(1, 10, 2)
range_iter = iter(range)

for num in range_iter:
    print(num)