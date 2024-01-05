#Lesson:12 - Swap 2 numbers without 3rd variable
'''
First lets do it using third variable
'''
a = 5
b = 7

temp = a
a = b
b = temp

print("a is =", a)
print("b is =", b)

'''
Lets do it using only 2 variables
'''
x = 9
y = 6
print("x is =", x)
print("y is =", y)
x = x + y
y = x  - y
x = x - y
print("x is =", x)
print("y is =", y)

'''
another way is
'''
print("a is =", a)
print("b is =", b)
a,b = b,a
print("a is =", a)
print("b is =", b)

