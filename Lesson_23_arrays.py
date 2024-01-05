#Lesson:23 - arrays
'''
Arrays are similar to lists with only one difference that all its elements are of same type eg [1,23,45,23]
or ['aamir', 'aamina', 'mir']
''' 
from array import *

vals = array('i',[2,5,334,23,56]) # here i means signed integer(can have both positive and negativ values)
print(vals)
vals.reverse()
print(vals)

for val in vals:
    print(val)
    
newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)
