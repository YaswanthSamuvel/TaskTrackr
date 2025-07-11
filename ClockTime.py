import tkinter as ttk
from tkinter import *

from time import strftime

win=Tk()
win.geometry('710x150')
win.title("CLOCK")

def time():
    l=Label(win,font=('ds-digital',80),bg='black',fg='cyan')
    string=strftime(' %H:%M:%S %a')
    l.config(text=string)
    l.after(1000,time)
    l.place(x=10,y=10)

time()

win.mainloop() 