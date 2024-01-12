
#Lesson:49 - method overloading and method overriding
'''
Method overloading: 
------------------
Method overloading typically refers to the ability to define
multiple methods in a class with the same name but different parameter lists.
Python does not support method overloading in the traditional sense as some other
programming languages like Java or C++ do.
In Python, if you define multiple methods with the same name in a class, the last
method definition will override any earlier ones. Therefore, you cannot have two
methods with the same name and different parameter lists.
However, Python provides a way to achieve similar functionality through default
parameter values and variable-length argument lists. Here's an example:

'''
class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b!= None:
            s = a + b
        else:
            s = a
            
        return s
    


s1 = Student(58,69)
print(s1.sum(4,6,7))
print(s1.sum(4,6))
print(s1.sum(4))

'''
Method overriding:
-------------------
Method overriding in Python refers to the ability of a subclass to provide a 
specific implementation for a method that is already defined in its superclass. 
When a subclass defines a method that is already present in its superclass, the
method in the subclass overrides the method in the superclass.
'''

class A:
    
    def show(self):
        print("in A show")


class B(A):
    def show(self):
        print("in B show")

a1 = A()
a1.show()

b1 = B()
b1.show()

# or we can take this realistic example
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")
        
# Create instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Call the overridden method
animal.make_sound()  # Output: Generic animal sound
dog.make_sound()     # Output: Bark
cat.make_sound()     # Output: Meow