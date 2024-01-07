#Lesson:34 - Recursion
'''
When a function calls itself.
By default you can do recursion for only 1000 times
we will find the factorial by recursion
''' 
num =int(input("Enter the number: "))
def factorial(num):
     
     if num == 0:
         return 1
     else:
         return num * factorial(num-1)



result = factorial(num)
print(f"the factorial for number {num} is {result}")