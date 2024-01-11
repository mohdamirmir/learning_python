#Lesson:48 - Operator overloading
'''
int is basically a class and you call add method on it
'''
a=5
b=6
print(int.__add__(5,6)) 
print(a+b)

c="aamir"
d="mir"
print(c+d)
print(str.__add__('aamir','mir')) 
