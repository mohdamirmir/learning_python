#Lesson:25 - install numpy
'''
multi-dimensional arrays are not supported in python, we need to install numpy
for using multi-dimensional arrays
pip3 install numpy

when we use numpy we dont need to specify the type in the array declaration
''' 
from numpy import *

arr = array([1,2,3,4,5,6])
print(arr)


matrix = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing elements
print(matrix[0, 0])  # Output: 1
print(matrix[2, 1])  # Output: 8

# Modifying an element
matrix[1, 2] = 10
print(matrix[1, 2]) 


#various ways for creating arrays using numpy
# linspace(), logspace(), arange(), zeros(), ones()
