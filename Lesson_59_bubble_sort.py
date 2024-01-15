#Lesson:58 -  Bubble Sort
'''
comparing 2 elements and swap them if the list[i] > list[i+1]
After 1 iteration you will find the biggest element at the end
so if there are n elements then after n-1 iterations the list will be sorted
'''

def sort(list):
    
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp



list = [5,3,8,6,7,2,10,34]

sort(list)
print(list)



