
# Q1: Write a function to print “hello_USERNAME!” USERNAME is the 
# input of the function.

from tkinter import *

def hello_name_gui():
    
    """ def hello_name_GUI() GUI version - gets <user_name> from Entry and 
    displays 'Hello <username>' in a popup window """

    pu_window = Toplevel(win)
    pu_window.title("Welcome!")

    user_name = name_entry.get()

    pu_frame = Frame(pu_window)
    pu_frame.pack(padx=20,pady=20)

    name_label = Label(pu_frame,text="Hello "+user_name+
                       "!",font=('Helvetica','14','bold'))
    name_label.grid(row=1,column=1)


def hello_name(user_name):
    
    """ def hello_name(user_name) Takes in <user_name> 
    as input and returns 'Hello <username>' """

    name = user_name.title()
    message = f"Hello {name}!"
    return message 

# Choose whether to corntinue with the GUI or Terminal

selection = input("Would you like to use the GUI [G]"+
                  " or remain on the Terminal [T]? ")

if selection.lower() == 'g':

# Display input in tkinter window 

    win = Tk()
    win.title("Enter Your Name")

    win_frame = Frame(win)
    win_frame.pack(padx=20,pady=20)

    name_entry_label = Label(win_frame,text="Enter Your Name: ")
    name_entry_label.grid(row=1,column=0)

    name_entry = Entry(win_frame,width=30)
    name_entry.grid(row=1,column=1)

    submit_btn = Button(win_frame,text="Submit",command=hello_name_gui)
    submit_btn.grid(row=4,column=1)

    win.mainloop()

else:
    user_name = input("Please enter your name: ")
    message = hello_name(user_name)
    print(message)



#################################################################################

# Q2: Write a python function, first_odds that prints the odd 
# numbers from 1-100 and returns nothing - no give and all take

def first_odds():
    
    """ def first_odds() Takes no arguments, prints out odd numbers from 
    1 to 100, inserts new line about 1/2 way thru for readablility,
    excludes trailng comma """

    index=0
    for num in range(100):
        if (num % 2) == 0:
            index+=1
            if index == 28:
                print("\n")
            continue
        else:
            if num != 99:
                print(num,end=", ")
            else:
                print(num)
first_odds()


#################################################################################

# Q3: Write a Python function, max_num_in_list to return the max 
# number of a given list

import random

def max_num_in_list(num):
    
    """ def max_num_in_list(nums) Takes list argument of random numbers 
    <num[]> and returns the largest value in the list as a string """

    max_number = max(num)
    message = f"\n{max_number} is the largst number in your list"
    return message


number_list=[]

# Generate 20 random numbers 'tween 1 and 30 and box 'em up 

for i in range(0,20):
    n=random.randint(1,30)
    number_list.append(n)

print(f"\nThe List:\n{number_list}")

max_num = max_num_in_list(number_list)
print(max_num)


#################################################################################

# Q4: Write a function to return if the given year is a leap year

def is_leap_year(year):

    """ def is_leap_year(year) Takes int <year> as argument 
    and returns True if the year is a leap year """
    
    year = int(year)

    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False
    
year = input("Enter a year and I will tell you if it is\
a leap year: ")

leap_year = is_leap_year(year)

if leap_year:
    print(f"{str(year)} is a leap year")
else:
    print(f"{str(year)} is not a leap year")


#################################################################################

# Q5: Write a function to check to see if all numbers in list are consecutive numbers

def is_consecutive(a_list):

    """ is_consecutive(a_list) Takes a list of integers as its argument and returns True if
     all numbers are in consecutive order, otherwise returns False """

    for i in range(1,len(a_list)):
        if a_list[i] - a_list[i-1] == 1:
            continue
        else:
            return False
    return True
    
print("\nConsecutive Numbers: ")
print("==========================")

num_list_cons = [5,6,7,8,9,10]
consecutive = is_consecutive(num_list_cons)
if consecutive:
    print("consecutive set of numbers")
else:
    print("not a consecutive set")


print("\nNON-Consecutive Numbers: ")
print("==========================")

num_list_non_cons = [1,3,5,7,9,11]
consecutive = is_consecutive(num_list_non_cons)
if consecutive:
    print("consecutive set of numbers")
else:
    print("not a consecutive set")