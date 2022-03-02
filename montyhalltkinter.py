import tkinter as tk
from tkinter import *

root = tk.Tk()

w = Canvas(root, width=250, height=200)
w.create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')
w.create_rectangle(100, 100, 0, 0, fill="red", outline = 'blue') 
w.pack()

root.mainloop()