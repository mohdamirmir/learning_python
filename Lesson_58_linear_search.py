#Lesson:58 -  Linear Search
'''
Search for element in a list one by one
'''

pos = -1
def search(list,n):
    
#one  method is to use for loop
    for i in range(0,len(list)):
        if list[i] == n:
            globals() ['pos'] = i
            return True
    return False        
    
#alternate method is to do is using while loop    
    # i = 0
    # while i < len(list):
    #     if list[i] == n:
    #         globals() ['pos'] = i
    #         return True
    #     i = i + 1
    
    # return False
    


list = [5,8,4,6,9,2]

n = 6


if search(list,n):
    print("number found at index ", pos)
else:
    print("not found")