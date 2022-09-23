
from re import S
from tkinter import CENTER, LEFT, RIGHT, messagebox
import mysql.connector

def clear_and_display():
    clear_all()
    display_all_students()

def display_all_students():
    # student_record = (1001,'Kaushal','kaushal@gmail.com',95,96,97,288)
    # treeview_display_students.insert(
    #     parent='',
    #     index='end',
    #     values=student_record
    # )
    
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
        
        for student_record in list_of_students:
            
            sid,sname,semailid,phy_marks,chem_marks,math_marks = student_record
            
            total_marks = phy_marks+chem_marks+math_marks
            
            temp_student = (sid,sname,semailid,phy_marks,chem_marks,math_marks,total_marks)
                        
            treeview_display_students.insert(
            parent='',
            index='end',
            values=temp_student
        )
            
def add_student():
    student_name = entry_student_name.get()
    student_email = entry_student_email.get()
    student_phy = entry_student_phy.get()
    student_maths = entry_student_maths.get()
    student_chemistry = entry_student_chemistry.get()    

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
        messagebox.showinfo(title='Sucess',message='Added to the DB successfully')
    else:
        messagebox.showerror(title='Failure',message='Could not connect to the DB!')
        print('could not connect to DB')         

def clear_all():
   for item in treeview_display_students.get_children():
      treeview_display_students.delete(item)

import tkinter as tk
from tkinter import ttk

root_window = tk.Tk()
root_window.geometry('1200x800')
root_window.configure()

label_frame_display_students=tk.LabelFrame(
    master= root_window,
    text='Display Students'
    # bg='cyan',
    # bd=5
)

label_frame_display_students.pack(
    fill = 'both',
    expand='yes',
    padx = 10,
    pady=10
)

label_frame_input=tk.LabelFrame(
    master= root_window,
    text='Enter the student information'
    # bg='cyan',
    # bd=5
)

label_frame_input.pack(
    fill = 'both',
    expand='yes',
    padx = 10,
    pady=10
)

label_frame_operations=tk.LabelFrame(
    master= root_window,
    text='Operations'
    # bg='cyan',
    # bd=5
)

label_frame_operations.pack(
    fill = 'both',
    expand='yes',
    padx = 10,
    pady=10
)

label_frame_student_info = tk.LabelFrame(
    master = label_frame_input,
    text = 'Student info'
)

label_frame_student_info.pack(
    fill = 'both',
    expand='yes',
    padx = 10,
    pady=10,
    side=LEFT
)

label_frame_student_marks = tk.LabelFrame(
    master = label_frame_input,
    text = 'Student Marks'
)

label_frame_student_marks.pack(
    fill = 'both',
    expand='yes',
    padx = 10,
    pady=10,
    side=RIGHT
)

# label_frame_submit_info = tk.LabelFrame(
#     master = label_frame_input,
#     text = 'Submit info'
# )

# label_frame_submit_info.pack(
#     fill = 'both',
#     expand='yes',
#     padx = 10,
#     pady=10,
#     side=RIGHT
# )

#Display Students
treeview_display_students = ttk.Treeview(
    master=label_frame_display_students,
    columns=(1,2,3,4,5,6,7),
    show='headings'
)

treeview_display_students.heading(1,text='SID')
treeview_display_students.heading(2,text='STUDENT NAME')
treeview_display_students.heading(3,text='EMAIL ID')
treeview_display_students.heading(4,text='PHYSICS')
treeview_display_students.heading(5,text='CHEMISTRY')
treeview_display_students.heading(6,text='MATHS')
treeview_display_students.heading(7,text='TOTAL')

treeview_display_students.pack(
    fill = 'both',
    expand = 'yes',
    padx = 10,
    pady=10
)

button_display_students = tk.Button(
    master = label_frame_operations,
    text = 'Display All Students',
    command=clear_and_display
)



#Taking student information as input
# treeview_enter_information = ttk.Treeview(
#     master = label_frame_input,
    
# )

label_student_name = tk.Label(
    master = label_frame_student_info,
    text = 'Enter Student name',
    font = ('Arial',10,'normal'),
    padx = 10,
    pady = 10
)

entry_student_name = tk.Entry(
    master = label_frame_student_info,
    font = ('Arial',10,'normal')
)

label_student_email = tk.Label(
    master = label_frame_student_info,
    text = 'Enter Student email ID',
    font = ('Arial',10,'normal'),
    padx = 10,
    pady = 10
)

entry_student_email = tk.Entry(
    master = label_frame_student_info,
    font = ('Arial',10,'normal')
)

label_student_phy = tk.Label(
    master = label_frame_student_marks,
    text = 'Enter Physics Marks',
    font = ('Arial',10,'normal'),
    padx = 10,
    pady = 10
)

entry_student_phy = tk.Entry(
    master = label_frame_student_marks,
    font = ('Arial',10,'normal')
)

label_student_maths = tk.Label(
    master = label_frame_student_marks,
    text = 'Enter Maths Marks',
    font = ('Arial',10,'normal'),
    padx = 10,
    pady = 10
)

entry_student_maths = tk.Entry(
    master = label_frame_student_marks,
    font = ('Arial',10,'normal')
)

label_student_chemistry = tk.Label(
    master = label_frame_student_marks,
    text = 'Enter Chemistry Marks',
    font = ('Arial',10,'normal'),
    padx = 10,
    pady = 10
)

entry_student_chemistry = tk.Entry(
    master = label_frame_student_marks,
    font = ('Arial',10,'normal')
)

button_add_student = tk.Button(
    master=label_frame_student_marks,
    text='Add Student',
    font=('Arial', 10, 'normal'),
    command=add_student
)

# button_clear_student_info = tk.Button(
#     master = label_frame_operations,
#     text='Clear',
#     command=clear_all
# )

button_display_students.pack()
label_student_name.grid(row=1, column=0,sticky=tk.E)
entry_student_name.grid(row=1,column =1)
label_student_email.grid(row=2, column=0,sticky=tk.E)
entry_student_email.grid(row=2,column =1)
label_student_phy.grid(row=3,column=0,sticky=tk.E)
entry_student_phy.grid(row=3,column=1)
label_student_maths.grid(row=4,column=0,sticky=tk.E)
entry_student_maths.grid(row=4,column=1)
label_student_chemistry.grid(row=5,column=0,sticky=tk.E)
entry_student_chemistry.grid(row=5,column=1)
button_add_student.grid(row=6,columnspan=2)
# button_clear_student_info.pack()
tk.mainloop()