
#401. Program to create a simple GUI

import tkinter as bot

def findSum():
    first_number = entry_first_number.get()
    a = float(first_number)
    second_number = entry_second_number.get()
    b = float(second_number)
    sum = a + b
    output_msg = 'The sum of ' + str(a) + ' and ' + str(b) + ' is = '+ str(sum)
    label_result.configure(text = output_msg)
    
def findDiff():
    first_number = entry_first_number.get()
    a = float(first_number)
    second_number = entry_second_number.get()
    b = float(second_number)
    diff = a - b
    output_msg = 'The difference of ' + str(a) + ' and ' + str(b) + ' is = '+ str(diff)
    label_result.configure(text = output_msg)
    
def findProd():
    first_number = entry_first_number.get()
    a = float(first_number)
    second_number = entry_second_number.get()
    b = float(second_number)
    prod = a * b
    output_msg = 'The Product of ' + str(a) + ' and ' + str(b) + ' is = '+ str(prod)
    label_result.configure(text = output_msg)
    
def findQuo():
    first_number = entry_first_number.get()
    a = float(first_number)
    second_number = entry_second_number.get()
    b = float(second_number)
    div = a / b
    output_msg = 'The Quotient of ' + str(a) + ' and ' + str(b) + ' is = '+ str(div)
    label_result.configure(text = output_msg)
    
def findRem():
    first_number = entry_first_number.get()
    a = float(first_number)
    second_number = entry_second_number.get()
    b = float(second_number)
    quo = a % b
    output_msg = 'The Remainder of ' + str(a) + ' and ' + str(b) + ' is = '+ str(quo)
    label_result.configure(text = output_msg)


#Create the GUI
rootWindow = bot.Tk()
rootWindow.title("Calculator")
rootWindow.geometry("500x300")
rootWindow.configure(bg = 'cyan',padx=20,pady=20)

frame_title = bot.Frame(rootWindow,padx=20,pady=20,bg='red')
frame_input = bot.Frame(rootWindow,padx=20,pady=10,bg='blue')
frame_compute = bot.Frame(rootWindow,padx=20,pady=10,bg='green')
frame_output = bot.Frame(rootWindow,padx=20,pady=10,bg='yellow')

#Create title
label_title = bot.Label(frame_title, text = 'SIMPLE CALCULATOR',font=('Arial',30,'bold'),bg='yellow',fg='red',padx=20,pady=10)

#Create Labels
label_first_number = bot.Label(frame_input, text = 'Enter the first number')
label_second_number = bot.Label(frame_input, text = 'Enter the second number')

#Create Entry boxes
entry_first_number = bot.Entry(frame_input)
entry_second_number = bot.Entry(frame_input)

#Create ADD Button
button_sum = bot.Button(frame_compute, text = 'ADD',command=findSum)
#Create DIFF Button
button_diff = bot.Button(frame_compute, text = 'DIFF',command=findDiff)
#Create PROD Button
button_prod = bot.Button(frame_compute, text = 'PROD',command=findProd)
#Create QUO Button
button_quo = bot.Button(frame_compute, text = 'DIV',command=findQuo)
#Create REM Button
button_rem = bot.Button(frame_compute, text = 'QUO',command=findRem)


#Create the result label
label_result = bot.Label(frame_output,text='Your result will appear here')

#Pack all the widgets
label_title.pack()
label_first_number.pack()
entry_first_number.pack()

label_second_number.pack()
entry_second_number.pack()

button_sum.pack()
button_diff.pack()
button_prod.pack()
button_quo.pack()
button_rem.pack()

frame_title.pack(pady = 20)
frame_input.pack(pady = 20)
frame_compute.pack(pady = 20)
frame_output.pack(pady = 20)


label_result.pack()

rootWindow.mainloop()