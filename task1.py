import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("task1")
window.geometry("400x400")
window.resizable(False,False)

entry1 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
lable1 = tk.Label(window, text="X")
entry2 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)
lable2 = tk.Label(window, text="=", borderwidth=1, relief=SUNKEN)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)







entry1.grid(row=1, column = 1, columnspan=1)
lable1.grid(row = 1, column = 2)
entry2.grid(row=1, column = 3, columnspan=1)
lable2.grid(row = 1, column = 4)
entry3.grid(row=1, column = 5, columnspan=1)

window.mainloop()