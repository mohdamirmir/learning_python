#Lesson:46 - constructor in inheritance 
'''
when you create an object of sub class, it will call the init of sub class first
if you have a super then it will first call the init of super class and then the
init of sub class
 
''' 
class A:
    def __init__(self):
        print("in A init")
    
    def feature1(self):
        print('feature 1 is working')
        
    def feature2(self):
        print('feature 2 is working')
        


class B(A):

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print('feature 3 is working')
        
    def feature4(self):
        print('feature 4 is working')
        
b = B()
        
        
'''
in case of multiple inheritane 
lets say R inherits from P and Q and R has super in its init..
The question is will it inherit from both P and Q...
in this case it follows MRO(method resolution order) which is always from left to right
So it will print "in P init" and then "in R init"
'''

class P:
    def __init__(self):
        print("in P init")
    
    def feature1(self):
        print('feature 1-P is working')
        
    def feature2(self):
        print('feature 2 is working')
        


class Q():

    def __init__(self):
        print("in 1-Q init")

    def feature1(self):
        print('feature 3 is working')
        
    def feature4(self):
        print('feature 4 is working')
        
class R(P,Q):

    def __init__(self):
        super().__init__()
        print("in R init")
        
    def feat(self):
        super().feature2()
        
r = R()
r.feature1()
r.feat()
 