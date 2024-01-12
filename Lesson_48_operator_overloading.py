#Lesson:49 - Operator overloading
'''
int is basically a class and you call add method on it

Operator overloading in Python refers to the ability to define and customize the behavior
of operators for user-defined objects. Python allows you to define special methods in your
classes that are invoked when certain operators are used on instances of those classes. 
These special methods are also known as "magic methods" or "dunder methods" (short for double underscores).
For example, if you want to use the + operator to perform a custom operation between instances
of your class, you can define the __add__ method in your class.

'''
a=5
b=6
print(int.__add__(5,6)) 
print(a+b)

c="aamir"
d="mir"
print(c+d)
print(str.__add__('aamir','mir')) 


class Student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
 
    def __sub__(self,other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s3 = Student(m1,m2)
        return s3   
  
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)    
        
        
        
s1 = Student(23,34)
s2 = Student(34,45)

s3 = s1 + s2#  Student.__add__(s1,s2)
s4 = s1 - s2
print(s3.m1)
print(s3.m2)
print(s4.m1)
print(s4.m2)


if s1 >  s2:
    print("s1 is greater")
else:
    print("s2 is greater")

print(s1)