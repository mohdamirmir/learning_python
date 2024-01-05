#Lesson:17 - while loop
'''
For doing reputations of something we use loops. One of them is the while loop
say i wanna print my name 5 times
'''
i = 1

while i <= 5:
    print("aamir")
    i = i + 1
 # or we can implemnt it this way
 
j = 5
while j >= 1:
    print("ulfat")
    j = j - 1
    
# we can also run nested loops

k=0
while k <= 3:
    print("aamir",end="")
    l = 0
    while l <= 5:
        print("l",end="")
        l += 1
    print()    
    k += 1
    

#write a code to print all the numbers from 1 to 100, skip the numbers
#divisibe 3 or 5
num = 1

while num <= 100:
    if num % 3 != 0 and num %5 != 0:  
        print(num)
    num+=1