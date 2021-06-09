import PyPDF2 
from tabula import read_pdf

# Get the number of pages in the file
pdfFileObj = open('files/default.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
n_pages = pdfReader.getNumPages()

# For each page the table can be read with the following code
table_pdf = read_pdf(pdf_file, guess=False, pages = 1, stream=True , encoding="utf-8", area = (96,24,558,750), columns = (24,127,220,274,298,325,343,364,459,545,591,748))