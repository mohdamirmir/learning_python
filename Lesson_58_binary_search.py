#Lesson:58 -  Binary Search
'''
In binary search the values have to be sorted first
we have the upper bound and lower bound

mid index = (Lower + upper)/2 eg. 0 + 5 / 2 = 2

if search value is smaller then change upper bound 
and mid becomes new upper bound

if search value is bigger then change lower bound
and mid becomes new lower bound
'''

pos = -1

def search(list,n):
    
    l = 0
    u = len(list) - 1
    
    while l <= u:
        mid = (l+u) // 2
        
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    
    return False
         

list = [4,7,8,12,45,99,102,303,435,657,678,778,889,990]
n = 657

if search(list,n):
    print("Number Found at", pos)
else :
    print("Number not Found")
