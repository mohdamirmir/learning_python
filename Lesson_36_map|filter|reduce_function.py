#Lesson:36 - Filter | Map | Reduce
'''
For filteing elements in a sequnce you can make use of "filter()" function
filter takes 2 arguments 
> a function
> a sequence(eg a list)
and returns True or false based on the function logic.

For performing some action on each element in a sequence we can make us of "map()" function
eg we wanna double every element in the list. Similar to filter, it also take 2 arguments.

We also have "reduce()" function. we can use it to reduce all the elements value to one,
say find the sum of all elements in the list. The reduce fucntions belong to a module called
functools so we have to import it before using it
''' 

def is_even(n):
    return n%2==0

nums = [5,12,23,45,24,55,34,33,23,56,77,88,67]

#using Filter function
even = list(filter(is_even,nums)) 
print(even)

#instead  of defining a function is_even we can make use of a lamba function shown below
# for finding odd numbers

odds = list(filter(lambda n: n%2 != 0, nums))
print(odds)

# Map function - say we want to double each element

doubles = list(map(lambda n: n*n,nums))
print(doubles)

from functools import reduce

sum = reduce(lambda a,b: a+b,nums)
print(sum)

