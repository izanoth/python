#SRC_Data 01-06-21
#by Ivan Zanoth

import tkinter as tk
from tkinter import *
import os
from typing import Optional
import re

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

logo = Label(Main, text="SRC_String")
logo["font"] = ("Arial", "22", "bold")
logo.pack()

widget1 = Frame(Main)
widget1["pady"] = 10
widget1.pack()    

title = Label(widget1, text="(d 'mounth')")
title["font"] = ("Arial", "8", "bold")
title.pack(side=LEFT)
bit = Label(widget1, text="string")
bit["font"] = ("Arial", "8", "bold")
bit.pack(side=RIGHT)

datevar = tk.StringVar()
strvar = tk.StringVar()
ddatevar = Entry(widget1, validate='focusout', textvariable=datevar).pack(side=LEFT)
stringvar = Entry(widget1, validate='focusout', textvariable=strvar).pack(side=RIGHT)

def check_entry(index, value, op):
    listboxA.delete(0,tk.END)
    def engine(input, pth):
        global listboxA
        op_file = open(file=pth, mode='r', encoding='utf8')
        lines = op_file.readlines()
        for i in lines:
            if re.search(input, i):
                listboxA.insert(tk.END, pth.split('/')[-1]+' '+i)
            else:
                continue
        
    def gear(value, pth=None):
        if pth:
            for i in os.listdir('logs'+str(pth)):
                if os.path.isfile('logs/'+str(pth)+'/'+i):
                    engine(value, 'logs'+pth+'/'+i)                    
                else:
                    gear(value,'/'+str(i))
        else:
            for i in os.listdir('logs'):
                if os.path.isfile('logs/'+i):
                    engine(value, 'logs/'+i)                
                else:
                    gear(value,'/'+str(i))

    if datevar.get():
        gear(datevar.get())
    if strvar.get():
        gear(strvar.get())

datevar.trace('rw', check_entry)
strvar.trace('rw', check_entry)

listboxA = Listbox(root, font=("Arial", "12"), width=70)
listboxA.pack()

footer = Frame(root)
footer.pack(side=tk.BOTTOM)
Quit_button = Button(footer)
Quit_button["text"] = "Sair"
Quit_button["font"] = ("Calibri", "12")
Quit_button["width"] = 22
Quit_button["command"] = root.quit
Quit_button.pack()

root.mainloop()
