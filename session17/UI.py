import tkinter as tk
from tkinter import Button, messagebox
import Quiz

root = tk.Tk()
root.geometry("800x450")
root.title("MCQ Quiz")


class UI:
    var = tk.IntVar()
    def __init__(self):
        self.render()

    def render(self):
        quiz = Quiz.Quiz()        
        for ques in quiz.questionlist:
            label = tk.Label(master = root)
            label.config(text = ques.questiontext)
            label.pack(anchor=tk.W)
            k = 1
            for ans in quiz.answerlist:
                R1 = tk.Radiobutton(master = root,text = ans.answertext,variable=self.var,value=k,command=self.sel)
                R1.pack(anchor=tk.W)
                k+=1
        
        
        root.mainloop()
        
    def sel(self):
        print('You selected the option '+str(self.var.get()))

ui = UI()

        # R2 = tk.Radiobutton(
        #     master = root,
        #     text = "Option 2",
        #     variable=var,
        #     value=2,
        #     command=sel
        # )

        # R2.pack(anchor=tk.W)

        # R3 = tk.Radiobutton(
        #     master = root,
        #     text = "Option 3",
        #     variable=var,
        #     value=3,
        #     command=sel
        # )

        # R3.pack(anchor=tk.W)

        # R4 = tk.Radiobutton(
        #     master = root,
        #     text = "Option 4",
        #     variable=var,
        #     value=4,
        #     command=sel
        # )

        # R4.pack(anchor=tk.W)

                
    
    # def sel():
    #     selection = "You selected the option" + var.get()
    #     label.config(text = selection)
        
