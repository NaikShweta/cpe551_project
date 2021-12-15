#!/usr/bin/python3.9
import PyPDF2
import os

cwd = os.getcwd()
files = os.listdir(cwd)
print(files)

pdfFileObj = open('test.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

text = pageObj.extractText()

print (pageObj.extractText())

pdfFileObj.close()
