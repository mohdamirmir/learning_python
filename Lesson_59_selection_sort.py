#Lesson:59 -  Selection Sort
'''
in seletion sort you find the min position and then you swap the min value with i element of list
so the first iteration will get u the minimum value...in next iteration you treat the first element 
as sorted array and then you find the min value in the rest of the arrray which means you are searching
2nd element of the array

'''

def sort(list):
    
    for i in range(0,len(list)-1):
        min_pos = i
        for j in range(i,len(list)-1):
            if list[j] < list[min_pos]:
                min_pos = j
        temp = list[i]
        list[i] = list [min_pos]
        list[min_pos] = temp
                




list = [5,3,8,6,7,2,10,34]

sort(list)
print(list)



