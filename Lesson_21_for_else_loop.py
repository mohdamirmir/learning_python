#Lesson:21 - for else
'''
Here we are checking for a number divisible by 5...if there is no such number we want to print
a message..in this case we can use for else ...
''' 

nums = [12,13,14,18,23,24]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("There is no such number")