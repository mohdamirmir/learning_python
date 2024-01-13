#Lesson:55 -  File handling
'''
Data stored in variables is temporary data... To store data in a persistent way and in a simpler format 
is to store in a file..

w -  which is the write mode, checks if the file exists and if it doesnt exist it will create a new one

'''

#read a file
f = open('myfile','r')
print(f.read())

#write into a file
f1 = open('new_file','w')
f1.write("my data has something \n")

# #append into a file
f2 = open('new_file','a')
f2.write("laptop has some data")


#copyiing from one file to another
for data in f:
    f2.write(data)
    
# rb is read binaray mode ..it can be used to read files like images
img = open("mypic.jpg","rb")

im_copy = open("new_mypic.jpg","wb")

for i in img:
    im_copy.write(i)