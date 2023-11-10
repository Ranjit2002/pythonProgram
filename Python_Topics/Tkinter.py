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
import tkinter
# from tkinter import *
# from tkinter.ttk import *
#
# ranjit = Tk()
# ranjit.title("Welcome to Tkinter")
# selected = IntVar()
# rad1 = Radiobutton(ranjit, text='First', value=1, variable=selected)
# rad2 = Radiobutton(ranjit, text='Second', value=2, variable=selected)
# rad3 = Radiobutton(ranjit, text='Third', value=3, variable=selected)
#
# def clicked():
#     print(selected.get())
#
#
# btn = Button(ranjit, text="Click Me", command=clicked)
# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=2, row=0)
# ranjit.mainloop()

# from tkinter import *
#
# root = Tk()
# root.title("Calculator")
# root.geometry("450x140")
#
# def func1():
#     a = int(enum1.get())
#     b = int(enum2.get())
#     lres1.config(text=str(a+b), bg='orange')
#
# def func2():
#     a = int(enum1.get())
#     b = int(enum2.get())
#     lres2.config(text=str(a-b), bg='orange')
#
# def func3():
#     a = int(enum1.get())
#     b = int(enum2.get())
#     lres3.config(text=str(a*b), bg='orange')
#
# def func4():
#     a = int(enum1.get())
#     b = int(enum2.get())
#     lres4.config(text=str(a/b), bg='orange')
#
# def func5():
#     a = int(enum1.get())
#     b = int(enum2.get())
#     lres5.config(text=str(a//b), bg='orange')
#
#
# lnum1 = Label(root, text="Num 1")
# lnum1.grid(row=0, column=0)
#
# enum1 = Entry(root)
# enum1.grid(row=0, column=1)
#
# lenum2 = Label(root, text="Num 2")
# lenum2.grid(row=1, column=0)
#
# enum2 = Entry(root)
# enum2.grid(row=1, column=1)
#
# btn = Button(root, text="ADD", command=func1)
# btn.grid(column=0, row=2)
#
# lres1 = Label(root, text="")
# lres1.grid(row=3, column=0)
#
# btn = Button(root, text="SUBTRACT", command=func2)
# btn.grid(column=1, row=2)
#
# lres2 = Label(root, text="")
# lres2.grid(row=3, column=1)
#
# btn = Button(root, text="MULTIPLY", command=func3)
# btn.grid(column=2, row=2)
#
# lres3 = Label(root, text="")
# lres3.grid(row=3, column=2)
#
# btn = Button(root, text="DIVIDE", command=func4)
# btn.grid(column=3, row=2)
#
# lres4 = Label(root, text="")
# lres4.grid(row=3, column=3)
#
# btn = Button(root, text="FLOOR", command=func5)
# btn.grid(column=4, row=2)
#
# lres5 = Label(root, text="")
# lres5.grid(row=3, column=4)
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
# root.title("Fibonacci")
# root.geometry("200x200")
#
# def fibonacci():
#     a, b = 0, 1
#     for i in range(n):
#
#
# a = int(enum1.get())
#     b = int(enum2.get())
#     lres1.config(text=str(a+b), bg='orange')

# import tkinter as tk
#
# # Function to check if a number is an Armstrong number
# def is_armstrong_number(num):
#     num_str = str(num)
#     num_digits = len(num_str)
#     total = sum(int(digit) ** num_digits for digit in num_str)
#     return total == num
#
# # Function to handle the button click event
# def check_armstrong():
#     input_number = int(entry.get())
#     if is_armstrong_number(input_number):
#         result_label.config(text=f"{input_number} is an Armstrong number")
#     else:
#         result_label.config(text=f"{input_number} is not an Armstrong number")
#
#
# # Create the main window
# window = tk.Tk()
# window.title("Armstrong Number Checker")
# window.geometry('300x150')
#
# # Create and configure input entry widget
# entry_label = tk.Label(window, text="Enter a number:")
# entry_label.pack()
# entry = tk.Entry(window)
# entry.pack()
#
# # Create and configure result label
# result_label = tk.Label(window, text="")
# result_label.pack()
#
# # Create and configure check button
# check_button = tk.Button(window, text="Check", command=check_armstrong)
# check_button.pack()
#
# # Start the Tkinter main loop
# window.mainloop()

# from tkinter import Tk, Label, Entry, Button
#
# # Function to check if a number is an Armstrong number
# def is_armstrong_number(num):
#     num_str = str(num)
#     num_digits = len(num_str)
#     total = sum(int(digit) ** num_digits for digit in num_str)
#     return total == num
#
# # Function to handle the button click event
# def check_armstrong():
#     input_number = int(entry.get())
#     if is_armstrong_number(input_number):
#         result_label.config(text=f"{input_number} is an Armstrong number")
#     else:
#         result_label.config(text=f"{input_number} is not an Armstrong number")
#
#
# # Create the main window
# window = Tk()
# window.title("Armstrong Number Checker")
# window.geometry('300x150')

# Create and configure input entry widget
# entry_label = Label(window, text="Enter a number:")
# entry_label.pack()
# entry = Entry(window)
# entry.pack()
#
# # Create and configure result label
# result_label = Label(window, text="")
# result_label.pack()
#
# # Create and configure check button
# check_button = Button(window, text="Check", command=check_armstrong)
# check_button.pack()
#
# # Start the Tkinter main loop
# window.mainloop()

# import tkinter as tk
# from tkinter import ttk, messagebox
# import mysql.connector
# from tkinter import *
#
# def GetValue(event):
#     e1.delete(0, END)
#     e2.delete(0, END)
#     e3.delete(0, END)
#     e4.delete(0, END)
#     row_id = listBox.selection()[0]
#     select = listBox.set(row_id)
#     e1.insert(0, select['id'])
#     e2.insert(0, select['empname'])
#     e3.insert(0, select['mobile'])
#     e4.insert(0, select['salary'])
#
#
# def Add():
#     studid = e1.get()
#     studname = e2.get()
#     coursename = e3.get()
#     feee = e4.get()
#     mysqldb = mysql.connector.connect(host="localhost", user="root", password='root', database="payroll_PYT65")
#     mycursor = mysqldb.cursor()
#
#     try:
#         sql = "INSERT INTO registration (id, empname, mobile.salary) VALUES (%s, %s, %s, %s)"
#         val = (studid, studname, coursename, feee)
#         mycursor.execute(sql, val)
#         mysqldb.commit()
#         lastid = mycursor.lastrowid
#         messagebox.showinfo("information", "Employee inserted successfully")
#         e1.delete(0, END)
#         e2.delete(0, END)
#         e3.delete(0, END)
#         e4.delete(0, END)
#         e1.focus.set()
#     except Exception as e:
#         print(e)
#         mysqldb.rollback()
#         mysqldb.close()
#
#
# def update():
#     studid = e1.get()
#     studname = e2.get()
#     coursename = e3.get()
#     feee = e4.get()
#     mysqldb = mysql.connector.conncet(host="localhost", user="root", password='root', database="payroll PYT65")
#     mycursor = mysql.cursor()
#
#     try:
#         sql = "Update registration set empname= %s, mobile= %s, salary=%s where id= %s"
#         val = (studname, coursename, feee, studid)
#         mycursor.execute(sql, val)
#         mysqldb.commit()
#         lastid = mycursor.lastrowid
#         messagebox.showinfo("information", "Record Updateddddd successfully...")
#
#         e1.delete(0, END)
#         e2.delete(0, END)
#         e3.delete(0, END)
#         e4.delete(0, END)
#         e1.foucs_set()
#
#     except Exception as e:
#         print(e)
#         mysqldb.rollback()
#         mysqldb.close()
#
#
# def delete():
#     studid = e1.get()
#
#     mysqldb = mysql.conncetor.connect(host="localhost", user="root", password="root", database="payroll_PYT65")
#     mycursor = mysqldb.cursor()
#
#     try:
#         sql = "delete from registration where id = %d"
#         val = (studid,)
#         mycursor.execute(sql, val)
#         mysqldb.commit()
#         lastid = mycursor.lastrowid
#         messagebox.showinfo("information", "Record Deleteeeee successfully...")
#
#         e1.delete(0, END)
#         e2.delete(0, END)
#         e3.delete(0, END)
#         e4.delete(0, END)
#
#     except Exception as e:
#         print(e)
#         mysqldb.rollback()
#         mysqldb.close()
#
#
# def show():
#     mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="payroll_pyt65")
#     mycursor = mysqldb.cursor()
#     mycursor.execute("SELECT id,empname,mobile,salary FROM registration")
#     records = mycursor.fetchall()
#     print(records)
#
#     for i (id, stname, course, fee) in enumerate(records, start=1):
#         listBox.insert("", "end", values=(id, stname, course, fee))
#         mysqldb.close()
#
#
# root = Tk()
# root.geometry('800x500')
# global e1
# global e2
# global e3
# global e4
#
# tk.label(root, text="Employee Registration", fg="red", font=(None, 30)).place(x=300, y=5)
#
# tk.Label(root, text="Employee ID").place(x=10, y=10)
# Label(root, text="Employee Name").place(x=10, y=40)
# Label(root, text="Mobile").place(x=10, y=70)
# Label(root, text="Salary").place(x=10, y=70)
#
# e1 = Entry(root)
# e1.place(x=140, y=10)
#
# e2 = Entry(root)
# e2.place(x=140, y=40)
#
# e3 = Entry(root)
# e3.place(x=140, y=70)
#
# e4 = Entry(root)
# e4.place(x=140, y=100)
#
# Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
# Button(root, text="update", command=update, height=3, width=13).place(x=140, y=130)
# Button(root, text="Delete", command=delete, height=3, width=13).place(x=250, y=130)
#
# cols = ('id','empname', 'mobile', 'salary')
# listBox = ttk.Treeview(root, columns=cols, show="headings")     # like columns
#
# for col in cols:
#     listBox.heading(col, text=col)
#     listBox.grid(row=1, column=0, columnspan=2)
#     listBox.place(x=10, y=200)
#
# show()
# listBox.bind('<Double+Button+1>' GetValue)  #double click on blue line highlight for getting value
#
# root.mainloop()

# from tkinter import *
#
# def btnClick(number):
#     global val
#     val = val + str(number)
#     data.set(val)
#
#
# def btnClear():
#     global val
#     val = ""
#     data.set("")
#
#
# def btnEqual():
#     global val
#     result = str(eval(val))
#     print(result)
#     data.set(result)
#
#
# root = Tk()
# root.title("Calculator")
# root.geometry('361x381+500+200')
# val = ""
# data = StringVar()
# display = Entry(root, textvariable=data, bd=29, bg="Powder blue", justify="right", font=("Arial", 20))
# # Border
# display.grid(row=0, columnspan=4)
#
# # First row
# btn7 = Button(root, text="7", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(7))
# btn7.grid(row=1, column=0)
#
# btn8 = Button(root, text="8", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(8))
# btn8.grid(row=1, column=1)
#
# btn9 = Button(root, text="9", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(9))
# btn9.grid(row=1, column=2)
#
# btn_add = Button(root, text="+", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('+'))
# btn_add.grid(row=1, column=3)
#
# #############
#
# btn4 = Button(root, text="4", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(4))
# btn4.grid(row=2, column=0)
#
# btn5 = Button(root, text="5", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(5))
# btn5.grid(row=2, column=1)
#
# btn6 = Button(root, text="6", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(6))
# btn6.grid(row=2, column=2)
#
# btn_sub = Button(root, text="-", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick('-'))
# btn_sub.grid(row=2, column=3)
#
# ##############
#
# btn1 = Button(root, text="1", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(1))
# btn1.grid(row=3, column=0)
#
# btn2 = Button(root, text="2", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(2))
# btn2.grid(row=3, column=1)
#
# btn3 = Button(root, text="3", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(3))
# btn3.grid(row=3, column=2)
#
# btn_mul = Button(root, text="*", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("*"))
# btn_mul.grid(row=3, column=3)
#
# ##############
#
# btnc = Button(root, text="C", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=btnClear)
# btnc.grid(row=4, column=0)
#
# btn0 = Button(root, text="0", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick(0))
# btn0.grid(row=4, column=1)
#
# btn00 = Button(root, text="00", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("00"))
# btn00.grid(row=4, column=2)
#
# btn_eql = Button(root, text="÷", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=btnEqual)
# btn_eql.grid(row=4, column=3)
#
# ################
#
# btn_back = Button(root, text="<-", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("<-"))
# btn_back.grid(row=5, column=0)
#
# btn_per = Button(root, text="%", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("%"))
# btn_per.grid(row=5, column=1)
#
# btn_div = Button(root, text="÷", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnClick("÷"))
# btn_div.grid(row=5, column=2)
#
# btn_eql = Button(root, text="=", font=("Arial", 12, "bold"), bd=12, height=2, width=6, command=btnEqual)
# btn_eql.grid(row=4, column=3)
#
#
# root.mainloop()

#############################

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select["id"])
    e2.insert(0, select["empname"])
    e3.insert(0, select["mobile"])
    e4.insert(0, select["salary"])


def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    fee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="pyt71A")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO registration (id,empname,mobile,salary)VALUES (%s,%s,%s,%s)"
        val = (studid, studname, coursename, fee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Employee Added Successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus.set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    fee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="Pyt71A")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update registration set empname=%s,mobile=%s,salary=%s,where id=%s"
        val = (studname, coursename, fee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record updated successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus.set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="Pyt71A")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from registration where id =%s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record deleted successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus.set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="Pyt71A")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,empname,mobile,salary FROM registration")
    records = mycursor.fetchall()
    print(records)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mysqldb.close()


root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root, text="Employee\nRegistration", fg="Red", font=(None, 30)).place(x=400, y=5)

tk.Label(root, text="Employee ID").place(x=10, y=10)
Label(root, text="Employee Name").place(x=10, y=40)
Label(root, text="Mobile").place(x=10, y=70)
Label(root, text="Salary").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="update", command=update, height=3, width=13).place(x=140, y=130)
Button(root, text="delete", command=delete, height=3, width=13).place(x=250, y=130)

cols = ("id", "empname", "mobile", "salary")
listBox = ttk.Treeview(root, columns=cols, show="headings")

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>', GetValue)  # double click on blue line highlight for getting value
root.mainloop()
