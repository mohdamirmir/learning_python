#Lesson:16 - if elif
'''
You can specify the flow of execution using the if statements
We make use of indentation to separate the block of code to be executed under if or else statement
'''
x = 8

if x % 2 == 0:
    print(x, "is even") 
else:
    print(x, "is odd")

# we can also do a nested if
if x % 2 == 0:
    print(x, "is even") 
    if(x == 8):
        print("x is eight")
else:
    print(x, "is odd")
    
#if elif else
y = 5

if y == 1:
    print("y is 1")
elif y==2:
    print("y is 2")     
elif y==3:
    print("y is 3")    
elif y==4:
    print("y is 4")    
else:    
    print("wrong choice")