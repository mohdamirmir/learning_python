#Lesson:14 - import math functions 
import math
x=math.sqrt(25)
print(x)

print(math.floor(2.5)) #takes upper limit
print(math.ceil(2.5)) #takes lower limit
print(math.pow(3,2))
print(math.pi)
print(math.e)

# you can also import and alias it as
# import math as m
#from math import sqrt,pow
# print(help(math))

from math import factorial as fac

print(fac(5))