#Lesson:45 - inheritance
'''
whatever belongs to the parent class belongs to the child class
Here we are defining  class B which is inheriting from class A which means
A is the parent class and B is the child class.. B will have both the features 1 and 2 apart from its
own features 3 and 4.. this is single level inheritance
''' 

class A:
    
    def feature1(self):
        print('feature 1 is working')
        
    def feature2(self):
        print('feature 2 is working')
        


class B(A):

    def feature3(self):
        print('feature 3 is working')
        
    def feature4(self):
        print('feature 4 is working')
        

a = A()

a.feature1()
a.feature2()

b = B()

b.feature1()
b.feature2()
b.feature3()
b.feature4()

'''
multi-level inheritance
we will define a class C which will inherit from B..But since B itself inherits from A so 
C will have features from both A and B..
''' 

class C(B):

    def feature5(self):
        print('feature 5 is working')
        
    def feature6(self):
        print('feature 6 is working')
      
c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()

'''
we also have multiple inheritance where a class derives from more than one class
say there are 2 different classes P and Q and we want to have a class R that should have
features from both the classes P and Q... we will define a class like this

'''
class P:

    def featureP(self):
        print('feature P is working')
        
class Q:
    
    def featureQ(self):
        print('feature Q is working')
        
class R(P,Q):
    
    def featureR(self):
        print('feature R is working')
        
r = R()
r.featureP()
r.featureQ()
r.featureR()


'''
Moreover we should note that child class accesses all the features of the parent class but parent class
doesnt access the features of child class
'''