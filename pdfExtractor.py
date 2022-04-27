import io
import json
import re
import sys

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

contentsByPage = {}


def get_pdf_file_content(path_to_pdf):
    resource_manager = PDFResourceManager(caching=True)

    out_text = StringIO()

    laParams = LAParams()
    text_converter = TextConverter(resource_manager, out_text, laparams=laParams)
    fp = open(path_to_pdf, 'rb')

    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = out_text.getvalue()

    fp.close()
    text_converter.close()
    out_text.close()

    return text


def processContent(content):
    return re.sub(r'(\n+)', ' ', content)


def readPerPage(path_to_pdf):
    global contentsByPage
    fp = open(path_to_pdf, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    print(type(retstr))
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    page_no = 0
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no and pageNumber == 2:
            interpreter.process_page(page)

            data = processContent(retstr.getvalue())[:-1]

            # print(data.encode('utf-8'))
            contentsByPage[pageNumber] = data
            retstr.truncate(0)
            retstr.seek(0)

        page_no += 1
    print(contentsByPage)


def saveAsJSON():
    global contentsByPage
    # Serializing json
    json_object = json.dumps(contentsByPage, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

#
# readPerPage('test.pdf')
# print(" ".join(contentsByPage))
