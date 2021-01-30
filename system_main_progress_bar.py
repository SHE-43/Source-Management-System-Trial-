


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style
from tkinter import font
# import pymysql
import pandas as pd, os, sys, glob, codecs, pickle, time
import system_main


# Either have this in the program;
# Or, run this first and then load the other one up.

class ProgressWindow:

    # This runs before the program runs and then closes down.

    def __init__(self, root):
        self.root = root
        self.root.geometry("400x70+500+350")
        self.root.title("Loading...")
        self.frame = Frame(self.root)
        self.frame.pack()
        self.loading_label = Label(text = "Loading main window...", bg = "dark grey")
        self.loading_label.pack(side=TOP)

        self.progressbar=ttk.Progressbar(self.frame,orient="horizontal",length=300,mode="determinate") #or indeterminate
        self.progressbar.pack(side=BOTTOM)

        currentValue = 10
        self.progressbar["value"]=currentValue
        self.progressbar["maximum"]=100

        # 10 times, 
        divisions=9
        for i in range(divisions):
            time_add = 1
            currentValue=currentValue+10
            if i == 7 or i == 6 or i == 3:
                time_add = 543
            else:
                time_add = 143
            self.progressbar.after(time_add, progress(currentValue, self.progressbar)) # after 200 secon
            self.progressbar.update() # Force an update of the GUI
        print(root.state())
        
        self.root.destroy()
        # self.run_application()
        
    def run_application(self):
        system_main.main()
  
def progress(currentValue, progressbar):
    progressbar["value"]=currentValue       
        

root = Tk()
obj = ProgressWindow(root)



        