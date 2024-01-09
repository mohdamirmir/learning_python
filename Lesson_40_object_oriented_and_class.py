#Lesson:40 - Object oriented programming
'''
In real world everything is object and we try to solve the real world problems with
virtual objects
A object had certain attributes and behaviours
fucntions in object oriented programming are called methods..

You can think of a class as a template/bluprint and the instance of class is called an object...
Class - Design
Object - instance

Everything in python is an object

''' 

class Computer:
    
    def config(self):
        print("i5,15gb,1TB")
        
com1 = Computer()
com2 =  Computer()

# we can do it in both ways, here we are passing the instance to config method of computer class
Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()


# special method  -  __init__ method - we use it to intialize our variables and it is similar
# to a constructor 

class Computers():
    def __init__(self, cpu,ram):
        self.cpu = cpu
        self.ram = ram
                
    def config(self):
        print("Config is",self.cpu,self.ram)
        
coms1 = Computers("i5",16)
coms2 = Computers("reyzen 3", 8) 

coms1.config() 
coms2.config() 
    

