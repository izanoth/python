import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import *
import os
from typing import Optional
import re

# Init db object, singleton pattern restricts multiple objects per db
db = sqlite3.connect("C:\Program Files\sqlite\compras.db")
print('................\n')
print("DEBUG\n")
print(db)
# Connect to db and creates execution thread
print('................\n\n')

dir(db.cursor())

cursor = db.cursor()

cursor.execute("""
               select * from pendentes;
               """)

res = cursor.fetchall()

df = pd.read_sql_query("SELECT * FROM sqlite3 WHERE type='table'", db)

root = tk.Tk()
root.geometry("800x600")
root.fontePadrao = ("Arial", "10")
root["pady"] = 15
w = 800
h = 600
screenw = root.winfo_screenwidth()
screenh = root.winfo_screenheight()
xLeft = int((screenw/2) - (w/2))
yTop = int((screenh/2) - (h/2))
root.geometry("+{}+{}".format(xLeft, yTop))

Main = Frame(root)
Main.pack()

logo = Label(Main, text="Compras")
logo["font"] = ("Arial", "22", "bold")
logo.pack()

listboxA = Listbox(root, font=("Arial", "12"), width=70)

for i in df:
    listboxA.insert(tk.END, i)

listboxA.pack()

widget1 = Frame(Main)
widget1["pady"] = 10
widget1.pack()  

footer = Frame(root)
footer.pack(side=tk.BOTTOM)
Quit_button = Button(footer)
Quit_button["text"] = "Sair"
Quit_button["font"] = ("Calibri", "12")
Quit_button["width"] = 22
Quit_button["command"] = root.quit
Quit_button.pack()

Selection_button = Button(footer)
Selection_button["text"] = "Proceder"
Selection_button["font"] = ("Calibri", "12")
Selection_button["width"] = 22
Selection_button["bg"] = 'GREEN'
Selection_button["command"] = Main.destroy()
Selection_button.pack()



root.mainloop()

# Create test db and specify columns
#db.create_table("test", ["foo", "bar"])
# insert
#db.insert("test", {"foo": "foo", "bar": "bar"})
# update
#db.update("test", {"foo": "fooo", "bar": "baar"}, "1 = 1")
# delete
#db.delete("test", "1 == 1")
# select all
#db.select("test")
# conditional select
#db.select("test", columns=['foo'], condition='foo = "fooo"')
# custom query
#db.execute(...)

db.close()