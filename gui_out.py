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
for entry in ner.neMap : 
  text.insert(END, entry + "\n")
  for entity in ner.neMap[entry]:
    text.insert(END,"\t" + entity + "\n")

#attach scrollbar with the text widget
h.config(command=text.xview)

win.mainloop()



