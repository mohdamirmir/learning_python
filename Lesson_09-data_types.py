#Lesson:09 - Data Types
'''
> None
> int (eg. a = 5)
> float(eg. pi = 3.14)
> bool(eg. True , False )
> complex (eg. num = 6 +9j)
> list
> tuple
> set
> range
> dict
'''
num = 5
print(type(num))

num1 = 3.14
print(type(num1))

decision = True
print(type(decision))

num2 = 9 +6j
print(type(num2))

a=5
b=4

#TypeCasting

number = int(3.9)
print(number,type(number))

c = complex(a,b)
print(c)

bool = a > b
print(bool,type(bool))

print(int(True))
print(int(False))

lis = [1,34,67,34]
print(lis,type(lis))

s = {23,56,34,89}
print(s,type(s))

t = (34,56,45,22,11)
print(t,type(t))

str = 'aamir mir'
print(str,type(str))
st = 'a'
print(st,type(st))

print(list(range(10)))
print(type(range(10)))
print(list(range(2,26,2)))

d = {'aamir': '11promax', 'ulfat': 'vivo', 'mom': 'redmi'}
print(d, type(d))
print(d.keys())
print(d.values())
print(d['ulfat'])
print(d.get('aamir'))