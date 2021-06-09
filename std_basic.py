from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

# open the pdf file.
fp = open('files/default.pdf', 'rb')

# create a pdf parser object associated with the file object.
parser = PDFParser(fp)

# create a pdf document that stores the document structure.
#  ?? providing a password but is the password really required?
# document = PDFDocument(parser, "password")
document = PDFDocument(parser)

# check if text extraction is allowed

if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# create a pdf resource manager object that stores shared resoruces
rsmgr = PDFResourceManager()

# creata a pdf device object
device = PDFDevice(rsmgr) #The device takes the resource manager as a variable.

# create a pdf interpreter object 
interpreter = PDFPageInterpreter(rsmgr, device)

# process each page contained in the document

for page in PDFPage.create_pages(document):
    page_ = interpreter.process_page(page)
    print(page_)


# Perfomning Layout Analysis