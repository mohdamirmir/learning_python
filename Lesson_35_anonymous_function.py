#Lesson:35 - Anonymous function | Lambda
'''
We can pass fucntions to a function.

Lambda functions are often used for short, simple operations 
where a full function definition would be unnecessarily verbose.
''' 
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

# Using both functions
result1 = add(3, 4)
result2 = add_lambda(3, 4)

print(result1)  # Output: 7
print(result2)  # Output: 7
