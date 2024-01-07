#Lesson:30 - global variable 
'''
Global variables are accessible throughout the program.However if we name a
varibale with the same name in a function block then preference is given to
local variable. If u want to use the global variable in the fucntion block
you can use the keyword 'global'
''' 

a = 10

def something():
    a = 15
    print('inside funciton',a)
    
something()
print('outside function', a)

'''
To access global varibale inside function
'''

b = 10

def something_():
    global b
    b = 15
    print('inside funciton',b)
    
something_()
print('outside function', b)

'''
you cannot use both local and global inside a function. However there is a
special way to change the value of both local and global varibale.
"globals" keyword is used to access all the global varibales 
'''

c = 20
print(id(c))

def something_():
    c = 15
    x = globals()['c'] # access the global variable a 
    print(id(x))
    globals()['c'] = 25
    
    print('local variable c =',c)
    
something_()
print('global variable c =', c)