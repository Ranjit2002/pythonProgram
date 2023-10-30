"""
from tkinter import *

window = Tk()       # We can use anything instead of window
window.title("Welcome to TKINTER")
window.mainloop()

from tkinter import *

ranjit = Tk()
ranjit.title("Welcome to Tkinter")
lbl = Label(ranjit, text="Hello")
lbl.grid(column=0, row=0)
lbl1 = Label(ranjit, text="Hello")
lbl1.grid(column=2, row=1)
ranjit.mainloop()

from tkinter import *

ranjit = Tk()
ranjit.title("Welcome to Tkinter")
ranjit.geometry('350x200')
lbl = Label(ranjit, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(ranjit, text="Click Me", bg="orange", fg="red")
btn.grid(column=1, row=0)
ranjit.mainloop()

from tkinter import *

ranjit = Tk()
ranjit.title("Welcome to Tkinter")
ranjit.geometry('350x200')
lbl = Label(ranjit, text="Hello")
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")


btn = Button(ranjit, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
text = Entry(ranjit, width=10)
text.grid(column=1, row=0)
ranjit.mainloop()

# ttk module provides access to the Tk themed widget set
from tkinter import *
from tkinter.ttk import *

ranjit = Tk()
ranjit.title("Welcome to Tkinter")
ranjit.geometry('350x200')
combo = Combobox(ranjit)
combo['values'] = (1, 2, 3, 4, 5, 'Ranjit', 'Aachal')
combo.current(1)    # Set the selected item
combo.grid(column=0, row=0)
ranjit.mainloop()

from tkinter import *
from tkinter.ttk import *

ranjit = Tk()
ranjit.title("Welcome to Tkinter")
ranjit.geometry('350x200')

# chk_state = BooleanVar
# chk_state.set(True)     # Set check state

chk_state = IntVar()
chk_state.set(0)    # Unckeck
chk_state.set(1)
chk = Checkbutton(ranjit, text='Choose', var=chk_state)
chk.grid(column=0, row=0)
ranjit.mainloop()

from tkinter import *
from tkinter.ttk import *

ranjit = Tk()
ranjit.title("Welcome to Tkinter")
ranjit.geometry("350x200")

selected_value = IntVar()

rad1 = Radiobutton(ranjit, text='First', value=1, variable=selected_value)
rad2 = Radiobutton(ranjit, text='Second', value=2, variable=selected_value)
rad3 = Radiobutton(ranjit, text='Third', value=3, variable=selected_value)

rad1.grid(column=0, row=0)
rad2.grid(column=0, row=1)
rad3.grid(column=0, row=2)
ranjit.mainloop()
"""

from tkinter import *
from tkinter.ttk import *

ranjit = Tk()
ranjit.title("Welcome to Tkinter")
selected = IntVar()
rad1 = Radiobutton(ranjit, text='First', value=1, variable=selected)
rad2 = Radiobutton(ranjit, text='Second', value=2, variable=selected)
rad3 = Radiobutton(ranjit, text='Third', value=3, variable=selected)

def clicked():
    print(selected.get())


btn = Button(ranjit, text="Click Me", command=clicked)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
ranjit.mainloop()
