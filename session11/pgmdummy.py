#student managemnt system

import tkinter as bot

root_window = bot.Tk()
root_window.geometry("600x500")

frame_heading= bot.Frame(master=root_window)
frame_input= bot.Frame(master=root_window)
frame_operation= bot.Frame(master=root_window)
frame_status= bot.Frame(master=root_window)

frame_heading.pack(pady=10)
frame_input.pack(pady=10)
frame_operation.pack(pady=10)
frame_status.pack(pady=10)

label_heading=bot.Label(
    master=frame_heading,
    text="STUDENT MANGAEMENT SYSTEM",
    background='cyan',
    foreground='blue',
    padx=10,
    pady=10
)

label_name= bot.Label(
    master=frame_input,
    text='enter the name',
    background='cyan',
    foreground='blue',
    padx=10,
    pady=10
)

label_subheading= bot.Label(
    master=frame_input,
    text='add student',
    background='cyan',
    foreground='blue',
    padx=10,
    pady=10
)

label_emailid= bot.Label(
    master=frame_input,
    text='enter emailID',
    background='cyan',
    foreground='blue',
    padx=10,
    pady=10
)
entry_name = bot.Entry(
    master=frame_input
)

label_heading.pack()
label_name.pack()
label_subheading.pack()
label_emailid.pack()

label_subheading.grid(row=0, column=0)
label_name.grid(row=1, column=0)

bot.mainloop()