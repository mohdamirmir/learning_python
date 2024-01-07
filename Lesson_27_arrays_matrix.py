
#Lesson:27 - operations on  array
'''
> 2d array
> 3d array
> matrix
''' 
from numpy import *

arr1 = array([
                [1,2,3,6,2,9],
                [4,5,6,7,5,3]
            ])
print(arr1.dtype)
print(arr1.ndim) #2D array
print(arr1.shape) #rows X columns
print(arr1.size) #elements

#converting  2D array into 1D array
print(arr1)
arr2 = arr1.flatten()
print(arr2)

#converting  1D array into 3D array
arr3 = arr2.reshape(3,4)
print(arr3)

#converting  2D array into 3D array
arr4 = arr1.reshape(3,4)
print(arr4)

#converting  2D array into two 2D arrays
arr5 = arr1.reshape(2,2,3)
print(arr5)

# creating a matrix
m = matrix('1,2,3;4,5,6;7,8,9')
print(m)
#to print diagonal elements
print(diagonal(m))
print(m.min())
print(m.max())


m1 = matrix('1,2,3;6,4,5;1,6,7')
m2 = matrix('1,2,3;4,5,6;7,8,9')

m3 = m1 * m2
print(m3)