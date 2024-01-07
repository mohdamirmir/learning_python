#Lesson:28 - Functions
'''
Functions are a reusable block of code/set of statements to perform a speciific task
when your programs gets too big you can divide it into smaller functions.
They also help in reducing the code redundancy. Function can return a value/multiple values with return 
statement and you can pass arguments from function call to function definition and receive them in fucntion
parameters..
''' 

def greet():
    print("Hello")
    print("Good Mornning")

greet()

#adding two numbers

def add(num1,num2): #num1,num2 are parameters
    result = num1 + num2
    print(result)


add(4,5) #4,5 are arguments
add(123,456)


# we can also return the values from the function
def multiply(x,y):
    return x*y

result = multiply(4,6)
print(result)

# we can also return more than one value in python

def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d

sum,diff = add_sub(10,6)
print(sum,diff)


'''
We have actual and formal arguments:
actual being the ones passed in function call

we have different types of arguments:
> positional - provide arguments in sequence
> keyword
> default
> variable

'''

def person(name,age=18): 
    print(name,age)
    
person('aamir',35) #positional
person(name='aamir',age=35) #keyword    
person(name='aamir') #if age is not passed it will take a default value of 18 defined in function definition


def sum(*b): #variable length arguments
    c = 0
    for i in b:
        c = c + i
    print(c) 
    
sum(12,23,45,56)

    
        


