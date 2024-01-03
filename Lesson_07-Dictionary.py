#Lesson:07 - Dictionary
'''
It is a collection of key: value pairs
key should be immutable and unique
In a dictionary all keys should be unique
'''
data = {1: 'aamir', 2: 'ulfat',3: 'aamina',4: 'mir'}
#to access a value we have to specify the key

print(data[3])
print(data.get(1))

#print(data[5])
print(data.get(5))

# in case you specify the key that does not exist and you want to return something instead of none
#in this case it will return does not exist
print(data.get(5,'does not exist'))

keys = ['aamir','ulfat','ruhi','asmat']
values = ['python', 'java', 'javascript', 'c++']
#merging 2 lists into a dictionary
data = dict(zip(keys,values))
print(data)
data['firdousa'] = 'C'
print(data['firdousa'])

#deleting values
del data['aamir']
print(data)

#here we are using a list and dictionary inside a dictionary as a key value
prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Sublime','Pycharm'], 'Java': {'JSE':'NetBeams','JEE':'Eclipse'}}

print(prog['JS'])

print(prog['Python'])
print(prog['Python'][1])

print(prog['Java'])
print(prog['Java']['JEE'])