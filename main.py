import PyPDF2
import sys
import os

pth_fls = input("Path to direcotry containing files: ")

for fl in os.listdir():
    if fl.endswith('.pdf'):
        merger = PyPDF2.PdfFileMerger()
        merger.append(fl)

pth_down = input("Path to directory to download combined file: ")
merger.write(pth_down)
