#Lesson:51 -  Iterator
'''
In Python, an iterator is an object that represents a stream of data and provides
a way to iterate over that data. Iterators are used to traverse sequences, 
such as lists, tuples, and strings, or to generate a sequence dynamically.
'''
nums = [2,5,7,3,4]

it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))

for i in nums:
    print(i)
    
    
class Topten:
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
        
values = Topten()

for i in values:
    print(i)
    
#another example of iterator for list of squares
class SquareIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration
        

squares = SquareIterator(limit=11)
print("Printing a list of iterators")
for square in squares:
    print(square)