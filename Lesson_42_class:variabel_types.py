#Lesson:42 - class - variable types
'''
we define class variables outside the __init__ method and instane variables inside the __init__ method
if u make a change to class variable the change would be seen in all the object instances and if
u make a change in an instance variable, the change will be noticed in ony that partiular instance.

''' 
class Car:
    wheels = 4
    
    def __init__(self):
        self.mil = 10
        self.company = "BMW"
        
        
c1 = Car()
c2 = Car()


print(c1.mil,c1.company,c1.wheels)
print(c2.mil,c2.company,c2.wheels)
c1.mil = 8
Car.wheels = 5
print(c1.mil,c1.company,c1.wheels)
print(c2.mil,c2.company,c2.wheels)