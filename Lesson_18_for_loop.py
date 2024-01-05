#Lesson:18 - for loop
'''
for printing values of sequences like a list or tuple, we can use a for loop
'''

val = ['aamir','khabib',35,4.98]

#here v will represent one element of val in each iteration
for v in val:
    print(v)
    
string = "mohdaaamirmirisveryhandsome"
for s in string:
    print(s)
    
    
for i in range(10):
    print(i)
    
#we can also start from some number
print("print 5 to 25")
for i in range(5,25,1):
    print(i)
print("print in reverse order")
for i in range(55,45,-1):
    print(i)    