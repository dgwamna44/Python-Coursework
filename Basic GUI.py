"""
Program: Duroje_Gwamna_HW7.5BasicGUI.py
Author: Duroje Gwamna
Date Last Modified: 11/14/2021

This program shows my favories meals using the tkinter visual platform
"""

import tkinter

def pick_bk():
    label.config(text="Biscuits and Gravy")

def pick_second_bk():
    label.config(text="Oatmeal")

def pick_lunch():
    label.config(text="Arby's")

def pick_dinner():
    label.config(text="Chicken Spaghetti")

m = tkinter.Tk()
m.title = "Favorite Meal"

check1 = tkinter.Checkbutton(m, text="Breakfast",
                           command=pick_bk).grid(row=1)
check2 = tkinter.Checkbutton(m, text="Second Breakfast",
                            command=pick_second_bk).grid(row=2)
check3 = tkinter.Checkbutton(m, text="Lunch",
                            command=pick_lunch).grid(row=3)
check4 = tkinter.Checkbutton(m, text="Dinner",
                            command=pick_dinner).grid(row=4)
label = tkinter.Label(m, text="waiting")
label.grid(row=5)

exitbutton = tkinter.Button(m, text="Exit", command=m.destroy).grid(row=6)

m.mainloop()
