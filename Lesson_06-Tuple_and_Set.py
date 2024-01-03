#Lesson:06 - Tuple & Set

'''
Like lists, a tuple is a collection of values.Hoewever unlike lists it is immutable..
tuples are represented in ()
you should use tuple when you a collection of values whom you dont wanna change.
Since values dont change in tuple, the iteration is faster than list and hence can be used to
enhance the speed of execution.
'''
tup = (34,23,56,45)
print(tup)
print(tup[1])
#tup[1] = 67 # doesnt work since they are immutable

#count will give the occurance iof a particular value
print(tup.count(23))


'''
Set is a collection of unique elements 
sets are represented in {}
set uses the concept of hash. values in sets dont follow a sequence and it doesnt support duplicate values
set doesnt support indexing so we cannot assign values..However we can add values using method add.
'''
set1 = {22,25,14,23,16}
print(set1)
print(set1)
set2 = {23,45,67,34,23,89}

print(set2)
print(set2)
set2.add(97)
print(set2)
set2.remove(67)
print(set2)