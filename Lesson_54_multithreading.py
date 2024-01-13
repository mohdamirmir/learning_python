#Lesson:54 -  Multithreading
'''
Multithreading in Python allows you to run multiple threads (smaller units of a process) concurrently. 
Python's threading module provides a way to create and manage threads.However, due to the Global Interpreter
Lock (GIL) in CPython (the reference implementation of Python), multithreading in Python may not provide
true parallelism for CPU-bound tasks. 
It is still useful for I/O-bound tasks, such as network communication or file I/O.
you need to import from threading lib and define the run method..You run threads by using the start() method..
And then you madke the threads join the main thread using join() method
With the help of threads you can use multiple cores and execute things simultaneously
'''
from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(20):
            print("Hello")
            sleep(1)
            
class Hi(Thread):
    def run(self):
        for i in range(20):
            print("Hi")
            sleep(1)
            


obj1 = Hello()
obj2 = Hi()

#starting threads
obj1.start()
sleep(0.2)
obj2.start()

#by default every execution has one thread which means if you are not creating a thread by yourself
# you have one thread..It is called main thread
#wait for both threads to finish and join them to main thread
obj1.join()
obj2.join()
print("bye")


