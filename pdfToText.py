#!/usr/bin/python3.9
import PyPDF2
import os
import slate3k as slate

import gui

#print(gui.path)

path = gui.path

cwd = os.getcwd()
files = os.listdir(cwd)
#print(files)

pdfFileObj = open(path, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#number of pages of the pdf file
#print (pdfReader.numPages)

pageObj = pdfReader.getPage(0)

text = pageObj.extractText()

#print (pageObj.extractText())

pdfFileObj.close()
