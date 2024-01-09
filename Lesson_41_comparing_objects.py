#Lesson:41 - construtor,self and comparing objects
'''
Objects are created in heap memory..
Every time we create an object, it is allocated to new space..
size of an object depends on the number of variables and size of each variable
The size is allocated by the constructor to an object.
self basically refers to the object instance

''' 

class Computer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def update(self):
        self.age = 40
        
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
        
c1 = Computer("aamir",35)
c2 = Computer("ajay", 40)

print(c1.name)
c1.update()
print(c1.age)

#comparing 2 objects
if c1.compare(c2):
    print("they are same")
    