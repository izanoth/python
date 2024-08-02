import tkinter as tk
from tkinter import *

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

widget1 = Frame(Main)
widget1["pady"] = 10
widget1.pack()    

root.mainloop()