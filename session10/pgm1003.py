'''
Assignment of Session 10:
1. Write a program to connect to the database where you have created employee table.
Extract all the employees from your python code and display it in the tabular format.
Also try display the column headings.

'''
import mysql.connector as bot

mydb = None
print("before connecting : ",mydb)
mydb = bot.connect(
    host = 'localhost',
    user = 'root',
    password = 'Tiger@123',
    database = 'g71s8'
)

if mydb == None:
    print('could not connect to the db')
else:
    print('Connected to the DB successfully !!')

    mycursor = mydb.cursor()
    mycursor.execute("select * from emp")
    
    list_of_emps = mycursor.fetchall()
    for row in list_of_emps:
        s = row
        
        id = s[0]
        empno = s[1]
        job = s[2]
        mgr = s[3]
        hiredate = s[4]
        sal = s[5]
        comm = s[6]
        deptno = s[7]
        
        print(f"|{id:2}|{empno:4}|{job:10}|{mgr:4}|{hiredate:19}|{sal:4}|{comm:4}|{deptno:2}|")
        
        
        
        
        