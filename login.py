from tkinter import *

root = Tk()

root.geometry("500x300")

def getVals():
    print("Accepted")

# Registration Form Heading
Label(root, text="Registration Form", font="arial 15 bold").grid(row=0,column=3)

# Field Names
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
DOB = Label(root, text="Date of Birth")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
DOB.grid(row=4, column=2)

# Variables for Storing Data
nameValue = StringVar
phoneValue = StringVar
genderValue = StringVar
DOBValue = StringVar

# Check Button
checkValue = IntVar

# Creating Entry Fields
nameEntry = Entry(root, textvariable = nameValue )
phoneEntry = Entry(root, textvariable = phoneValue )
genderEntry = Entry(root, textvariable =  genderValue)
DOBEntry = Entry(root, textvariable =  DOBValue)

# Packing Entry Fields
nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
DOBEntry.grid(row=4, column=3)

# Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable=checkValue)
checkbtn.grid(row=5, column=3)

# Submit Button
Button(text="Submit",command=getVals).grid(row=6,column=3)

root.mainloop()