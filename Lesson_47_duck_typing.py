#Lesson:47 - polymorphism - Duck typing
'''
one thing with multiple forms.. object has multiple forms
we will discuss
> duck typing
> operator overloading
> method overloading
> method overriding


Duck-Typing: 
If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.
duck typing allows you to use an object based on its behavior, rather than its type. 
If an object supports the necessary methods or attributes that are expected by a piece of code, 
then it can be used in that context, regardless of its actual class or type.
''' 

class Pycharm:
    
    def execute(self):
        print("Compliling")
        print("Running")
        

class MyEditor:
    
    def execute(self):
        print("Spell check")
        print("convention check")        
        print("Compliling")
        print("Running")
        
class Laptop:
    
    def code(self, ide):
        ide.execute()

#ide = Pycharm()
ide = MyEditor()

l1 = Laptop()
l1.code(ide)

# we can change the ide from Pycharm to MyEditor provide it has a method called execute
# it doesnt matter which class object you are passing, what matters is it should have a
# execute method() 
