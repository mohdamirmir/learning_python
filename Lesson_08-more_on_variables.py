#Lesson:08 - more on variables
'''
variable stores a value at a memory location which has a address
in python if u create multiple variable and if some of them have same value, they will point to same location
and if u change the value they will point to different location,thats how python is memory efficent.All you can 
remember is values are stored in labelled boxes and different variable names will point to same labelled 
address if their value is same.. 
Now if there is some data which is not tagged to any variable name, that data is ready for garbage collection
In python there are no constants, although we can intend to use it as constansts
we can know the type of a variabel using type()
'''
num = 5
print(id(num))

a = 10
b = 5
a = b
k = 5
PI = 3.14
print(a,id(a),type(a))
print(b,id(b),type(a))
print(k,id(k),type(a))
print(PI,id(PI),type(PI))

