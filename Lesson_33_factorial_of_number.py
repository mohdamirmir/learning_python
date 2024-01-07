#Lesson:33 - factorial of a number
'''
eg 
5! = 5*4*3*2*1
''' 
num = int(input("Enter the number: "))

def factorial(num):
    result = 1
    while num >=1:
        result = num  * result
        num = num - 1
    return result

fact = factorial(num)
print(f"Factorial for {num} is {fact}")

'''
You can also do using the for loop


def factorial(num):
    result = 1
    for i in range(1,num+1)
        result = num  * result
    return result


'''