#Lesson:37 - inner functions and Decorators
'''
It’s possible to define functions inside other functions. Such functions are
called inner functions. Here’s an example of a function with two inner functions:
''' 

def div(a,b):
    print(a/b)
    
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)

#simple decorators
'''
Using decorators we can add extra features in the existing function
functions are just like any other object in Python
decorators wrap a function, modifying its behavior.
Python allows you to use decorators in a simpler way with the @ symbol,
sometimes called the “pie” syntax. 
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper



@my_decorator
def say_whee():
    print("Whee! i am working with decorators")
    
say_whee()