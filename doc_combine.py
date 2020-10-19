import os
import glob
from docx import Document

cwd = os.getcwd()
mylist = os.listdir(cwd)

#docCounter = len(glob.glob1(cwd,"*.doc*"))

docList = glob.glob1(cwd,"*.doc*")

files = docList

def combine_docs(files):
    merged_document = Document()

    for index, file in enumerate(files):
        sub_doc = Document(file)

        if index < len(files)-1:
           sub_doc.add_page_break()

        for element in sub_doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save('combined.docx')

combine_docs(files)