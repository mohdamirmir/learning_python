#Lesson:43 - class - method types
'''
we have various methods in classes
> class methods
> instance methods
> static methods

getters are get methods > they get the value > also called accessors
setters are set methods > they set the value > also called mutators

to work with instance variable we need an instance method eg avergae method as shown in the code below
to work with class variable we need  a class method.. To define a class method u need to use the
@classmethod decorator

static method has nothing do do with instances or class variables..it is used to something extra
we use @staticmethod decorator to define static methods

''' 

class Student:
    school ="Tyndale Biscoe"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def average(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("this is student class..in abc module")
        

s1 = Student(112,34,56)
s2 = Student(12,43,78)

print(s1.average())
print(s2.average())
print(Student.getSchool())
Student.info()