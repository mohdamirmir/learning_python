#Lesson:20 - printing patterns
'''
# # # #
# # # #
# # # #
# # # #
''' 

for i in range(0,4):
    for j in range(0,4):
        print("#",end=" ")
    print()
    
# OR

for i in range(0,4):
    print("# # # #")


'''
# 
# #
# # #
# # # #
'''
print("pattern 2")
for i in range(0,4):
    for j in range(i+1):
        print("#",end=" ")
    print()

'''
# # # #
# # # 
# # 
# 
'''
print("pattern 3")
for i in range(0,4):
    for j in range(4-i):
        print("#",end=" ")
    print()