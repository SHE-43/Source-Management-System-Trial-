# My main project for Birkbeck that we will improvise with a whole network so we understand how stuff works.
# Eventually, this will be a CRm software which you will then translate to Java, then Java Script, and then C++ and if you have more years, C.
# This may loook like an Excel form, but do not be fooled so undisputably.
# REQUIRED ENGINES FOR EXCEL
    # We need openpyxl
    # We need xlrd

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style
from tkinter import font
from system_main_password_window import PasswordWindow
import pandas as pd, os, sys, glob, codecs, pickle, time, types
# import pymysql
# from system_main_testing_outside_method_imports import test_button_2


    # https://www.youtube.com/watch?v=tUc6FMPSZDg&list=PL4P8sY6zvjk44vUpBQc7y-zlm_VAq5Abx&index=4
    # MORE EXAMPLES - ALSO, MAKE SURE VENV IS USED OR NOTE THE VERSIONS OF MODULES USED.

        #https://riptutorial.com/tkinter/example/22870/-after--
        # https://runestone.academy/runestone/books/published/thinkcspy/GUIandEventDrivenProgramming/03_widgets.html
        # https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Treeview.html
        # https://docs.python.org/3/library/tkinter.ttk.html
        # https://docs.python.org/3/library/tkinter.ttk.html#ttkstyling
        # https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style
            # This can be used to adjust after

        # Create admin page and have an option to not run it rhough that
        # Connect the loading screeen as well,
        # Make a menu bar and add save, save as and reset file over there
        # Make a help menu and add about 
        # tkinter Separator - add them to divide stuff.
        # Help where you can launch a readme window, about me and updates available or not
        # View settings and then save the setting - change font as well.
        # A window that has these options availabel like the one in the above link with sliders, font to choose from 
            # Change password
            # 
        # either divide postcode, first line and city
                # or have a entry box
                # this can be used to make a map with values being displayed
                # or a matplotlib graph

        # Learning with Tensor or so,
            # If the customer is investing in something, then we can learn from it

        # The ability to select data and then copy it on to something
            # What if value is not found.
            # If value is not found, then what?

        # Sorting up or down - but will it affect us or not?

        # When a treeview value is loaded onto the loader, we can press view more details.
            # PROBLEM: If a value is selected, then we can 

        # Reset file, save, save as in fike menu - add menu bar
        # A button that adds about 50 entries to the backup file.        
        # can we save the path and password in one text file or as pickle so that we have that outside 
            # the application - 
        # What if any entry is empty - emails, contacts could have a tick box
            # if there is no email then disable the entry box - place tick boxes next to it.
            # NaNs, Nones, especially if customer ID and name are
        # Save to excel should be one function.
        # Make the launch window method using a method
        # Finish the SMP version of indian video guy please.
        # Change address to entrybox and enter address in one line please.
        # Apply excel file reset method from within please.
        # Can we use data structures?
        # Can we use that files search method made in Jupyter?
        # button bg color
        ### Mark
        # separate the frames
        ### Add a progress bar to this please
        # How to make the frames move when changing size of the window
        # A way to make a copy of the treeeview and then save it somewhere.
        # A way to change the back up file by entering a path- 
        # Again, it will be a password window that opens so have a way to assign the password for this file.
        # send an email as a report to an email address of your choice as well.
            # This warns if internet is off, before it attempts - it checks for internet connection first.
        # Can we add methods to itertools cycle, so open, clean, print? stuff like that?
        # Rather than having the error pop up upon adding data, just add a warning up there somewhere.
        # Rather than profile popping up, have a button that shows pics, data and everything else.
        # At the end, this will be on a server where this PC and the other PC can access the software.
                # use multithreading and processing for this
                # have a sql database where all of this can be saved
                # because of this, more software can be made that can be shared between multiple servers
        # Undo changes - for that we need more memory somewhere.
        # A temporary dataframe that remembers when something was deleted or updayed.


def the_product_backlog(x = "EVERYTHING WE NEED"):

    # Control datatypes, dateofbirth insertion, finish this prototype with all buttons working, on_enter as well, launch file,
            # have file menu that enables or disables on_enter - fake data generation connection, add calculator Icon to open system calculator
            # Amend Address with Line 1, Line 2, Line 3
            # Make sure nulls are not allowed and it does not go through unless all details are entered correctly.
            # Change style - grid to pack()
            # Remove text box to entry please.
            # Cannot save unless cvalidated
            # Cannot reset file unless encrypted pass word is entered.
            # Menu bar for more functionality.
            # Start integrating SQL and have a separate connected program or window that allows views, etc and options to update database.
            # Make new window option for showing more details as well
            # Upon hover, show a small graph of what the customer's investments are yielding for them.
            # Use any other programming languages if needed - C, Java to build a better front end
            # OR, use another sexier library for other tools, if needed.
            # Build a save as box and project a file manager, explorer. 
            # Empty BOX?
            # Option to have multiple sources updating together
            # MongoDB functionality as well please.
            # The new window code needs to be credited to the online guy like a champ.
            # Testing is essentialk here.
            # Upon hover, show the graphs please.
            # Codecs, locale, glob, timezones as well.
            # The new window admin log in or log out.
            # Password protection, username recognition, feature block, 
            # Map graph that shows all locations of customers/ network/ suppliers/ product origins/ Investororinvestment origin
            # Pics of people
            # Open small window to show customers details
            # Hover over option as well please.
            # Use fake data to increase the number of data entered - Make sure this can be done internally so that a password protection fun can be done
            # Limit the number of data
            # Search internet for address, name, contact numbers
            # Connect network with this 
            # These could be customers and the network could be the sources of data we save for them
            # Each source has a price and each time, a sources data is forwarded to a customer - think about this.
            # So, imagine we have 20 sources - each for a price - we download them regularly.
            # We forward the data to customers on a regular basis - charge them, their card declines or not is upto them
            # We build a source manager type thing
            # Show on Github what you've made.
            # Use algorithms for sorting, searching, finding the quickest route between 2 customers.
            # We also ship products - this may as well use the above algorithm.
            # Data science, regression, machine and deep learning to make [predictions] of customer's investments
            # What if these are investors and they invest in sources.
            # The network is collection of co0mmodity prices that we send to the customer everyday.
            # This system is on a server so that it can be used remotely.
            # Data centre option where customers also have their own blog pages and they save videos, pictures, notes, ideas.
            # So, eventually a website which our customers can visit and use the CRM features.
            # Management has more options.
            # I have most options available.
            # Unittesting, version control, classes and modules in separate files (make a clone program and save them separately already)
            # Start already!
    # Record customer details for now - customer ID, DOB, Name, Last Name, Address, Email, Contact - Unique Only.
    # Generate fake data and then make 1000 rows and then import them to your treeview please.
            # CREATE A FAKE data generator that can be made using tkinter GUIs.
    # Divide tasks in immediate changes, long term changes and mixture of both.
    # Can we create a unique random ID for each customer which does not show up in the table, but we can only use it in the back end.
    # Send to Marcel when this is complete as an exe so he can test it out. Make sure he does not need Python for it though - nor excel.
        # Maybe just save it as a pickle file???
    # Delete index
    # Change treeview to listboxes for mapping - or open a new window where mapping option is available for us.
        # When one item selected, delete or insert but automatically highlight the next one.
    #In an insertbox, as soon as an item longer than required link is entered should be taken in immediately. Like on YTD.
    # Have loading screen, when loading the project up from start.
    # Change of DOB to 3 text boxes that added the hyphen and make a dtobject for us or make a dt object that is today's date.
    # Create something like the dataentry viewer box.
    # Reset the file
    # Remove methodology
    # Have a password protected settings menu that has the option to change the font, overwrite font using a file that we have saved as JSON
    # Power to select cells to know which one goes where in the SQL mapping - WOW. Check this situation out
    # Try with simple text files first or excel
    # This should read a file in treeview and then make it make then values we select the ones that should be pasted.
    # This can then allow us to delete the excel file to build a new one.
            # More settings and views
            # File for saving it somewhere else - Using Json or pickle, we save the link of the new path somewhere if we can.
    # Fix the grid, placement and packing of all these rows and what not - make the format neat and clean - divide in methods and then further into modules. DIVIDE and make neat.
    # Make 2 tabs like that man did in video # https://www.youtube.com/watch?v=J48tIufwmRI&t=69s
    # Save on multiple sheets different type of data- have a clever way of knowing where to save what type of data even if we are making a mistake here.
            # Making a sale, customer data, product details (Available and updated on a website)
    # Start with a smart window that asks what we want - view data of a sheet, update or add data. Other functions then do more and more.
    # Have option to clear the whole excel file or SQL database aswell.
    # Start making database for this and can we save to different relations
    # A tkinter interface that updates various relations of a database - could be excel
    # Fix the issue with exiting via cross
    # Add some windows to this window - like a file explorer from which we can get a file name, link or just look around
    # Add features like your calculator, or launch windows calculaotr
    # Writing notes that can be in a window that can be killed completely without saving anything
    # Have file edit and view buttons available as well
    # Add a very secure user registration for users to use - have access for managers and for simple access people - like you have in a SQL database
    # Add all of this on a server to be used as an exe and a SaaS online - this will take you to another level.
    # Have a website where managers can log in and then use this for updating stuff.
    # Have a portal for customers as well where they can make a purchase - The online store where we sell Online Tools.
    # Add pandas tricks to this same thing to do tricks with the data we are landing
    # Machine learning with colimns or the whole dataset.
    # Automatically clear and make an extra layer where this data gets added once you''ve press add so that we can have a view of the data we just added.
    # Your network must use TreeVIEW
    # Hardcore would be to make something like tkinter yourself that connects to the PC.
    # Use common modules stuff as well
    # Add to server or only launch from a deployable server that is created by Python
    # Learn more of these as well.
    # Arrange by date, name or dob, up or down in treeview.  SORTING OPTION UP AND DOWN
    # ADD DATETIME as well which adds current date time and then have sorting option too
    # This could be your Mintec project as well - Do not over do this,
    # Have geographical sales so that at the end we have a map of a graph that can be opened to see the number of sales made in each region
    # Make sure we can have a PYTZ usage as well
    # Have file edit view options to change various stuff
    # TEST it rigourously and apply basic datascience options like probability of sale in which region and when due to time of month.
    # Next month's sales - other pandasd and data analysis tricks applied
    # Should be neat and well tested - remove anything that causes errors
    # Sign in for multiple managers - view only mode as well.
    # Strong password protection
    # To exe please.
    # Later apply the network to it somehow - non project related
    # It is all connected baby.
    # Data scraping for names.
    # Or make it in Java.
    # Grab other ideas from idea lists in PC (prject ideas, iphone and samsung and others).
    # Make this deployable at first - have a way to ask whether this is launched for the 1st time but be clever if the other person is lying.
    # Tkinter tutorial for further knowledge.
    # At the end, attach the Java calulator with this.
    pass

def longterm_ideas():
    # a program that can create labels and entry boxes and then do what this app does.
    # only that that one is flexible.
    # Once options are chosen, a new tkinter app is deployed and dedicated to the group/department.
    pass

class Student:
    def __init__(self, root):
        print("Application starting...")
        print(sys.version)
        self.path = r"C:\Users\ABC\Desktop\Source-Management-System-Trial--main\Source-Management-System-Trial--main\files_excel\SMS.xlsx"
        if os.path.exists(self.path):
            df1 = pd.read_excel(self.path, engine='openpyxl', dtype = "object")
            self.df1 = df1
            # Take care of NaNs and replace them with N/A
        else:
            self.df1 = pd.DataFrame(columns = ["Customer ID", "Full Name", "Email", "Gender", "Contact", "DOB", "Address"] )
            
        # ROOT 

        self.all_dtypes = {"Customer ID": "int", "Full Name": "str", "Email" : "str", "Gender" : "str", "Contact" : "str", "DOB" : "str", "Address" : "str"}

        self.root = root
        self.root.title("Series Manager (SM V2.1)")
        self.root.geometry("1300x500+100+20")
        self.root.state("zoomed") # This makes sure that it is always launched in full screenmode.
        self.root.minsize(900,750)

        # TITLE
        # THIS IS WHERE YOU ENTER TITLE LABEL
        # FONT NO. 111
        title = Label( # This adds a label with a window
            self.root, text = "Series Management", 
            font= ("Sans-Serif",40, "bold"), 
            bg= "Dark Grey", 
            fg = "Black",
            bd=12, # Border width
            relief=FLAT) # must be flat, groove, raised, ridge, solid, or sunken
        title.pack(side=TOP, fill = X)


        
        # VARIABLES
        # VARIABLES FOR ENTRY BOXES

        # These should all have the word text in them.
        self.Roll_No_var = StringVar(value='Enter...') # these are to be added in the entry object as textvariable
        self.Name_var = StringVar(value='Enter...')
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.empty_box_text = StringVar()

        self.search_by_entry_text = StringVar(value='Enter...')
        self.combo_box_search_text = StringVar()

        self.tick_box_case_sensitive = IntVar()
        





        # MANAGE_FRAME MANAGE_FRAME MANAGE_FRAME
        # MANAGE_FRAME MANAGE_FRAME MANAGE_FRAME
        Manage_Frame = Frame(self.root, bd=2, relief=FLAT, bg = "Dark Grey") # FLAT RAISED SUNKEN GROOVE RIDGE
        Manage_Frame.place(x=30, y=100, width= 450, height=600)
        # Manage_Frame.grid_columnconfigure(1, weight=2) # this is used to centre the label.        
        


        # MAIN LABEL - MANAGE FRAME
        # FONT NO. 112
        font_labels = ("Sans-serif", 25)
        Manage_Frame_Label = Label(Manage_Frame, text = "Manage", font = font_labels, bg = "Dark Grey" , fg= "White", relief = FLAT, bd=1.1)
        Manage_Frame_Label.grid(row = 0, columnspan = 2, column = 0, pady = 20, padx= 20)
        d = { "bg" : "Dark Grey" ,"fg": "Black", "relief" : FLAT, "bd":1.1} # done with a dictionary.


        # FONTS FOR MANAGE FRAME LABELS AND ENTRIES - TO BE CONVERTED TO font.Font
        font_labels = ("Sans-serif", 15, "bold")
        font_entry = ("Sans-serif", 15)



        # Labels and Entries.
        # FONT NO. 113
        # FONT NO. 114 (FOR ENTRY BOXES ONLY.)

        # ROLL NUMBER - L
        Roll_Number_Label = Label(Manage_Frame, text = "Customer ID", font = font_labels, **d)
        Roll_Number_Label.place(x=5, y = 82)
        # Roll_Number_Label.grid(sticky="w") # w = west

        # ROLL NUMBER - E
        text_entry_roll_number = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.Roll_No_var)
        text_entry_roll_number.place(x = 140, y = 77)


        # NAME - L
        Name_Label = Label(Manage_Frame, text = "Full Name", font = font_labels, **d)
        Name_Label.place(x=5, y = 82+30)        

        # NAME - E
        text_entry = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.Name_var)
        text_entry.place(x = 140, y = 77+30)
        

        # EMAIL - L
        Email_Label = Label(Manage_Frame, text = "Email", font = font_labels, **d)
        Email_Label.place(x=5, y = 82+30+30)        

        # EMAIL - E
        text_entry_email = Entry(Manage_Frame, font = font_labels, bd=1, relief = GROOVE, textvariable=self.Email_var)
        text_entry_email.place(x = 140, y = 77+30+30)


        # GENDER - L
        Gender_Label = Label(Manage_Frame, text = "Gender", font = font_labels, **d)
        Gender_Label.place(x=5, y = 82+30+30+30)

        # Change to tick boxes.

        # GENDER - E (combobox)        
        combo_box_gender = ttk.Combobox(Manage_Frame, font = ("Sans-Serif", 12), state = "readonly", textvariable=self.Gender_var)     
        combo_box_gender['values'] = ("Male", "Female", "Transgender" ,"No Comment")
        combo_box_gender.place(x = 140, y = 78+90, width = 225, height = 25)
        ### HAVE OPTION TO AUTOSELECT WHEN PRESSING AN ALPHABET.
  

        # CONTACT - L
        Contact_Label = Label(Manage_Frame, text = "Contact", font = font_labels, **d)
        Contact_Label.place(x=5, y = 82+120)        

        # CONTACT - E
        text_entry_contact = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.Contact_var)
        text_entry_contact.place(x = 140, y = 77+120)


        # ADDRESS - L 
        Address_Label = Label(Manage_Frame, text = "Address", font = font_labels, **d)
        Address_Label.place(x=5, y = 82+155)

        # ADDRESS - E
        self.text_entry_address = Text(Manage_Frame, width = 25, height = 4)
        self.text_entry_address.place(x = 140, y = 77+160)


        # DOB - L
        DOB_Label = Label(Manage_Frame, text = "DOB", font = font_labels, **d)
        DOB_Label.place(x=5, y = 82+250)

        # DOB - E (THREE COMBO BOXES)
        DOB_Entry = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.DOB_var)
        DOB_Entry.place(x = 140, y = 80+250) # Convert this to datetime object
        # But it must have a pick day month and year option too.
        # To be improved later.


        ### EMPTY ONE.
        self.empty_entry_box_label = Label(Manage_Frame, text = "Index", font = font_labels, **d)
        self.empty_entry_box_label.place(x=5, y = 110+250)
        empty_entry_box = Entry(Manage_Frame, font = font_entry, bd=1, relief = GROOVE, textvariable=self.empty_box_text)
        empty_entry_box.place(x = 140, y = 110+250) # Convert this to datetime object

        
        Main_Button_Frame = Frame(self.root, bd=1, relief=FLAT, bg = "Dark Grey") # BD = BORDER WIDTH
        Main_Button_Frame.place(x=400, y=750) #, width= 650, height=50)

    
        BUTTON_FONT = font.Font(weight = "bold", size =  10, family = 'Helvetica')
        #BUTTON ADD
        button_manage_add = Button(Main_Button_Frame, bg = "Dark Grey", font = BUTTON_FONT, text="Add", height = 3, width = 10, activebackground = "grey", command=self.add_students_to_dataframe)
        button_manage_add.grid(row=1, column = 3)# , padx = 7, pady = 13)
        #BUTTON SAVE
        button_manage_update = Button(Main_Button_Frame, bg = "Dark Grey", font = BUTTON_FONT, text="Save",height = 3, width = 10, activebackground = "grey", command = self.save_to_excel)
        button_manage_update.grid(row=1, column = 4)# , padx = 7, pady = 13)
        ##BUTTON DELETE SELECTED ROW
        button_manage_delete = Button(Main_Button_Frame, bg = "Dark Grey", font = BUTTON_FONT, text="Delete",height = 3, width = 10, activebackground = "grey", command = self.delete_row)
        button_manage_delete.grid(row=1, column = 5)# , padx = 7, pady = 13)
        #BUTTON CLEAR
        button_manage_clear = Button(Main_Button_Frame, bg = "Dark Grey", font = BUTTON_FONT, text="Clear",height = 3, width = 10, activebackground = "grey", command = self.clear)
        button_manage_clear.grid(row=1, column = 6)# , padx = 7, pady = 13)
        #BUTTON UPDATE SELECTED ROW
        button_update_row = Button(Main_Button_Frame, bg = "Dark Grey", font = BUTTON_FONT, text="Update Row",height = 3, width = 10, activebackground = "grey", command = self.update_row)
        button_update_row.grid(row=1, column = 7)# , padx = 7, pady = 13)
        #RESET WHOLE TABLE
        button_reset_file = Button(Main_Button_Frame, bg = "Dark Grey", font = BUTTON_FONT, text="RESET FILE",height = 3, width = 10, activebackground = "grey", command = lambda: self.reset_file())
        button_reset_file.grid(row=1, column = 8)# , padx = 7, pady = 13)
        ##BUTTON Launch file for viewing
        launch_file_button = Button(Main_Button_Frame, bg = "Dark Grey", font = BUTTON_FONT, text="Launch File",height = 3, width = 10, activebackground = "grey", command=self.launch_file)
        launch_file_button.grid(row=1, column = 9)        
        ##BUTTON Exit system
        exit_system_button = Button(Main_Button_Frame, bg = "Dark Grey", font = BUTTON_FONT, text="Exit",height = 3, width = 10, activebackground = "grey", command=self.exit_method)
        exit_system_button.grid(row=1, column = 10)

        # Now, this may cause errors as nothing will be detecte in for loop insertion - so improvise the if statement please.
        # This requires a password that will we save in a file that is pickled - a loading screen shall appear when that happens.
    

        # LABEL AUTHOR
        label_author = Label(Manage_Frame, text = "Author: 'Hamza Malik'")
        label_author.place(x=15, y=550)

        # LOADING LABEL 
        self.loading_label = Label(Manage_Frame, text = "", bg = "Dark Grey")
        self.loading_label.place(x = 350, y = 550)

        

        font_labels = ("Sans-serif", 12)

        # SEARCH FRAME NOW
        #DETAIL FRAME DETAIL FRAME DETAIL FRAME
        #DETAIL FRAME DETAIL FRAME DETAIL FRAME
        Detail_Frame = Frame(self.root, bd=1, relief=FLAT, bg = "Dark Grey") # BD = BORDER WIDTH
        Detail_Frame.place(x=505, y=95+5, width= 900, height=600)


        #MAIN LABEL - DETAIL FRAME
        # FONT NO. 112
        Detail_Frame_Label = Label(Detail_Frame, text = "Search", font = ("Sans-Serif", 25), bg = "Dark Grey", fg= "White", relief = FLAT, bd=1.1)
        Detail_Frame_Label.grid(row = 0, columnspan=2, column=0, pady = 20, padx= 20, sticky="w") # column 2 and covers 2 and 3 thus next should be 4.


        

        # SEARCH FRAME BUTTONS
        # FONT NO. 113
        # FONT NO. 114 (FOR ENTRIES)
        #SEARCH BY - L
        search_by_label_detail_frame = Label(Detail_Frame, text="Search by", font = ("Sans-Serif", 15), bg = "Dark Grey")
        search_by_label_detail_frame.grid(row=1, column = 0, padx = 20, pady= 20)
        
        #SEARCH BY - E (COMBO BOX)
        combo_box_search = ttk.Combobox(Detail_Frame, font = ("Sans-Serif", 15), state = "readonly", textvariable = self.combo_box_search_text)     
        combo_box_search['values'] = ("Customer ID", "Full Name", "Email", "Any")
        combo_box_search.grid(row=1, column=3, padx= 10, pady=21)
        ### If nothing is chosen then present error - the error shall be printed back underneath this column.
        
        font_b = ("Sans-Serif", 10, "bold")

        #SEARCH BY = E (ENTRY)
        search_by_entry = Entry(Detail_Frame, font=font_entry, bd = 1, relief = GROOVE, textvariable = self.search_by_entry_text) # ADD BOLD 
        search_by_entry.grid(row = 1, column = 1)

        showAll_button = Button(Detail_Frame, text = "Show All", font = font_b, bg = "Dark Grey",height = 2, width = 10, activebackground = "grey", command = self.fetch_data)
        showAll_button.grid(row=0, column = 1)


        # BUTTON FRAME - DETAIL FRAME (SEARCH BY FRAME)
        button_frame_detail_frame = Frame(Detail_Frame, bd=1, relief = RIDGE, bg = "Red", height = 50, width = 380)
        button_frame_detail_frame.place(x = 400, y = 150)

        # BUTTONS - Button Frame - belongs to DETAIL FRAME
        # have a separate variable for height and width
        search_button = Button(button_frame_detail_frame, text = "Search", font = font_b, bg = "Dark Grey",height = 2, width = 10, activebackground = "grey", command = self.print_search_items)
        search_button.grid(row=0, column = 0)
        
        

        check_case_sensitive_tick_box = Checkbutton(
            Detail_Frame, text='Case Sensitive',font = font_b,
            variable=self.tick_box_case_sensitive, height = 2, bg = "Dark grey",
            relief = FLAT,
            bd=0,
            activebackground = "dark grey",
            onvalue=1, offvalue=0)
            #, command=print_selection)

        check_case_sensitive_tick_box.grid(row=3, column = 1)
        # (row=1, column=3, padx= 10, pady=21)

        # TABLE FRAME - DETAIL FRAME - to place the Treeview object in.
        table_frame_detail_frame = Frame(Detail_Frame, bd=1, relief = GROOVE, bg = "Dark Grey")
        table_frame_detail_frame.place(x = 20, y= 200, height = 375, width = 850)        

        # Make scrollbar objects and assign the orientation.
        self.scroll_x = Scrollbar(table_frame_detail_frame, orient=HORIZONTAL) 
        self.scroll_y = Scrollbar(table_frame_detail_frame, orient=VERTICAL) 
        
        # Pack them within the frame of choice.
        self.scroll_x.pack(side=TOP, fill = X)
        self.scroll_y.pack(side=RIGHT, fill = Y)

        # Need to make this work again.

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        
        # Create a widget and place within a Frame, and set the xscrollcommand and yscrollcommand argument
        self.search_results_table = ttk.Treeview(
            table_frame_detail_frame, 
            show="headings",
            selectmode='browse', # The ability to select one or more
            columns = ("Index", "Customer ID", "Full Name", "Email", "Gender", "Contact", "DOB", "Address"), # these columns are just for tags.
            xscrollcommand=self.scroll_x.set, 
            yscrollcommand=self.scroll_y.set)

        self.search_results_table.tag_configure('odd', background='#E8E8E8')
        self.search_results_table.tag_configure('even', background='#DFDFDF')
        

        # Configure the scrollbars and set the command for them.
        self.scroll_x.config(command=self.search_results_table.xview)
        self.scroll_y.config(command=self.search_results_table.yview)

        # Lets name the headings of the TreeView
        # This could be a for loop.
        self.search_results_table.heading("Index", text = "Index")
        self.search_results_table.heading("Customer ID", text = "Customer ID")
        self.search_results_table.heading("Full Name", text = "Full Name")
        self.search_results_table.heading("Email", text = "Email")
        self.search_results_table.heading("Gender", text = "Gender")
        self.search_results_table.heading("Contact", text = "Contact")
        self.search_results_table.heading("DOB", text = "DOB")
        self.search_results_table.heading("Address", text = "Address")

        for column in self.search_results_table['columns']:
            if column != "Email" and column != "Address":
                self.search_results_table.column(column, width = 150) # Loop to adjust the width of the system.
            elif column == "Index":
                self.search_results_table.column(column, width = 50) # Loop to adjust the width of the system.
            else:
                self.search_results_table.column(column, width = 300) # Loop to adjust the width of the system.

        self.search_results_table.pack(fill=BOTH, expand=1) # This fills and expands till the end of it
        # self.search_results_table.bind("<ButtonRelease-1>", self.get_cursor) # attach a button when button is clicked - row is selected.
        self.search_results_table.bind("<ButtonRelease-1>", self.get_cursor) # attach a button when button is clicked - row is selected.
        self.search_results_table.bind("<Button-3>", self.test_method) # attach a button when button is clicked - row is selected.
        # self.search_results_table.bind("<Enter>", self.on_enter) # attach a button when button is clicked - row is selected.
        self.fetch_data()       

    # Experimental - if we plan on adding more values.
    # So, the idea is. The customers register, then they invest in companies and then the total is added to their dataframes.
    # The current treeview only shows the values we need.
    def on_enter(self, event):
        a = self.search_results_table.focus()
        b = self.search_results_table.item(a)
        print("Hovering over... ")
        print(b["values"])


    # ADD TO TREEVIEW
    def add_students_to_dataframe(self):
        # Find the position of the dataframe so that an index can be added too.
        # The treeview and DataFrame are going to be handled differently.
        position = len(self.df1.index.tolist())
        # Every value must have a datatype condition or else it shouldn't be cleared and not added to the TreeView - also if anything is empty, do not add but do not clear.
        # Apply regex for email format, email and contact number
        list_ = [
            self.Roll_No_var.get(),         
            self.Name_var.get(), 
            self.Email_var.get(), 
            self.Gender_var.get(), 
            self.Contact_var.get(), 
            self.DOB_var.get(), 
            self.text_entry_address.get('1.0',END) # Issue with this line.
            ]
        
        # Do data check write here.
        # Use regex for emails, isnumeric for contact, alphanum for address, isalpha for name, isnumeric for DOB, isalpha for gender
        # Regex to check each one
        if self.Roll_No_var.get().isnumeric() and self.Name_var.get().isalpha() and self.Email_var.get().isalnum(): # and self.Gender_var.get().isalpha() and self.Contact_var.get().isalpha() and self.DOB_var.get().isalpha() and self.text_entry_address.get('1.0', END).isalpha():
            print("Good to go!")
        else:
            print("Failure!")

        list_ = list(map(str, list_))
        list_with_index = [position] + list_
        
        self.search_results_table.insert("",END, text = self.Contact_var.get(), values = list_with_index)
        series_ = pd.Series(list_, ["Customer ID", "Full Name", "Email", "Gender", "Contact", "DOB", "Address"], name="SERIES1" )
        series_ = series_.to_dict()
        self.df1 = self.df1.append(series_, ignore_index=1)        
        # Added to dataframe but not saved at all.

        messagebox.showinfo("Warning", "The row is not saved to back up file. Press update to save.")
        self.loading_label.config(text = "Not saved!")        

    def save_to_excel(self):
        # Insert try and except right here so that we can make sure errors do not say SAVED!
        # Change the size of the Saved box please.
        path = self.path
        MsgBox = messagebox.askquestion ('Permission','Are you sure you want to save to backup file?',icon = 'warning')
        if MsgBox == 'yes':
            writer = pd.ExcelWriter(path)
            self.df1.to_excel(writer, index = False)
            writer.save()
            self.clear()
            self.loading_label.config(text = "Saved!")
        else:
            messagebox.showinfo('Not saved','Returning to main window.')       
        
    def launch_file(self) -> "For viewing purposes and making quick amends only - they won't affect the treeview":        
        os.startfile(self.path)

    def delete_tree_data(self):
        self.search_results_table.delete(*self.search_results_table.get_children())

    def fetch_data(self):
        print("Fetch Run!")
        # Working well as dtype is imported as object.
        rows = self.df1.values.tolist()
        # We need to add the indexes as well so that we know.
        self.delete_tree_data()
        for x,row in enumerate(rows):
            self.search_results_table.insert('',END,text = row[4], values=[x] + row)
            # text takes the 4th row value (the number) and values takes the index values + the rest of the row.

    # Clears the textboxes only.
    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.text_entry_address.delete('1.0',END)
        

    def get_cursor(self, ev):
        print("GET CURSOR!!!")
        cursor_row = self.search_results_table.focus()
        contents = self.search_results_table.item(cursor_row)
        v = contents["values"]
        t = contents["text"]
        i = 0
        if v == "":
            print("No value.")
        else:
            i = v[0]
            self.Roll_No_var.set(v[1])
            self.Name_var.set(v[2])
            self.Email_var.set(v[3])
            self.Gender_var.set(v[4])
            self.Contact_var.set(t)
            self.DOB_var.set(v[6])
            self.text_entry_address.delete('1.0',END)
            self.text_entry_address.insert(END, v[7])
            self.empty_box_text.set(v[0])

    def update_row(self):
        # Check if any fields are empty,
        # Check if anything in treeview is selected.
        # Or find a way to have index saved whilst there is data in the fields.
        i = self.search_results_table.item(self.search_results_table.focus())
        # If there are no values in selected tree row
        if i["values"] == "":
            print("NONE")
            messagebox.showinfo("Error", "Field(s) empty")
        else:
            ind = (i["values"][0]) # the index from the treeview
            list143 = [self.Roll_No_var.get(),         
            self.Name_var.get(), 
            self.Email_var.get(), 
            self.Gender_var.get(), 
            self.Contact_var.get(), 
            self.DOB_var.get(), 
            self.text_entry_address.get('1.0',END)]
            # If selected row is now in fields and the values are blank, then raise an error.
            if list143[0] == "" or list143[1] == "" or list143[2] == "" or list143[3] == "":
                messagebox.showinfo("Error", "Field(s) empty - cannot update!")
            
            else:
                self.df1.iloc[ind] = list143 # replace that particular row with the list.
                self.fetch_data() # fetch the data again to refresh the updated dataframe.
                self.loading_label.config(text="Not saved!") # label shows that changes aren't saved.
            print(self.empty_box_text.get())
            print("Updated and fetched.")

    def delete_row(self):
        # Either use the details that are imported in the textboxes or from the back end using the index please.
        i = self.search_results_table.item(self.search_results_table.focus())
        if i["values"] == "":
            messagebox.showinfo("Error", "Field(s) empty")
            # Replace with label in the space somewhere using label.config. 
        else:
            ind = (i["values"][0])
            self.df1 = self.df1.drop([ind])
            self.df1 = self.df1.reset_index(drop=True)
            self.fetch_data()
            self.loading_label.config(text="Not saved!")
            self.clear()
        # Make a method that selects 

    def exit_method(self):        
        self.root.destroy()

    def windowLauncherMethodForPasswordWindow(self, class_, reset_dataframe_completely, deny_method):
        enterPasswordWindow = Toplevel()
        class_(enterPasswordWindow, reset_dataframe_completely, deny_method)

    def password_window(self, class_, reset_dataframe_completely, deny_method):
        global enterPasswordWindow
        try:
            if enterPasswordWindow.state() == "normal":
                enterPasswordWindow.focus()
        except NameError as e:
            # This could be a method as well. We've made it, but let's keep a copy of it too.
            self.windowLauncherMethodForPasswordWindow(class_, reset_dataframe_completely, deny_method)
            # enterPasswordWindow = Toplevel()
            # class_(enterPasswordWindow, reset_dataframe_completely, deny_method) # because the class takes in root, run, deny
        except TclError as T:
            self.windowLauncherMethodForPasswordWindow(class_, reset_dataframe_completely, deny_method)
            # enterPasswordWindow = Toplevel()
            # class_(enterPasswordWindow, reset_dataframe_completely, deny_method)  # because the class takes in root, run, deny

    def reset_dataframe_completely(self):
        messagebox.showinfo(title="LAUNCHED",message="This launched!")
        self.df1 = self.df1[0:0]
        writer = pd.ExcelWriter(self.path)
        self.df1.to_excel(writer, index = False)
        writer.save()
        self.fetch_data()
        
    def deny_method(self):
        messagebox.showinfo(title="Failed", message="This is failed.")

    def reset_file(self):
        # This takes in the method that has the toplevel window and the following function
        self.password_window(PasswordWindow, self.reset_dataframe_completely, self.deny_method)        
            
        # The password is saved in a pickle file
        # Clear the TreeView as well.
        # It should be able to start entering data again.

        # How to delete a file using Python?
        # Add warning that only administrator priveleges and ONLY a manager can delete or reset it.
        # Create a new one with same dtypes and attributes, please.

        # Or, just clear the dataframe we are using, the treeview will clear, also and so will the excel file.

    def test_method(self, event):
        # Learn how to select an individual cell.
        # Create a new window where all values are added
        a = self.search_results_table.focus() # This gets the ID, and that is it.
        b = self.search_results_table.item(a)
        c = self.search_results_table.identify_column(event.x)
        
        print(c)

        cols = self.search_results_table['columns']

        index1 = int(c[1:])
        if index1 != 0:
            print(f"Index Number: {int(index1)-1}")
            print("Column name: {}".format(cols[int(index1) - 1],))       

            print(b["values"])
            print(b["values"][int(index1)])

            s = f"I: {int(index1)} C: {cols[int(index1) - 1]}" #  V: {b['values'][int(index1]}"
        
            self.empty_box_text.set(s)

            print(b["values"][int(index1) - 1])
            print(event.x)
            print(event.y)

    def test_button(self, f, d):
        f(d)

    def print_search_items(self):
        # The column we are searching in is fixed.  
        # Have an any option where we search for the word and it finds those that have the value       
        
        column = self.combo_box_search_text.get() # The column we are searching in
        row = self.search_by_entry_text.get() # The value we are searching

        if column == "Any":
            print(self.df1[self.df1.apply(lambda r: r.str.contains(row, case=False).any(), axis=1)] )


            # values_found = self.df1[self.df1.apply(lambda r: r.str.contains(row, case=False).any(), axis=1)] 
            # print(values_found)
            # THe tree should only show this value and then
            # It can be selected
            # then, press back to go back to normal
        else:
            print(self.df1[self.df1[column].str.contains(row, na = False)].index.values )
            print(self.df1[self.df1[column].str.contains(row, na = False)] )            
            print("\n")
            values_found = self.df1[self.df1[column].str.contains(row, na = False)].values 
            print(values_found)
        
        
def more_product_backlog(x = "MOREOFWHATWENEED"):




    # Can this be modular so that all sections are divided? Challenge 1.
    # Ratta, Steps, Copy
    # You need to first decide on your copy the type of store you need. Make a BLUEPRINT - Do this non-stop.
    # CHANGE TO GRID MODE.
    # Use itertools cycle to iterate over a column and select a value - FOR FUN call it the iterator like you did in your practice Software
    # Make your own mapping tool that is smart and knows more that sourfce manager.
    # Have a fake data generator to increment multiple fake values in this treeview
    # Try opening the treeview in a new window
    # Try dividing the two in half so that there are to main windows.
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
    # Use extensive Python on this please.
    # Copy all instructions from Project43 and the Left file
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

    # Desktop apps are fun to make and this is what I want to do forever and ever.
    # Apache, node.js, vue.js, other servers, graphQL, amplify, mongoDB, mySQL, C#, C, C++, JS, HTML5.
    # Make more from YouTube till you are comfortable with them yourself.
    # Have loading label on the window.
    # Tkinter full tutorial.

    # VERSIONS USED FOR THIS PROJECT.

    # beautifulsoup4==4.9.3
    # bs4==0.0.1
    # certifi==2020.12.5
    # chardet==4.0.0
    # et-xmlfile==1.0.1
    # idna==2.10
    # jdcal==1.4.1
    # lxml==4.6.2
    # numpy==1.19.5
    # openpyxl==3.0.6
    # pandas==1.2.1
    # python-dateutil==2.8.1
    # pytz==2020.5
    # requests==2.25.1
    # six==1.15.0
    # soupsieve==2.1
    # urllib3==1.26.3
    # xlrd==2.0.1
    pass; pass; pass

def main():

    root = Tk()
    obj = Student(root)
    
    root.mainloop()


if __name__ == '__main__':
    
    main()