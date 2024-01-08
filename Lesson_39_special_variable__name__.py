#Lesson:39 - special variable __name__
'''
The value of __name__ changes as per the place of using it.
if you are running the file as main code and you are using name..it will print main..
But if you print __name__ which is imported as a module then it will print the module name 

''' 

print(__name__)


def main():
    print("Hello")
    print("welcome")
    

if __name__ == "__main__":
    main()
    
#it will execute the main function only if it is the starting point.So for instance
# you  define the above lines of code in a module name demo and then import demo in another file 
# and  run that file...it will not execute the main function