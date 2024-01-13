#Lesson:53 -  Exception Handling
'''
> compile time error - eg syntactical errors - wrong syntax eg misisng of : etc

> logical error - wrong logic eg wrong output

> runtime error - errors coming up at runtime - eg wrong input eg 6/0

'''

a = 5
b = 0

try:
    print("resource open")
    print(a/b)
    k =  int(input("Enter the number"))
    print(k)
    
except ZeroDivisionError as e:
    print("Hey you cannot divide the number by zero",e)

except ValueError as e:
    print("You have entered a wrong input",e)
    
except Exception as e:
    print("Something went wrong",e)
    
finally:
    print("The resource is closed")