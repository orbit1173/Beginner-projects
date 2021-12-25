import random
from tkinter import *

root=Tk()
root.geometry("700x450")

i1=Label(root,font=("times",200))

def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    i1.config(text=f'{random.choice(number)}{random.choice(number)}')
    i1.pack()

b1=Button(root,text="Lets roll",command=roll)
b1.place(x=320,y=0)

root.mainloop()