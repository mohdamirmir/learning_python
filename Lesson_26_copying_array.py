#Lesson:26 - operations on  array
'''
Lets perform some operations on the arrays
when we copy one array into another, they point to the same address
There are  2 copy methods for an array
> shallow copy
> deep copy
''' 
from numpy import *

arr = array([1,2,3,4,5])
print(arr)
arr = arr + 5
print(arr)
arr1 = array([10,21,32,43,54])
arr2 = array([12,20,30,40,50])

arr3 = arr1  + arr2
print(arr3)
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(square(arr1))
print(sqrt(arr1))

arr2 = arr1
print(arr1,id(arr1))
print(arr2,id(arr2))

#if u want to copy an array but have a different address
arr4 = arr1.view()
print(arr1,id(arr1))
print(arr4,id(arr4))

# we have two types of copying 
# > shallow copy  
# > deep copy
# in shallow copy if we modify any change in the array we copied from, it is also reflected
# in the copied array

arr1[1] = 111
print(arr1,id(arr1))
print(arr4,id(arr4))

#when we deep copy the two arrays are no way linked
#for deep copy we use copy() method, you will notice when we change an element of array we copy from,
# the change is seen only in that array and no change is seen in the copued array

arr5 = arr1.copy()
arr1[2] = 222
print(arr1,id(arr1))
print(arr5,id(arr5))