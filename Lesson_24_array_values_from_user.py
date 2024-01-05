#Lesson:24 - arrays values from user in python
'''
intializing an array by inputs given from user 
''' 
from array import *
arr = array('i',[])

n = int(input("Enter the length of array: "))

for i in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)
    
print(arr)

val = int(input("enter the value u wanna search: "))
k = 0
for e in arr:
    if e ==val:
        print(k)
        break
    k += 1

# other way to find
print(arr.index(val))