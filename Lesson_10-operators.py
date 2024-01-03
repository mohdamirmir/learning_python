#Lesson:10 - Operators
'''
Arthimetic operators
 + , - , * , / etc
Assignment operators
 =
Unary operators
negate the value eg change n to -n

Relational operators
< , > , <= , >= , == , !=

Logical operators
and or and not
for and both conditions should satisfy to be True else it is false
for or one of the  conditions should satisfy to be True else it is false
not is opposite or result(True or False)
'''


x = 2
y = 3

#Arthimetic operations
print("Arthimetic operations")
print(x+y)
print(x-y)
print(x*y)
print(x/y)


#Assignment operations
print("Assignment operations")
z = 5
z = z + 10
z += 10 # is same as z = z + 10
x *=3 # is same as x = x * 3
a,b = 5,6 # is same as a=5 b=6
print(a,b)

#Unary operations
print("Unary operations")
n = 7
print(n)
n = -n
print(n)

#Relational operations
print("Relational operations")
p=5
q=9
print(p>q)
print(p<q)
print(p<=q)
print(p>=q)
print(p==q)
print(p!=q)

#Logical operations
print("Logical operations")
s = 5 
t = 9
print(s<8 and t>6)
print(s<8 and t<6)
print(s<8 or t<6)
print(s<8 or t>6)
print(s>8 or t<6)

l = True
print("l is ", l)
print("negation of l is not l ",not l)
