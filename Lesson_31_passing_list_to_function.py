#Lesson:31 - pass list to the function
'''
Find the number of even and odd numbers in the list
''' 

def count_numbers(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even += 1
        else:
            odd  += 1
    return even,odd
            

lst = [21,23,34,37,56,59,84]
even,odd = count_numbers(lst)
print("Even elements: ",even)
print("Odd elements: ",odd)
#or you can print like this
print("Even : {} and Odd : {}".format(even,odd))
print(f"Even : {even} and Odd : {odd}")
print("Even : %s and Odd : %s" %(even,odd))
