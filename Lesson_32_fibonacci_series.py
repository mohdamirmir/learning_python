#Lesson:32 - fibonacci series
'''
0 1 1 2 3 5 13 21 ...... 
''' 
num = int(input("Enter the number upto which you want to find the fibonacci series: "))

def fibonacci(num):
    prev = 0
    curr = 1
    print(prev)
    print(curr)
    while curr + prev <= num:
        res = prev + curr
        print(res)
        prev = curr
        curr = res
print(f"Here goes your fibonacci series upto {num}")
fibonacci(num)
