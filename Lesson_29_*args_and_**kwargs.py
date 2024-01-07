#Lesson:29 - *args and **kwargs
'''
In Python, *args and **kwargs are used to allow a function to accept a variable number of arguments.
These constructs are often used when you want to create flexible and generic functions that can handle
different input scenarios.

The *args syntax allows a function to accept any number of positional arguments. 
It collects these arguments into a tuple within the function.

In this example, *args collects all the positional arguments passed 
to the function into a tuple, and the function prints each argument.
''' 
def print_args(*args):
    for arg in args:
        print(arg)

# Example usage
print_args(1, 2, 3, 'four', 'five')



'''
**kwargs (Arbitrary Keyword Arguments):
The **kwargs syntax allows a function to accept any number of keyword arguments. 
It collects these arguments into a dictionary within the function.

In this example, **kwargs collects all the keyword arguments passed to the function
into a dictionary, and the function prints each key-value pair.


'''
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print_kwargs(name='John', age=25, city='New York')



#another example
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
        
person('aamir',age=35,city='dubai',phone=505481917)


'''
You can use both *args and **kwargs in the same function signature to create
a function that accepts both positional and keyword arguments.
'''
    
def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print_args_and_kwargs(1, 2, 3, name='John', age=25, city='New York')
    


