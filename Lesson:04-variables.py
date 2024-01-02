#Lesson:04 - Variables
'''
We can think of a variable as a container in which we store some value
eg x = 5
'''
x = 5
x = x + 2
print(x)

y =  6
y = y - 4
print(y)

z = 'youtube'
z = z + ' rocks'
print(z)
print(z[0],z[3],z[8],z[-1],z[-3])
print(z[0:3])
print(z[1:4])
print(z[3:])
print(z[:6])

#note strings are immutable

#z[0] = 'R' # this wont be allowed for strings
my_name ="mohd aamir mir"
print(len(my_name))