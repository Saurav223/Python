from PyPDF2 import PdfMerger
import os

def Merger(files):
    merge = PdfMerger()  #it make object of class PdfMerger
    for i in files:
        merge.append(i)
    merge.write("mergered.pdf") #this writes the merged content into new pdf file
    merge.close()

Files = os.listdir()
pdffiles = []
for i in Files:
    if i.endswith(".pdf"):
        pdffiles.append(i)

pdffiles.sort()
Merger(pdffiles)
