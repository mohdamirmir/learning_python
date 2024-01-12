#Lesson:50 - Abstract Classes and Abstarct methods
'''
Abstract methods:
Methods which only have a declaration and no definition
Abstract class is a class which has an abstract method..ateast 1

Abstract methods are methods declared in an abstract class that have
no implementation in the abstract class itself. Instead, they are meant
to be implemented by concrete (non-abstract) subclasses. Abstract methods
serve as a way to define a common interface or contract that all subclasses
must adhere to.
In Python, abstract methods are typically defined using the @abstractmethod
decorator from the abc module (Abstract Base Classes). This module provides
tools for working with abstract classes and methods.
'''
from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
class Laptop(Computer):
    def process(self):
        print("it is running")


class Programmer:
    def work(self,com):
        print("solving bugs")
        com.process()
        
        
com1 = Laptop()
lap = Laptop()
lap.process()
prog1 = Programmer()
prog1.work(com1)