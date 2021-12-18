# cpe551_project
CPE 551 Final Project

Named entity recognition (NER)is probably the first step towards information extraction that seeks to locate and 
classify named entities in text into pre-defined categories such as the names of persons, organizations, locations, 
expressions of times, quantities, monetary values, percentages, etc. NER is used in many fields in Natural Language Processing (NLP).

In this project nltk package is used to build a NER. The package takes a text input and gives the tag sequences converted into a chunk tree.

First, thorugh a GUI, a pdf file is taken as an input. The input GUI is built using PySimpleGUI library.
This takes the path of the pdf file and gives it to pdfToText converter. The converter is built using PyPDF2 module. This convertes the given pdf input to text.

This text is given as input to ner.py module where the chunk tree is built. From this chunk tree, labels and entities are separated.

This separated list if given to the output GUI and displayed in a window. The output GUI is built using tkinter module.

How to run the Project:
1. Run gui_out.py
2. Select the file and click sumbit.
3. The output GUI will display named entities.
