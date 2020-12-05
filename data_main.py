import pandas as pd
import sys, os
import numpy
import re
import random as rd
import datetime
from matplotlib import pyplot as plt
from names_main import list_of_names



# df = pd.read_excel("Tidy\\complex_header.xlsx", header=[1], sheet_name="Sheet1", index_col=0)
"""
self.Roll_No_var = StringVar() # these are to be added in the entry object as textvariable
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
"""

columns = ["Roll No.", "Name", "Email", "Gender", "Contact", "DOB", "Address"]

# Have 50 entries.
# Check if file already exists.
# Have ascending roll numbers.

roll = [1100000+(x * 10000)+rd.randint(1000,9999) for x in range(1,50)]
name = []
email = []
gender = []
contact = []
DOB = []

