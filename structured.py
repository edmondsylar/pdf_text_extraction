from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

def test_files(file):
    fp = open(file, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser, "password")

    # check text extratable
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed

    rsc = PDFResourceManager() #Resource Manager
    device = PDFDevice(rsc)
    interp = PDFPageInterpreter(rsc, device)

    for page in PDFPage.create_pages(doc):
        pg = interp.process_page(page)
        print(pg)


test_files('files/default.pdf')
test_files('files/1.pdf')
test_files('files/2.pdf')