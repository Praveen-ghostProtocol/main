'''
Program to connect a specific database and retrieve the data from student table

'''

import mysql.connector as bot

mydb = None
print("before connecting : ",mydb)
mydb = bot.connect(
    host = 'localhost',
    user = 'root',
    password = 'Tiger@123',
    database = 'g71s6'
)

if mydb == None:
    print('could not connect to the db')
else:
    print('Connected to the DB successfully !!')

    mycursor = mydb.cursor()
    mycursor.execute("select * from student")
    
    list_of_students = mycursor.fetchall()
    for row in list_of_students:
        s = row
        
        studentid = s[0]
        sname = s[1]
        grade = s[2]
        course = s[3]
        emailid = s[4]
        print(f"|{studentid:4}|{sname:17}|{grade:2}|{course:28}|{emailid:28}|")