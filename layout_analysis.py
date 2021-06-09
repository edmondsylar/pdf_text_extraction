from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

# bring in our document.
doc = open('files/2.pdf', 'rb')

# Create the resource manager.
rsc = PDFResourceManager()

# set parameters for analysis
laparams = LAParams()

# create a pdf page aggregator object.
device = PDFPageAggregator(rsc, laparams=LAParams)
interpreter = PDFPageInterpreter(rsc, device)

for page in PDFPage.get_pages(doc):
    interpreter.process_page(page)

    # receive the LTPage Object
    layout = device.get_results()
    for elem in layout:
        if isinstance(elem, LTTextBoxHorizontal):
            print(elem.get_text())