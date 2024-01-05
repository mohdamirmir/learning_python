#Lesson:22 - prime number
'''
Prime number is a number which is divisble by 1 and the number itself
eg 1,2,3,5,7,11,13,17,19,23 and so
''' 
from math import floor
num = int(input("Enter the number: "))

if num < 2:
    print(num,"is not primeprime")
else:
    for i in range(3, floor(num/2) + 1):
        if num % i == 0:
            print(num,"is not prime")
            break
    else:   
        print(num,"is prime")