from dataclasses import dataclass
import mysql.connector

def add_emp():
    emp_id = entry_emp_id.get()
    emp_name = entry_emp_name.get()
    emp_email_id = entry_emp_email_id.get()
    emp_salary = entry_emp_salary.get()
    
    output_msg = ""
    output_msg += f"{emp_id}"
    output_msg += f"{emp_name}"
    output_msg += f"{emp_email_id}" 
    output_msg += f"{emp_salary}"   
    output_msg += "Received Successfully"
    
    label_status.configure(text = output_msg)     
    

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
        sql = "insert into emp(emp_id,emp_name,emp_email_id,emp_sal) values(%s,%s,%s,%s)"
        val = (emp_id,emp_name,emp_email_id,emp_salary)
        mycursor.execute(sql,val)
        mydb.commit() 
        mydb.close()
    else:
        print('could not connect to DB')
        
    


import tkinter as bot

root_window = bot.Tk()
root_window.geometry("600x600")

frame_heading = bot.Frame(master=root_window,bg='cyan')
frame_input = bot.Frame(master=root_window,bg='cyan')
frame_operation = bot.Frame(master=root_window)
frame_status = bot.Frame(master=root_window)

frame_heading.pack()
frame_input.pack()
frame_operation.pack()
frame_status.pack()

label_heading = bot.Label(
    master = frame_heading,
    text = 'Employee Management System',
    font = ('Arial',30,'bold'),
    bg = 'cyan',
    fg = 'blue',
    padx = 10,
    pady = 10
)

label_subheading = bot.Label(
    master = frame_input,
    text = 'Add Employee',
    font = ('Arial',24,'bold'),
    bg = 'cyan',
    fg = 'blue',
    padx = 10,
    pady = 10
)

label_emp_id = bot.Label(
    master = frame_input,
    text = 'Enter Employee ID',
    font = ('Arial',20,'normal'),
    bg = 'cyan',
    fg = 'blue',
    padx = 10,
    pady = 10
)

entry_emp_id = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

label_emp_name = bot.Label(
    master = frame_input,
    text = 'Enter Employee name',
    font = ('Arial',20,'normal'),
    bg = 'cyan',
    fg = 'blue',
    padx = 10,
    pady = 10
)

entry_emp_name = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

# label_emailid = bot.Label(
#     master = frame_input,
#     text = 'Enter Employee email ID',
#     font = ('Arial',20,'normal'),
#     bg = 'cyan',
#     fg = 'blue',
#     padx = 10,
#     pady = 10
# )

# entry_emp_emailid = bot.Entry(
#     master = frame_input,
#     font = ('Arial',20,'normal')
# )

label_emp_email_id = bot.Label(
    master = frame_input,
    text = 'Enter Employee email ID',
    font = ('Arial',20,'normal'),
    bg = 'cyan',
    fg = 'blue',
    padx = 10,
    pady = 10
)

entry_emp_email_id = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

label_emp_salary = bot.Label(
    master = frame_input,
    text = 'Enter Employee Salary',
    font = ('Arial',20,'normal'),
    bg = 'cyan',
    fg = 'blue',
    padx = 10,
    pady = 10
)

entry_emp_salary = bot.Entry(
    master = frame_input,
    font = ('Arial',20,'normal')
)

label_status = bot.Label(
    master = frame_status,
    text = '',
    font = ('Arial',20,'normal'),
    bg = 'cyan',
    fg = 'blue',
    padx = 10,
    pady = 10
)

# label_emp_name = bot.Label(
#     master = frame_input,
#     text = 'Enter Employee name',
#     font = ('Arial',20,'normal'),
#     bg = 'cyan',
#     fg = 'blue',
#     padx = 10,
#     pady = 10
# )

# entry_emp_name = bot.Entry(
#     master = frame_input,
#     font = ('Arial',20,'normal')
#     )

button_add_emp = bot.Button(
    master=frame_operation,
    text='Add Employee',
    font=('Arial', 24, 'normal'),
    command=add_emp
)


label_heading.pack()
label_subheading.grid(row=0, columnspan=2)
label_emp_id.grid(row=1, column=0,sticky=bot.E)
entry_emp_id.grid(row=1,column =1)
label_emp_name.grid(row=2, column=0,sticky=bot.E)
entry_emp_name.grid(row=2,column =1)
label_emp_email_id.grid(row=3,column=0,sticky=bot.E)
entry_emp_email_id.grid(row=3,column=1)
label_emp_salary.grid(row=4,column=0,sticky=bot.E)
entry_emp_salary.grid(row=4,column=1)

button_add_emp.pack()
label_status.pack()

bot.mainloop()


