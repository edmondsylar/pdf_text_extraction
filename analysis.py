from pprint import pp, pprint
from io import StringIO
import re
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from lxml import html

# ignored from margins here.

invoice_style = "position:absolute; border: textbox 1px solid; writing-mode:lr-tb; left:328px; top:254px; width:70px; height:14px;"

description_style = "position:absolute; border: textbox 1px solid; writing-mode:lr-tb; left:59px; top:411px; width:150px; height:9px;"

output = StringIO()

def _():
    with open('files/default.pdf', 'rb') as pd:
        extract_text_to_fp(pd, output, laparams=LAParams(), output_type='html', codec=None)

        # we have converted the document into raw html.
        raw_html = output.getvalue()

        # extract all the div tags.
        tree = html.fromstring(raw_html)
        divs = tree.xpath('.//div')

        #Sort and filter the div tag.
        filtered_divs = {'ID': [], 'More-detail': []}
        for div in divs:
            dv_style = div.get('style')
            if dv_style == invoice_style:
                # print(dv_style, "Target Div Located")
                invoice_number = div.text_content().strip('\n')
                # print(invoice_number)

def get_invoice_number(file):
    output = StringIO()
    with open(file, 'rb') as pd:
        extract_text_to_fp(pd, output, laparams=LAParams(), output_type='html', codec=None)

        # we have converted the document into raw html.
        raw_html = output.getvalue()

        # extract all the div tags.
        tree = html.fromstring(raw_html)
        divs = tree.xpath('.//div')

        #Sort and filter the div tag.
        filtered_divs = {'ID': [], 'More-detail': []}
        for div in divs:
            dv_style = div.get('style')
            if dv_style == invoice_style:
                # print(dv_style, "Target Div Located")
                invoice_number = div.text_content().strip('\n')
                return (invoice_number)

        print('No invoice Number found in the document presented')
        return False


def get_invoice_description(file):
    output = StringIO()
    with open(file, 'rb') as pd:
        extract_text_to_fp(pd, output, laparams=LAParams(), output_type='html', codec=None)

        # we have converted the document into raw html.
        raw_html = output.getvalue()

        # extract all the div tags.
        tree = html.fromstring(raw_html)
        divs = tree.xpath('.//div')

        #Sort and filter the div tag.
        filtered_divs = {'ID': [], 'More-detail': []}
        for div in divs:
            dv_style = div.get('style')
            if dv_style == description_style:
                # print(dv_style, "Target Div Located")
                invoice_number = div.text_content().strip('\n')
                return (invoice_number)

        print('Not a valid DHL Invoice file')
        return False

# description = get_invoice_description('files/1.pdf')
# inv_number = get_invoice_number('files/1.pdf')

# print('Invoice Number: {} \nDescription: {}'.format(inv_number, description))