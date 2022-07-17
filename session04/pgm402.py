#Area Calculator

from cmath import pi
import tkinter as bot

def findAreaSq():
    first_number = entry_first_number.get()
    a = float(first_number)
    area = a ** 2
    output_msg = "The area of the square of side " + str(a) + ' is = '+str(area)
    label_result.configure(text = output_msg)

def findAreaCircle():
    first_number = entry_first_number.get()
    a = float(first_number)
    area = pi * a * a
    output_msg = "The area of the Circle of radius " + str(a) + ' is = '+str(area)
    label_result.configure(text = output_msg)

#Create the GUI
rootWindow = bot.Tk()
rootWindow.title("Calculator")
rootWindow.geometry("500x300")

#Create Labels
label_first_number = bot.Label(rootWindow, text = 'Enter the side/radius')

#Create Entry boxes
entry_first_number = bot.Entry(rootWindow)

#Create sq Button
button_sq = bot.Button(rootWindow, text = 'SQUARE',command=findAreaSq)
#Create circle Button
button_circle = bot.Button(rootWindow, text = 'CIRCLE',command=findAreaCircle)

#Create the result label
label_result = bot.Label(rootWindow,text='Your result will appear here')

#Pack all the widgets
label_first_number.pack()
entry_first_number.pack()

button_sq.pack()
button_circle.pack()
label_result.pack()

rootWindow.mainloop()