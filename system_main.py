from tkinter import *
from tkinter import ttk
import pymysql
import pandas as pd, os, sys, glob



class Student:

    def __init__(self, root, df1):
        if os.path.exists(r"\\ukdfs.mintecglobal.com\User\Redirect\Hamza.Malik\Desktop\My Python\School Management System\SMS.xlsx"):
            df1 = pd.read_excel(r"\\ukdfs.mintecglobal.com\User\Redirect\Hamza.Malik\Desktop\My Python\School Management System\SMS.xlsx")
            self.df1 = df1
        else:
            self.df1 = df1

        # ROOT 
        self.root = root
        self.root.title("Series Manager (SM V2.1)")
        self.root.geometry("1300x500+100+20")
        self.root.state("zoomed") # This makes sure that it is always launched in full screenmode.

        # LABEL FOR ROOT
        title = Label( # This adds a label with a window
            self.root, text = "Series Management", 
            font= ("Sans-Serif",40, "bold"), 
            bg= "Dark Grey", 
            fg = "Crimson",
            bd=12, # Border width
            relief=FLAT) # must be flat, groove, raised, ridge, solid, or sunken
        title.pack(side=TOP, fill = X)
        
        
        # StringVars to collect string data from entry.
        self.Roll_No_var = StringVar() # these are to be added in the entry object as textvariable
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()



        # MANAGE_FRAME MANAGE_FRAME MANAGE_FRAME
        # MANAGE_FRAME MANAGE_FRAME MANAGE_FRAME
        Manage_Frame = Frame(self.root, bd=2, relief=FLAT, bg = "Dark Grey") # FLAT RAISED SUNKEN GROOVE RIDGE
        Manage_Frame.place(x=10, y=100, width= 450, height=690)
        # Manage_Frame.grid_columnconfigure(1, weight=2) # this is used to centre the label.        
        


        # MAIN LABEL - MANAGE FRAME
        font_labels = ("Sans-serif", 25, "bold")
        Manage_Frame_Label = Label(Manage_Frame, text = "Manage", font = font_labels, bg = "Dark Grey" , fg= "White", relief = FLAT, bd=1.1)
        Manage_Frame_Label.grid(row = 0, columnspan = 2, column = 0, pady = 20, padx= 20)
        d = { "bg" : "Dark Grey" ,"fg": "Black", "relief" : FLAT, "bd":1.1} # done with a dictionary.


        # FONTS
        font_labels = ("Sans-serif", 15, "bold")
        font_entry = ("Sans-serif", 15)



        # Labels and Entries.

        # ROLL NUMBER - L
        Roll_Number_Label = Label(Manage_Frame, text = "Source ID", font = font_labels,       **d)
        Roll_Number_Label.place(x=5, y = 82)
        # Roll_Number_Label.grid(sticky="w") # w = west

        # ROLL NUMBER - E
        text_entry_roll_number = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.Roll_No_var)
        text_entry_roll_number.place(x = 140, y = 77)


        # NAME - L
        Name_Label = Label(Manage_Frame, text = "Name", font = font_labels,       **d)
        Name_Label.place(x=5, y = 82+30)        

        # NAME - E
        text_entry = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.Name_var)
        text_entry.place(x = 140, y = 77+30)


        # EMAIL - L
        Email_Label = Label(Manage_Frame, text = "Location ID", font = font_labels,       **d)
        Email_Label.place(x=5, y = 82+30+30)        

        # EMAIL - E
        text_entry_email = Entry(Manage_Frame, font = font_labels, bd=1, relief = GROOVE, textvariable=self.Email_var)
        text_entry_email.place(x = 140, y = 77+30+30)


        # GENDER - L
        Gender_Label = Label(Manage_Frame, text = "Rationality", font = font_labels,       **d)
        Gender_Label.place(x=5, y = 82+30+30+30)   

        # GENDER - E (combobox)        
        combo_box_gender = ttk.Combobox(Manage_Frame, font = ("Sans-Serif", 12), state = "readonly", textvariable=self.Gender_var)     
        combo_box_gender['values'] = ("L", "M", "S")
        combo_box_gender.place(x = 140, y = 78+90, width = 225, height = 25)
        ### HAVE OPTION TO AUTOSELECT WHEN PRESSING AN ALPHABET.
        

        # CONTACT - L
        Contact_Label = Label(Manage_Frame, text = "Series count", font = font_labels,       **d)
        Contact_Label.place(x=5, y = 82+120)        

        # CONTACT - E
        text_entry_contact = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.Contact_var)
        text_entry_contact.place(x = 140, y = 77+120)


        # ADDRESS - L 
        Address_Label = Label(Manage_Frame, text = "Methodology", font = font_labels,       **d)
        Address_Label.place(x=5, y = 82+155)

        # ADDRESS - E
        self.text_entry_address = Text(Manage_Frame, width = 25, height = 4)
        self.text_entry_address.place(x = 140, y = 77+160)


        # DOB - L
        DOB_Label = Label(Manage_Frame, text = "Size", font = font_labels,       **d)
        DOB_Label.place(x=5, y = 82+250)

        # DOB - E (THREE COMBO BOXES)
        DOB_Entry = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.DOB_var)
        DOB_Entry.place(x = 140, y = 80+250) # Convert this to datetime object
        # But it must have a pick day month and year option too.
        # To be improved later.




        # BUTTON FRAME (within MANAGE FRAME) >>> total width of 450.
        button_manage_frame = Frame(Manage_Frame, bd=1, relief = RIDGE, bg = "Grey")
        button_manage_frame.place(x=25, y = 450)


        #BUTTON ADD
        button_manage_add = Button(button_manage_frame, bg = "Dark Grey", text="Add", width = 10, activebackground = "grey", command=self.add_students_to_dataframe)
        button_manage_add.grid(row=0, column = 1)# , padx = 7, pady = 13)
        #BUTTON  UPDATE
        button_manage_update = Button(button_manage_frame, bg = "Dark Grey", text="Update", width = 10, activebackground = "grey", command = self.save_to_excel)
        button_manage_update.grid(row=0, column = 2)# , padx = 7, pady = 13)
        ##BUTTON DELETE
        button_manage_delete = Button(button_manage_frame, bg = "Dark Grey", text="Delete", width = 10, activebackground = "grey")
        button_manage_delete.grid(row=0, column = 3)# , padx = 7, pady = 13)
        #BUTTON CLEAR
        button_manage_clear = Button(button_manage_frame, bg = "Dark Grey", text="Clear", width = 10, activebackground = "grey")
        button_manage_clear.grid(row=0, column = 4)# , padx = 7, pady = 13)

        label_author = Label(Manage_Frame, text = "Author: 'Hamza Malik'")
        label_author.place(x=15, y=650)

        

        font_labels = ("Sans-serif", 12)

        #DETAIL FRAME DETAIL FRAME DETAIL FRAME
        #DETAIL FRAME DETAIL FRAME DETAIL FRAME
        Detail_Frame = Frame(self.root, bd=1, relief=FLAT, bg = "Dark Grey") # BD = BORDER WIDTH
        Detail_Frame.place(x=525, y=95+5, width= 1000, height=690)


        #MAIN LABEL - DETAIL FRAME
        Detail_Frame_Label = Label(Detail_Frame, text = "Search", font = ("Sans-Serif", 25, "bold"), bg = "Dark Grey", fg= "White", relief = FLAT, bd=1.1)
        Detail_Frame_Label.grid(row = 0, columnspan=2, column=0, pady = 20, padx= 20, sticky="w") # column 2 and covers 2 and 3 thus next should be 4.

        #LOADING LABEL
        # loading_label_detail_frame = Label(Detail_Frame, text=)
        # Knowing when the data has now arrived or ready.
        # Maybe boolean stays false till data is downloaded, when it is ready, we can then mark it as true.


        #SEARCH BY - L
        search_by_label_detail_frame = Label(Detail_Frame, text="Search by", font = ("Sans-Serif", 15, "bold"), bg = "Dark Grey")
        search_by_label_detail_frame.grid(row=2, column = 0, padx = 20, pady= 20)
        
        #SEARCH BY - E (COMBO BOX)
        combo_box_search = ttk.Combobox(Detail_Frame, font = ("Sans-Serif", 15), state = "readonly")     
        combo_box_search['values'] = ("Source ID", "Name")
        combo_box_search.grid(row=2, column=3, padx= 10, pady=21)
        ### If nothing is chosen then present error - the error shall be printed back underneath this column.

        #SEARCH BY = E (ENTRY)
        search_by_entry = Entry(Detail_Frame, font=("Sans-serif", 15, "bold"), bd = 1, relief = GROOVE)
        search_by_entry.grid(row = 2, column = 1)



        # BUTTON FRAME - DETAIL FRAME (SEARCH BY FRAME)
        button_frame_detail_frame = Frame(Detail_Frame, bd=1, relief = RIDGE, bg = "Grey", height = 50, width = 380)
        button_frame_detail_frame.place(x = 450, y = 150)

        # BUTTONS - Button Frame - DETAIL FRAME
        search_button = Button(button_frame_detail_frame, text = "Search", bg = "Dark Grey", width = 10, activebackground = "grey").grid(row=0, column = 0)
        showAll_button = Button(button_frame_detail_frame, text = "Show All", bg = "Dark Grey", width = 10, activebackground = "grey").grid(row=0, column = 1)



        # TABLE FRAME - DETAIL FRAME - to place the Treeview object in.
        table_frame_detail_frame = Frame(Detail_Frame, bd=1, relief = GROOVE, bg = "Dark Grey")
        table_frame_detail_frame.place(x = 25, y= 200, height = 460, width = 950)

        # Making scroll bars - this way.
        # Make scrollbar objects and assign the orientation.

        scroll_x = Scrollbar(table_frame_detail_frame, orient=HORIZONTAL)       
        scroll_y = Scrollbar(table_frame_detail_frame, orient=VERTICAL)       
        
        # Pack them within the frame of choice.

        scroll_x.pack(side=BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill = Y)

        # Create a widget and place within a Frame, and set the xscrollcommand and yscrollcommand argument

        search_results_table = ttk.Treeview(
            table_frame_detail_frame, 
            show="headings",
            columns = ("Roll", "Name", "Email", "Gender", "Contact", "DOB", "Address"), # these columns are just for tags.
            xscrollcommand=scroll_x.set, 
            yscrollcommand=scroll_y.set)

        # Configure the scrollbars and set the command for them.
        scroll_x.config(command=search_results_table.xview)
        scroll_y.config(command=search_results_table.yview)

        search_results_table.heading("Roll", text = "Roll Number")
        search_results_table.heading("Name", text = "Name")
        search_results_table.heading("Email", text = "Email")
        search_results_table.heading("Gender", text = "Gender")
        search_results_table.heading("Contact", text = "Contact")
        search_results_table.heading("DOB", text = "DOB")
        search_results_table.heading("Address", text = "Address")


        for column in search_results_table['columns']:
            if column != "Email" and column != "Address":
                search_results_table.column(column, width = 143) # Loop to adjust the width of the system.
            else:
                search_results_table.column(column, width = 200) # Loop to adjust the width of the system.

        search_results_table.pack(fill=BOTH, expand=1) # This fills and expands till the end of it



    def add_students_to_dataframe(self):
        # conn = pymysql.connect(host="localhost", user="root", password="", database = "stm")
        # print(self.Roll_No_var.get()) # these are to be added in the entry object as textvariable
        # print(self.Name_var.get())
        # print(self.Email_var.get())
        # print(self.Gender_var.get())
        # print(self.Contact_var.get())
        # print(self.DOB_var.get())
        # print(self.text_entry_address.get('1.0',END))

        list143 = [self.Roll_No_var.get(),         
        self.Name_var.get(), 
        self.Email_var.get(), 
        self.Gender_var.get(), 
        self.Contact_var.get(), 
        self.DOB_var.get(), 
        self.text_entry_address.get('1.0',END)] # Issue with this line.

        series_ = pd.Series(list143, ["Roll No.", "Name", "Email", "Gender", "Contact", "DOB", "Address"], name="SERIES1" )
        series_ = series_.to_dict()
        
        self.df1 = self.df1.append(series_, ignore_index=1)
        self.df1.index = [x for x in range(1, len(self.df1 )+ 1)]

        print("\nThe series;\n")
        print(series_)
        print("\n... is now added to the following dataframe!\n")
        print(self.df1)




        # This method will be added to the Add Button
        # Have a way to commit the input of data.
        # If wrong, clear and start again.
        # Or, let it stay and then edit it.
        # For delete, have an 'are you sure' button.
        # First, find the record and then delete it.
        # Make modulare if you can. That is a challenge.
    # For this we need MySQL.
    # Or you could use a dataframe to add them and then add to Excel as well.

    def save_to_excel(self):
        path = r"\\ukdfs.mintecglobal.com\User\Redirect\Hamza.Malik\Desktop\My Python\School Management System\SMS.xlsx"
        writer = pd.ExcelWriter(path)

        self.df1.to_excel(writer)
        writer.save()
        
        
    def launch_file(self):
        # Can we launch file to see if it works?
        pass
    # Yes we can using os or sys.
    

df = pd.DataFrame(columns = ["Roll No.", "Name", "Email", "Gender", "Contact", "DOB", "Address"] )

root = Tk()
obj = Student(root, df)
root.minsize(900,750)
root.mainloop()


obj.add_students_to_dataframe()





# Can this be modular so that all sections are divided? Challenge 1.
# Ratta, Steps, Copy
# You need to first decide on your copy the type of store you need. Make a BLUEPRINT - Do this non-stop.
# CHANGE TO GRID MODE.
# Use itertools cycle.
# Make a SM in a way to show Mintec that we can change the way mapping works.
# Make a plan, please for design, wrangling, scraping, random generator option for names. 
# Have an option that runs to create fake data or uploads exisitng fake data.
# Try smaller versions inside module.
# HTML and SQL after this. Tkinter tutorial. C# (asp.net)
# C as well with advanced features too.
# What can I do with this?
# Have fake sales information added to a database that is created by another program - Excel Scraper
# Create an online store that this can be based on.
# Have a way to enter a new sale.
# Then, make a website that can be launched from within this.
# Add pandas tricks to this same thing.
# Copy all instructions from Project43 and the Left file
# Use grid, eventually.
# Introduce new item opens a new window
# Add sale should be on same and viewing sales for the month as well.
# More options open more windows however, integrate to C and make it faster.
# Use same concepts to make a wrangling, regex tool - matplotlib, reports, machine learning, future productions and stuff
# Please make it look good. Beautiful graphics. Like antivirus softwares, with curvy corners, colored edges, specific color
                # schemes, title color, perfect measurement and division.
# For that - you go for web design. .NET and ASP .NET.
# Make smaller window as fixed window only.
# Even when it is made bigger, it should stay in the middle.
# Learn the bindings first.
# Arrange by date, name or dob, up or down in treeview. 
# Desktop apps are fun to make and this is what I want to do forever and ever.
# Apache, node.js, vue.js, other servers, graphQL, amplify, mongoDB, mySQL, C#, C, C++, JS, HTML5.
# Make more from YouTube till you are comfortable with them yourself.
# Have loading label on the window.
# Tkinter full tutorial.