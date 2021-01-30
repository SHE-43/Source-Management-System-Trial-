# Have a username and password
# Upon passing, the buttons become enabled.
# Upon not passing, the buttons stay disabled and then we can try again later.


# Just make an admin window

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style
from tkinter import font
# import pymysql
import pandas as pd, os, sys, glob, codecs, pickle, time


class AdminWindow:

    def __init__(self, root):
        
        self.root = root
        self.root.geometry("200x300")
        self.root.title("Log in")
        self.frame = Frame(self.root)
        self.frame.pack()

        b = Button(self.frame, command = self.button_press)
        b.pack()

        self.var1 = IntVar()
        # self.bg = PhotoImage(file = pic_file)

        c1 = Checkbutton(self.root, text='Python',variable=self.var1, onvalue=1, offvalue=0)#, command=print_selection)
        c1.pack()

    def button_press(self):
        print(self.var1.get())



root = Tk()
obj = AdminWindow(root)
root.mainloop()





