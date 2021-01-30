# A plug for the system_main.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style
from tkinter import font
# import pymysql
import pandas as pd, os, sys, glob, codecs, pickle, time



# def run_window():
#     r = Toplevel()
#     print(r.state())
    
def progress(currentValue, progressbar):
    progressbar["value"]=currentValue


class PasswordWindow:

    # this needs to be a pickle file and can be updated as well through the settings menu.
    password_ = "123"

    def __init__(self, root, method, deny_method, MAINROOT = 0):
        self.MAINROOT = MAINROOT
        self.method = method;
        self.deny_method = deny_method;
        self.root = root
        self.root.title("Enter Password")
        self.root.geometry("200x400+400+200")
        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.progressbar=ttk.Progressbar(self.root,orient="horizontal",length=300,mode="indeterminate") # or determinate
        self.progressbar.pack(side=TOP)

        currentValue = 10
        self.progressbar["value"]=currentValue
        self.progressbar["maximum"]=100

        # 10 times, 
        divisions=9
        for i in range(divisions):
            currentValue=currentValue+10
            self.progressbar.after(200, progress(currentValue, self.progressbar)) # after 200 secon
            self.progressbar.update() # Force an update of the GUI


        self.first = StringVar()

        self.label1 = Label(self.frame1, text = "Enter Password").pack()
        self.label2 = Label(self.frame1, text = "Attempts left").pack()
        self.label3 = Label(self.frame1, text = "3")
        self.label3.pack()
        self.entry1 = Entry(self.frame1, textvariable = self.first, show="*").pack()

        self.buttonSend = Button(self.frame1, text = "Send", command = self.checkPassword).pack()

        if MAINROOT == 0:
            self.buttonExit = Button(self.frame1, text = "Exit", command = self.root.destroy).pack()
        else:
            self.buttonExit = Button(self.frame1, text = "Exit", command = self.MAINROOT.destroy).pack()

        self.root.mainloop()
    counter = 0
    def checkPassword(self):
        if self.first.get() == PasswordWindow.password_: # if password matches
            print("MATCHES") 
            self.root.destroy() # close the password window
            self.method() # run the method that we want to run - this is entered in the class we made.
            PasswordWindow.counter = 0
            return True
        else:
            PasswordWindow.counter += 1
            if PasswordWindow.counter >= 3:
                self.root.destroy()
                PasswordWindow.counter = 0
                # messagebox.showerror("OVER", "OVER!!!")
            else:
                # self.root.destroy()
                self.label3.config(text = f"{str(3 - PasswordWindow.counter)}")
                # self.deny_method() # Each time there is a fail attempt, this method runs.
                self.root.focus()

def m(MAINROOT, c, m1, m2):
    root1 = Toplevel()
    c(root1,m1,m2,MAINROOT)


def launch_window(class_, m1, m2):
    global root1
    global root
    try:
        if root1.state() == "normal":
            root1.focus()
    except NameError as n:
        m(root, PasswordWindow, m1,m2)
    except TclError as t:
        m(root, PasswordWindow, m1,m2)
    # except:
        # root1 = Toplevel()
        # class_(root1, m1, m2)

def method1():
    global root
    messagebox.showinfo("YES")
    # root.destroy()
def method2():
    global root
    messagebox.showinfo("NO")
    # root.destroy()

if __name__ == '__main__':
    root = Tk()
    
    launch_window(PasswordWindow, method1, method2)