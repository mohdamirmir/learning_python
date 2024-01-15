#Lesson:60 -  Database connection
'''
install mysql installer

in order to connect mysql with any language you need a connector

pip3 install mysql-connector
'''


import mysql.connector

mydb =mysql.connector.connect(host ="localhost", user="aamir", passwd="1234", database="telusko")

mycursor = mydb.cursor()

# mycursor.execute("show databases")
mycursor.execute("select * from student")

# result = mycursor.fetchall

for i in mycursor:
    print(i)

