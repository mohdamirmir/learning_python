#Lesson:38 - Modules
'''
Your code should be modular...
This helps in reusability of code, reducing redundancy, making it easier to debug etc..
''' 
import Calc
res_sub = Calc.subtract(11,4)
print(res_sub)

#you can either used it like this or if you dont wanna mention module name everytime which is Calc here
# you can use as described below

from Calc import *
res = add(5,6)
print(res)