def sprint_backlog(greeting = ["Hey, Fuck you!!!", "I am tired", "I am happy", " I am neutral", "I don't care", "Ily a bit", "I LOVE YOU MAN",
    "stop banging my keys!!!"]):
    import random as rd
    a = rd.choice(greeting).strip() + "!"
    print(a)
    return a
    # The OOP with 2 classes if possible. (inheritance where the 2nd class calls another window as class is another window as well) - Try this one.
    # Use global so that labels in methods are read
    # We could disable the button if a new window is open at that moment.
    # Make an OOP bank management system in Python and Java that acts liek the backend of a front end CRM system.
    # If 5 are added continuously, then add another one
    # Make sure there are no more than one copy of an entry in this.
    # Create a checkbox that enables or disables a button for us.
    # FOR THIS ONE, START PUTTING THESE IN SEPARATE PYTHON FILE TO MAKE THEM NEAT - CLASS FOR ADD, SETTING MENU, VIEW PROFILE (essentially, hover makes new toplevel)
    # Fake data generator gives option to save as retrieve either as JSON, excel, csv, notepad, list as csv, a dict as pickle, pickle or sql.
            # Have this ready before the end of today.
    
    # Graphs option to show multiple projections - Past, Future, Present, Bar, Line, Pie, Scatter, One with many on them.
    # A local map to color as per number of accounts opened.
    # 

    # THE DESING SHOULD BE AMAZING!

    # What is sticky and NW
    # Bind commands to message box?
    # Have a help menu or option just like in normal softwares
    # Make an admin entry before this begins - show or hide buttons upon entry - have manager and employee sections binded to buttons
            # loading screen - just for fun
            # hide the password entry or make it astericks
            # Warning sounds - from Pygame
            # Hover over treeview to show something - profile pics or avatar
            # Have option register yourself - that being the third option on admin screen so that they don't have to put user or password;
            # The employee can register himself - dob as calendar only or an updown arrow keys to increase or decrease value of day/month/year with limits of course
            # file explorer that is opened when you want to save as or just look for something
            # attach the MS Calculator and your own with it so they both can be used to make changes.
    # BIG DATA: Fake data generator will launch as separate file and on pressing commit, it will reset the original back up file by saving that somewhere else
            # making this new one the sole back up file from where the dataframe launches and makes treeee. Also, fake data generator will follow rules of the
            # data frame we make at the beginning of the file
    # Change font, background, but permanently please.
    # Save most of the changeable data in a back up file.
    # Keep a log of everytime something is done on this program/application - just for the sake of it. 
    # WE ARE SHOWING OFF!
    # PAths can be changed easily or obtained from a file menu or the algorithm written for the datascience Jupyter file - unique on that goes back and forth
    # make a listview option as well so that we can try to map certain data points to know what to save in our self made SQL database of all data
    # This will have a unique purpose - either a bank account (but do OOP on that first please and use data structures for each element sved recursilvely)
        # a cellular service provider's CRM
        # a bank's crm
        # look for other ideas
        # when adding a new product for the customer, have the option to populate certain items automatically, use tick boxes for stuff like 
                    # enable mobile or internet banking (even if it is just for the showcasing purpoooose (indian/pak accent))
        
    # YESSS! if it kicks your ass in speed, make a recursive tree that sprouts the tree upon loading the data from excel or sql - ADVANCED SHIT
    # MACHINE LEARNING - what is the customer's balance in savings with this rate - tick boxes for other aspects that can affect.
        # Other savings accounts which can, on pressing one button, populate the whole 12 month plan showing each month according to AH's amount and our IR
        # AH = Account Holder, IR - Interest Rate
        # NLP to locate certain transactions from the customer's account
        # Neural Network to determine differences in fraudulent Tesco and real Tesco (TESCOEXPRESS2150 vs. TESCO STORE TRANSACTION)
                    # Remember one as legit and the other as NOT!
        # When will the customer be out of balance according to an average of upcoming transactions in terms of spending habits, trends,
        # Savings rates affected according to average of 



from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style
import pandas as pd, os, sys, glob, codecs, pickle

dict_ = {
    "path_1" : r"C:\Users\ABC\Desktop\JOB 2020\Source-Management-System-Trial--main\Source-Management-System-Trial--main",
    "path_2" : r"C:\Users\ABC\Desktop\JOB 2020\Source-Management-System-Trial--main\Source-Management-System-Trial--main\excel_test_files",
    "main_excel_file" : r"C:\Users\ABC\Desktop\JOB 2020\Source-Management-System-Trial--main\Source-Management-System-Trial--main\excel_test_files\main_excel.xlsx"
}

main_current_path = r"C:\Users\ABC\Desktop\JOB 2020\Source-Management-System-Trial--main\Source-Management-System-Trial--main\excel_test_files\main_excel.xlsx"

df = pd.DataFrame(columns=list(("first", "second", "third", "FOURTH",)))

# Creates a new folder.
if not os.path.exists(dict_["path_1"]):
    os.path.makedirs(dict_["path_2"])

class forRoot2:
    def __init__(self, root_):
        self.root = root_
        self.root.title("Second Window")
        self.root.geometry("200x400+400+200")

        self.frame2 = Frame(self.root)
        self.frame2.pack()
        
        self.first = StringVar()
        self.second = StringVar()
        self.third = StringVar()
        self.fourth = StringVar()

        list_1 = [self.first, self.second, self.third, self.fourth]
        
        self.labelEntry1 = Label(self.frame2, text = "First").grid(row=0, column=0)
        self.labelEntry2 = Label(self.frame2, text = "Second").grid(row=1, column=0)
        self.labelEntry3 = Label(self.frame2, text = "Third").grid(row=2, column=0)
        self.labelEntry4 = Label(self.frame2, text = "Fourth").grid(row=3, column=0)

        self.c = 2

        self.entry1 = Entry(self.frame2, textvariable = self.first).grid(row=0, column=self.c)
        self.entry2 = Entry(self.frame2, textvariable = self.second).grid(row=1, column=self.c)
        self.entry3 = Entry(self.frame2, textvariable = self.third).grid(row=2, column=self.c)
        self.entry4 = Entry(self.frame2, textvariable = self.fourth).grid(row=3, column=self.c)    

        self.buttonSend = Button(self.frame2, text = "Send", command = self.print_the_tree)
        self.buttonSend.grid(row= 5, column=0)
        self.buttonExit = Button(self.frame2, text = "Exit", command = self.root.destroy).grid(row= 5, column=1)

    def printAllVars(first, second, third, fourth):
        list_of_vars = [first.get(), second.get(), third.get(), fourth.get()]
        print(list_of_vars)

    def print_the_tree(self): # Method for send only)
        global df
        L = [self.first.get(),self.second.get(),self.third.get(),self.fourth.get()]
        treeView1.insert("", END, values = L)
        series_ = pd.Series(L, list(("first", "second", "third", "FOURTH",)))
        print(series_)
        df = (df.append(series_, ignore_index=1))
        warningMessage = messagebox.showwarning("Not saved", "Latest data input not saved to any back up file.")
        helpMessage = messagebox.askquestion("How to save!", "Click below to learn how to save, you muggg!")
        

def launchSettingsMenu(class_ = "You could make one for more options"):
    pass

def launchRoot2(class_):
    global root2
    # Send a text line to the entry box to see if it gets a number without 0 or not.
    try:
        if root2.state() == "normal":
            root2.focus()
    except NameError as e:
        root2 = Toplevel()
        class_(root2)
        
    except TclError as T:
        root2 = Toplevel()
        class_(root2)

def launchSettings():
    # Could make a dynamic class like we do in Java
    # Or have a separate class in a separate file if you want.
    global settingsMenu
    try:
        if settingsMenu.state() == "normal":
            settingsMenu.focus()
    except NameError as e:
        print(e)
        settingsMenu = Toplevel()
        settingsMenu.geometry("300x300+750+200")
        settingsMenu.mainloop()
    except TclError as T:
        print(T)
        settingsMenu = Toplevel()
        settingsMenu.geometry("300x300+750+200")
        settingsMenu.mainloop()


def print_df():
    '''
    This gets the df for us.
    '''
    global df
    print(df)

def save_treeview(df, path):
    writer = pd.ExcelWriter(path)
    df.to_excel(writer, index = False)
    writer.save()
    
    # This saves the dataframe to the same excel file

def save_as_treeview():
    # This takes in a new link to save the treeview
    # Have the option to make a save as file explorer
    # Or just take in a new link for now.
    pass

def reset_file():
    # This deletes and creates a new file for us
    pass

def settings_font():
    # Create s pickle file that saves font settings.
    # We can change them by creating a box that can select multiple using radiobuttons
    # Tick box for italics and bold
    # This applies to entry boxes as well.
    pass

def open_root_file_method(df):
    print("""
    
    """)
    print(df)
    print("""
    
    """)



root = Tk()
root.title("Data Manager")
root.geometry("300x300")

buttonSizes = {"height" : 1, "width": 5}

frameButtons = Frame(root, bg = "red", bd = 5)
frameButtons.pack()

buttonDel = Button(frameButtons, text = "Delete", bg = "blue", fg = "white", **buttonSizes)
buttonDel.pack(side = LEFT, fill=X)

buttonUpdate = Button(frameButtons, text = "Update", bg = "blue", fg = "white", **buttonSizes)
buttonUpdate.pack(side=RIGHT, fill=X)
buttonUpdate["state"] = "disabled"

buttonAdd = Button(frameButtons, text = "Add", bg = "blue", fg = "white", command = lambda :  launchRoot2(forRoot2),  **buttonSizes)
buttonAdd.pack(side = LEFT, fill=X)

buttonExit = Button(frameButtons, text = "Exit", bg = "blue", fg = "white", command = root.destroy, **buttonSizes)
buttonExit.pack(side=RIGHT, fill=X)

buttonDF = Button(frameButtons, text = "Print DF", bg = "blue", fg = "white", command = print_df, **buttonSizes)
buttonDF.pack(side=RIGHT, fill=X)


# Have color change upon hover for the menuBar tabs - A stronger grey
menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Save", command = lambda : save_treeview(df, r"C:\Users\ABC\Desktop\JOB 2020\Source-Management-System-Trial--main\Source-Management-System-Trial--main\excel_test_files\main_excel.xlsx"))
fileMenu.add_command(label="Save As") # , command = save_treeview)
fileMenu.add_command(label="Open Root File" , command = lambda : open_root_file_method(df))
fileMenu.add_command(label="Settings", command = launchSettings) # This must be greyed out

# This opens a new window which of course cannot be shut as well.
menuBar.add_cascade(label="File", menu = fileMenu)
root.config(menu = menuBar)

# Create hover
# Change color on hover
# Open something on treeview hover
# Right click menu on treeview
# Menu option that saves the table.

frameTreeView = Frame(root, bg = "red", bd = 5)
frameTreeView.pack()

scroll_x = Scrollbar(frameTreeView, orient= HORIZONTAL)
scroll_y = Scrollbar(frameTreeView, orient = VERTICAL)

scroll_x.pack(side=TOP, fill = X)
scroll_y.pack(side=RIGHT, fill = Y)

treeView1 = ttk.Treeview(frameTreeView, show = "headings", columns = ("first", "second", "third", "FOURTH"), 
xscrollcommand = scroll_x.set, 
yscrollcommand = scroll_y.set)

scroll_x.config(command = treeView1.xview)
scroll_y.config(command = treeView1.yview)

col = treeView1["columns"]

for c in col:
    treeView1.heading(c, text = c)
    treeView1.column(c, width = 50)
    
treeView1.pack()



print(dir(fileMenu))

root.mainloop()





















"""
Hi there,

I am going to quickly say helo to everyone here in my circle.

The application I am trying to work on is actually quite an easy one as it includes very basic functionality and is made entirely using Tkinter GUIs.


What I really want to do is use Binary Search Trees and give it a GUI. The algorithms used to write BST scripts are so complicated yet I am so interested in
making them right here right now that I cannot wait. There are so many data structures that I've read about but only a few I remember coding myself. I want to
build more.

There is a heap that is a straightforward array type structure. Then we have an array itself. Then come the Binary Search Trees and the B trees. We move on
to discussing the Big O notation for these structures. 



Finally, I want them to be what store the data in the background whilst using my GUI front end. Is it true that I may only want to build GUIs. There is so
much more I'd like to do with machine learning, deep learning, NLP and neural networks that I do not even know where to begin. I am so far behind from so
many people that I get discouraged every now and then. In fact, I am getting discouraged every other second. I've wasted about the whole of last 2 days,
entirely. 


Thus, I'd like to end this right now and start working on these right away.

Loads of luck and love to you all.


Respectfully yours,


Hamza   S    Malik
GO!!! GO!!! GO!!!


P.S. It takes me a long time to even go over simple ass topics. Something like data structures just gets overwhelming and that is all.
    My mission, however, is to learn them all and start making my own scripts as soon as I possibly can. This way, I can grasp the one
    and only concept being used to connect recursion with data storage. 

    It recursively creates a new object and stores it with a right and/or left value. That is it.

    Let's make one, right now.

"""