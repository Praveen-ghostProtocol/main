   
 
import tkinter as bot
from tkinter.tix import COLUMN
from turtle import bgcolor, width   
import mysql.connector
    
def add_student():
    student_name = entry_student_name.get()
    student_email = entry_student_email.get()
    student_phy = entry_student_phy.get()
    student_maths = entry_student_maths.get()
    student_chemistry = entry_student_chemistry.get()
    
    output_msg = ""
    output_msg += f"{student_name} "
    output_msg += f"{student_email} "
    output_msg += f"{student_phy} " 
    output_msg += f"{student_maths} "   
    output_msg += f"{student_chemistry} "   
    output_msg += "Received Successfully"
    
    label_status.configure(text = output_msg,bg='yellow',fg='orange')     
    

    mydb = None
    print("before connecting : ",mydb)
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Tiger@123',
        database = 'g71s12'
    )

    if mydb:
        print('connected to the db successfully!!')
        mycursor = mydb.cursor()
        sql = "insert into student(student_name,student_email,student_phy,student_maths,student_chemistry) values(%s,%s,%s,%s,%s)"
        val = (student_name,student_email,student_phy,student_maths,student_chemistry)
        mycursor.execute(sql,val)
        mydb.commit() 
        mydb.close()
    else:
        print('could not connect to DB')         
        
def search_student():    

    mydb = None
    print("before connecting : ",mydb)
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Tiger@123',
        database = 'g71s12'
    )

    if mydb:
        print('connected to the db successfully!!')
        mycursor = mydb.cursor()
        student_name = entry_student_name.get()
        sql = "select * from student where student_name like %s;"
        mycursor.execute(sql,[student_name])
        
        list_of_headings = ['SID','STUDENT NAME','STUDENT EMAIL','PHY','MATHS','CHEM','TOTAL']
        
        output_msg = ""  
        output_msg += '-'*92+'\n'
        output_msg += f"| {list_of_headings[0]:^6}"
        output_msg += f"| {list_of_headings[1]:^20}"
        output_msg += f"| {list_of_headings[2]:^20}"
        output_msg += f"| {list_of_headings[3]:^6}"
        output_msg += f"| {list_of_headings[4]:^6}"
        output_msg += f"| {list_of_headings[5]:^6}"
        output_msg += f"| {list_of_headings[6]:^6}"
        output_msg += '\n'
        output_msg += '-'*92+'\n'
        for data in mycursor:
            s_id =data[0]
            student_name = data[1]
            student_email = data[2]
            student_phy = data[3]
            student_maths = data[4]
            student_chemistry = data[5]   
            total = student_phy + student_maths + student_chemistry         
            
            output_msg += f"| {s_id:^6} "
            output_msg += f"| {student_name:^20} "
            output_msg += f"| {student_email:^20} "
            output_msg += f"| {student_phy:^6} " 
            output_msg += f"| {student_maths:^6} "   
            output_msg += f"| {student_chemistry:^6} "   
            output_msg += f"| {total:^6}"
            output_msg += '\n'
            print()
            
        output_msg += '\n'+'-'*92
        label_status.configure(text = output_msg,bg='orange',fg='black')                
                           
            
        mydb.commit() 
        mydb.close()
    else:
        print('could not connect to DB')        

def display_student():    

    mydb = None
    print("before connecting : ",mydb)
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Tiger@123',
        database = 'g71s12'
    )

    if mydb:
        print('connected to the db successfully!!')
        mycursor = mydb.cursor()
        sql = "select * from student"
        mycursor.execute(sql)
        
        list_of_students = mycursor.fetchall()
        
        list_of_headings = ['SID','STUDENT NAME','STUDENT EMAIL','PHY','MATHS','CHEM','TOTAL']
        
        output_msg = ""  
        output_msg += '-'*92+'\n'
        output_msg += f"| {list_of_headings[0]:^6}"
        output_msg += f"| {list_of_headings[1]:^20}"
        output_msg += f"| {list_of_headings[2]:^20}"
        output_msg += f"| {list_of_headings[3]:^6}"
        output_msg += f"| {list_of_headings[4]:^6}"
        output_msg += f"| {list_of_headings[5]:^6}"
        output_msg += f"| {list_of_headings[6]:^6}"
        output_msg += '\n'
        output_msg += '-'*92+'\n'
        for data in mycursor:
            s_id =data[0]
            student_name = data[1]
            student_email = data[2]
            student_phy = data[3]
            student_maths = data[4]
            student_chemistry = data[5]   
            total = student_phy + student_maths + student_chemistry         
            
            output_msg += f"| {s_id:^6} "
            output_msg += f"| {student_name:^20} "
            output_msg += f"| {student_email:^20} "
            output_msg += f"| {student_phy:^6} " 
            output_msg += f"| {student_maths:^6} "   
            output_msg += f"| {student_chemistry:^6} "   
            output_msg += f"| {total:^6}"
            output_msg += '\n'
            print()
            
        output_msg += '\n'+'-'*92
        label_status.configure(text = output_msg,bg='orange',fg='black')                
                           
            
        mydb.commit() 
        mydb.close()
    else:
        print('could not connect to DB')        


root_window = bot.Tk()
root_window.geometry("1200x1000")
root_window.config(padx=10,pady=10,bg='yellow')

frame_heading = bot.Frame(master=root_window,bg='yellow')
frame_input = bot.Frame(master=root_window,bg='orange')
frame_operation = bot.Frame(master=root_window)
frame_status = bot.Frame(master=root_window)

frame_heading.pack()
frame_input.pack()
frame_operation.pack()
frame_status.pack()

label_heading = bot.Label(
    master = frame_heading,
    text = 'Student Management System',
    font = ('Arial',30,'bold'),
    bg = 'orange',
    fg = 'black',
    padx = 10,
    pady = 10
)

label_subheading = bot.Label(
    master = frame_input,
    text = 'Add Student',
    font = ('Arial',24,'bold'),
    bg = 'orange',
    fg = 'black',
    padx = 10,
    pady = 10
)

label_student_name = bot.Label(
    master = frame_input,
    text = 'Enter Student name',
    font = ('Arial',20,'normal'),
    bg = 'orange',
    fg = 'black',
    padx = 10,
    pady = 10
)

entry_student_name = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

label_student_email = bot.Label(
    master = frame_input,
    text = 'Enter Student email ID',
    font = ('Arial',20,'normal'),
    bg = 'orange',
    fg = 'black',
    padx = 10,
    pady = 10
)

entry_student_email = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

label_student_phy = bot.Label(
    master = frame_input,
    text = 'Enter Physics Marks',
    font = ('Arial',20,'normal'),
    bg = 'orange',
    fg = 'black',
    padx = 10,
    pady = 10
)

entry_student_phy = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

label_student_maths = bot.Label(
    master = frame_input,
    text = 'Enter Maths Marks',
    font = ('Arial',20,'normal'),
    bg = 'orange',
    fg = 'black',
    padx = 10,
    pady = 10
)

entry_student_maths = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

label_student_chemistry = bot.Label(
    master = frame_input,
    text = 'Enter Chemistry Marks',
    font = ('Arial',20,'normal'),
    bg = 'orange',
    fg = 'black',
    padx = 10,
    pady = 10
)

entry_student_chemistry = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

label_status = bot.Label(
    master = frame_status,
    text = 'Enter student details and click to add!',
    font = ('Courier',20,'normal'),
    bg = 'orange',
    fg = 'black',
    padx = 10,
    pady = 10
)

# label_display = bot.Label(
#     master = frame_status,
#     text = 'Student details will be displayed here!',
#     font = ('Arial',20,'normal'),
#     bg = 'orange',
#     fg = 'black',
#     padx = 10,
#     pady = 10
# )

button_add_student = bot.Button(
    master=frame_input,
    text='Add Student',
    font=('Arial', 24, 'normal'),
    command=add_student
)

button_display_student = bot.Button(
    master=frame_operation,
    text='Display Students',
    font=('Arial', 24, 'normal'),
    command=display_student
)

button_search_student = bot.Button(
    master=frame_operation,
    text='Search Student',
    font=('Arial', 24, 'normal'),
    command=search_student
)

label_heading.pack()
label_subheading.grid(row=0, columnspan=2)
label_student_name.grid(row=1, column=0,sticky=bot.E)
entry_student_name.grid(row=1,column =1)
label_student_email.grid(row=2, column=0,sticky=bot.E)
entry_student_email.grid(row=2,column =1)
label_student_phy.grid(row=3,column=0,sticky=bot.E)
entry_student_phy.grid(row=3,column=1)
label_student_maths.grid(row=4,column=0,sticky=bot.E)
entry_student_maths.grid(row=4,column=1)
label_student_chemistry.grid(row=5,column=0,sticky=bot.E)
entry_student_chemistry.grid(row=5,column=1)
button_add_student.grid(row=6,columnspan=2)

button_display_student.pack()
button_search_student.pack()
label_status.pack()
#label_display.pack()


bot.mainloop()

