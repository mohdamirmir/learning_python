#Lesson:15 - Getting input from user
'''
The input() function always returns a string.
so if you intend to add 2 numbers you need to convert them into to int in order to perform the addition
'''

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = x + y
print("The result is:",z)

#input a character
#no matter how many characters you enter, it will pick only the first character
char = input("Enter a character: ")[0]
print(char)

# you can also evaluate an expression using eval function eg 2 + 4 - 3
expr  = eval(input('Enter the expression: '))
print(expr)

#it is also possible to provide values  while running the .py file from command line
# python main.py 3 5
# indexes  0 - for file    1 2 and so on.. for the values you provide with the file name
#we can so it with the argv

from sys import argv
#argv[0] is for filename
a = int(argv[1])
b = int(argv[2])
c = a + b
print(c)

#Also if we had imported just sys eg import sys then we need to use sys.argv in code instead of just argv
 