#Lesson:52 -  Generators
'''
Generators in Python are a way to create iterators in a more concise and memory-efficient manner. 
Instead of creating a full sequence in memory, generators allow you to iterate over elements one
at a time, producing values on-the-fly. They are defined using a special type of function called
a generator function.
Key features of generators:
> Lazy Evaluation: Values are generated and returned one at a time, as needed,
                   rather than creating an entire sequence in memory. 
                   This is known as lazy or on-the-fly evaluation.
                   
> yield Statement: Generator functions use the yield statement to produce a value
                   and temporarily suspend the function's state. The next time the
                   generator is called, it resumes execution from where it was paused.
                   
                   When the generator is iterated over using a for loop, it produces squares on-the-fly, 
                   and the state of the function is maintained between calls. 
                   
                   Generators are often more memory-efficient compared to creating a list or sequence 
                   explicitly, especially when dealing with large datasets. They are commonly used in 
                   scenarios where the entire sequence does not need to be stored in memory at once.  
                   
                   Another common use case for generators is processing data in a stream-like fashion, 
                   where items are generated and processed as they arrive, rather than waiting for the 
                   entire dataset to be available.                
'''


def topten():
    n = 1
    while n<=10:
        sq = n*n
        yield sq 
        n+=1

values = topten()

for i in values:
    print(i) 