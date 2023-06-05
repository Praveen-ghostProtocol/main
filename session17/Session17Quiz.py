import tkinter as tk

def sel():
    selection = "You selected the option "+ str(var.get())
    label.config(text = selection)
    
root = tk.Tk()
var = tk.IntVar()
R1 = tk.Radiobutton(master = root,text = "Option 2",variable=var,value=2,command=sel)
R1.pack(anchor=tk.W)
R2 = tk.Radiobutton(master = root,text = "Option 2",variable=var,value=2,command=sel)
R2.pack(anchor=tk.W)
R3 = tk.Radiobutton(master = root,text = "Option 2",variable=var,value=2,command=sel)
R3.pack(anchor=tk.W)
R4 = tk.Radiobutton(master = root,text = "Option 2",variable=var,value=2,command=sel)
R4.pack(anchor=tk.W)

label = tk.Label(root)
label.pack()
root.mainloop()