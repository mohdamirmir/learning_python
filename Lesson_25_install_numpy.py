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

#various ways for creating arrays using numpy
# linspace(), logspace(), arange(), zeros(), ones()