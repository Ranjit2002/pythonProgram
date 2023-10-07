from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    # string = strftime('%H:%M:%S %p')
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 30), background="Black", foreground="yellow")
label.pack(anchor='center')
time()

mainloop()
