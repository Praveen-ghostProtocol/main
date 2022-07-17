import mysql.connector as bot

mydb = None
print("before connecting : ",mydb)
mydb = bot.connect(
    host = 'localhost',
    user = 'root',
    password = 'Tiger@123'
)

if mydb:
    print('connected to the db successfully!!')
else:
    print('could not connect to DB')
    
mycursor = mydb.cursor()

mycursor.execute("show databases;")

for db in mycursor:
    print(db)