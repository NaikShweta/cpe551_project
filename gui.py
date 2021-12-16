#!/usr/bin/python3.9
import PySimpleGUI as sg

sg.theme("DarkTeal2")

layout = [[sg.T("")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key = "-IN-")], [sg.Button("Submit")]]

#create the window

window = sg.Window("My File Browser", layout)

while True:
  event, values = window.read()
  #End program if user closes window or presses OK button
  if event == "Exit" or event == sg.WIN_CLOSED:
    break
  elif event == "Submit":
    print(values["-IN-"])
    
window.close()

