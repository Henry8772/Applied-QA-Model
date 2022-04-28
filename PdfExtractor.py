import io
import json
import os
import re
import sys

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
from os import listdir
from os.path import isfile, join

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


class PdfExtractor:

    def __init__(self, root_dir=None):
        self.contentsByPage = {}
        self.root_dir = root_dir or 'assets\ppt'
        self.file_paths = []

    def processContent(self, content):
        replaceDict = {r'(\n+)': ' ', r'\ﬁ': 'fi', r'\ﬃ': 'ffi', r'IADS\u2013 .* \u2013 .*': ''}
        for k, v in replaceDict.items():
            content = re.sub(k, v, content)
        return content

    def readPerPage(self, path_to_pdf):
        print("Reading", path_to_pdf)
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

                data = self.processContent(retstr.getvalue())[:-1]
                self.contentsByPage[pageNumber] = data
                retstr.truncate(0)
                retstr.seek(0)

            page_no += 1

    def loop_through_all_files(self):

        for subdir, dirs, files in os.walk(self.root_dir):
            for file in files:
                self.file_paths.append(os.path.join(subdir, file))

    def read_all_files(self):
        for path in self.file_paths:
            self.readPerPage(path)

    def saveAsJSON(self):
        print("Saving as JSON file")
        # Serializing json
        json_object = json.dumps(self.contentsByPage, indent=4)

        # Writing to sample.json
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)


pdfExtractor = PdfExtractor()
pdfExtractor.loop_through_all_files()
pdfExtractor.read_all_files()

# loop_through_all_files('assets\ppt')
# readPerPage('assets/test.pdf')
# saveAsJSON()
#
# readPerPage('test.pdf')
# print(" ".join(contentsByPage))
