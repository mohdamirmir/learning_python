#Lesson:19 - break,continue,pass
'''
Break helps you jump out of the loop
''' 
#break implementation
available = 5
x = int(input("how many candies you : "))
i = 1
while i < x:
    if i > available:
        print("out of stock")
        break
    print("candy")
    i += 1
print("Bye")
   
'''
continue helps you skip an iteration
''' 
#skip numbers divisible by 3
#continue
for i in range(1,31):
    if i%3 == 0:
        continue
    print(i)


#print odd numbers
#pass
print("Odd numberes from 1 to 20")
for i in range(0,21):
    if i%2 == 0:
        pass
    else:
        print(i)
        
