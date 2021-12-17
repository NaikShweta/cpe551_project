#!/usr/bin/python3.9
import ner
#import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Let's create the Tkinter window
win = Tk()

#set the geometry
win.geometry("700x350")

#add a scrollbar (horizontal)
h = Scrollbar(win, orient = 'horizontal')
h.pack(side = BOTTOM, fill='x')

# add a text widget
text = Text(win, font=("Calibi, 16"), wrap = NONE, xscrollcommand=h.set)
text.pack()

#add text in the widgest
text.insert(END, ner.ne_tree)

#attach scrollbar with the text widget
h.config(command=text.xview)

win.mainloop()


# creating a function called DataCamp_Tutorial()
#def DataCamp_Tutorial():
    #tkinter.Label(window, text = ner.ne_tree).pack()

#tkinter.Button(window, text = "Click Me!", command = DataCamp_Tutorial).pack()
#window.mainloop()

