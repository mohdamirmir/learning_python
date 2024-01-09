#Lesson:44 - inner class
'''

''' 

class Student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        
    class Laptop:
        
        def __init__(self):
            self.brand ='HP'
            self.cpu = 'i5'
            self.ram = '8gb'
            
        def show(self):
            print(self.brand,self.cpu,self.ram)
        
        
s1 = Student("Aamir",28)
s2 = Student("Aamina", 29)

s1.show()

lap1 = s1.Laptop
lap2 = s2.Laptop

lap3 = Student.Laptop()