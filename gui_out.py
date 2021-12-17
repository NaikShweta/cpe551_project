#!/usr/bin/python3.9
import ner

import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

# creating a function called DataCamp_Tutorial()
def DataCamp_Tutorial():
    tkinter.Label(window, text = ner.ne_tree).pack()

tkinter.Button(window, text = "Click Me!", command = DataCamp_Tutorial).pack()
window.mainloop()

