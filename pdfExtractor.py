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


def processContent(content):
    replaceDict = {r'(\n+)': ' ', r'\ﬁ': 'fi', r'\ﬃ': 'ffi', r'IADS\u2013 .* \u2013 .*': ''}
    for k, v in replaceDict.items():
        content = re.sub(k, v, content)
    return content


def readPerPage(path_to_pdf):
    global contentsByPage
    fp = open(path_to_pdf, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    page_no = 0
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no and pageNumber != 0:
            interpreter.process_page(page)

            data = processContent(retstr.getvalue())[:-1]
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


readPerPage('assets/test.pdf')
saveAsJSON()
#
# readPerPage('test.pdf')
# print(" ".join(contentsByPage))
