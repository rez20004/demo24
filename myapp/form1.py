# from django import forms
from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title('form')


Fullname = StringVar()


def database():
    name1 = Fullname.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS student (Fullname TEXT)')
        cursor.execute('INSERT INTO student (Fullname) VALUES(?)', (name1,))
        conn.commit()


label_0 = Label(root, text ="Registration Form", width=20, font=("bold",20))
label_0.place(x=90, y=53)
label_1 = Label (root, text="Fullname", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=240, y=130)
list = ['test', 'place']
c = StringVar()
droplist = OptionMenu(root, c, *list)
droplist.config(width=15)
c.set('select')
droplist.place (x=240, y=280)

Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=250, y=230)

root.mainloop()








