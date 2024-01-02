#Lesson:04 - Lists

'''
list is a collection of values. It can be of of same or different types..
Lists are mutable
'''
nums = [12,34,65,34]
print(nums)
print(nums[0],nums[3], nums[-1])

names = ['aamir','ulfat', 'aamina', 'mir']
print(names)

values = [36,'aamir',45.78]

#list of lists
mil = [nums,names]
print(mil)

#listname.insert(index,value)
nums.insert(2,77)
print(nums)

#listname.remove(value)
nums.remove(34)
print(nums)

#listname.pop(index)
nums.pop(2)
print(nums)

#without index removes last item
nums.pop()
print(nums)

#deletes elements from index 2 to end of list
del nums[2:]
print(nums)

#adding a list ot list
nums.extend([12,23,45,65])
print(nums)

print(min(nums))

print(max(nums))

print(sum(nums))

#sorting a list
nums.sort()
print(nums)