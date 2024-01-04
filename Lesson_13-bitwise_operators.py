#Lesson:13 - Bitwise operators
'''
~ (tilde) - complement
& AND
| OR
! NoT
^ XOR
'''

#Compliment
print(~12)


#AND operation
print(12&13)
'''
12 > 00001100
13 > 00001101
& ------------(perform AND on bits)
     00001100 -> 8

'''

#OR operation
print(12|13)
'''
12 > 00001100
13 > 00001101
| ------------(perform OR on bits)
     00001101 -> 9
'''

#XOR operation
print(12^13)
'''
12 > 00001100
13 > 00001101
^ ------------(perform OR on bits)
     00000001 -> 1
'''