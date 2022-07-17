
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

#Create Labels
label_first_number = bot.Label(rootWindow, text = 'Enter the first number')
label_second_number = bot.Label(rootWindow, text = 'Enter the second number')

#Create Entry boxes
entry_first_number = bot.Entry(rootWindow)
entry_second_number = bot.Entry(rootWindow)

#Create ADD Button
button_sum = bot.Button(rootWindow, text = 'ADD',command=findSum)
#Create DIFF Button
button_diff = bot.Button(rootWindow, text = 'DIFF',command=findDiff)
#Create PROD Button
button_prod = bot.Button(rootWindow, text = 'PROD',command=findProd)
#Create QUO Button
button_quo = bot.Button(rootWindow, text = 'DIV',command=findQuo)
#Create REM Button
button_rem = bot.Button(rootWindow, text = 'QUO',command=findRem)


#Create the result label
label_result = bot.Label(rootWindow,text='Your result will appear here')

#Pack all the widgets
label_first_number.pack()
entry_first_number.pack()

label_second_number.pack()
entry_second_number.pack()

button_sum.pack()
button_diff.pack()
button_prod.pack()
button_quo.pack()
button_rem.pack()


label_result.pack()

rootWindow.mainloop()