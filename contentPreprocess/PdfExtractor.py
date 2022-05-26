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
        self.root_dir = root_dir or '../assets/FDS_PPT'
        self.file_paths = []
        self.title = ""
        self.lecture_num = ""

    def readPdf(self, path_to_pdf):
        print("Reading", path_to_pdf)
        fp = open(path_to_pdf, 'rb')
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        page_no = 0
        content = {}
        for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
            interpreter.process_page(page)
            context = retstr.getvalue()
            if pageNumber == page_no and pageNumber == 0:

                self.process_front_page(context)

                m = re.search('\n1 Video: (.+?)1', context)
                if m:
                    context = m.group(1)
                content['content'] = context
                content['lecture'] = self.title
                content['page'] = str(page_no)
                self.contentsByPage[self.title + "_" + str(pageNumber)] = content
                content = {}

            elif pageNumber == page_no and self.title != "empty":
                print("Reading page", pageNumber)

                data = self.process_content(context)[:-1]
                content['content'] = data
                content['lecture'] = self.title
                content['page'] = str(page_no)
                self.contentsByPage[self.title + "_" + str(pageNumber)] = content
                content = {}

            retstr.truncate(0)
            retstr.seek(0)

            page_no += 1
        print("Finished")


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
        content = {}
        for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
            interpreter.process_page(page)
            if pageNumber == page_no and pageNumber == 0:

                self.process_front_page(retstr.getvalue())

            elif pageNumber == page_no and self.title != "empty":
                print("Reading page", pageNumber)

                data = self.process_content(retstr.getvalue())[:-1]
                content['content'] = data
                content['lecture'] = self.title
                content['page'] = str(page_no)
                self.contentsByPage[self.lecture_num + "_" + str(pageNumber)] = content
                content = {}


            retstr.truncate(0)
            retstr.seek(0)

            page_no += 1
        print("Finished")

    def process_content(self, content):
        #For RAA
        # content = "\n\n".join(content.split("\n\n")[3:])
        replaceDict = {r'\ﬁ': 'fi', r'\ﬃ': 'ffi', r'IADS\u2013 .* \u2013 .*': ''}

        # r'(\n+)': ':',
        for k, v in replaceDict.items():
            content = re.sub(k, v, content)
        return content

    def process_front_page(self, content):
        # m = re.search('\nLecture(.+?)\n\n', content)
        # m = re.search('\nLecture(.+?)\n', content)
        m = re.search('\nTopic: (.+?)\n\n', content)
        if m:
            self.title = m.group(1)
            self.lecture_num = "0"
            # self.lecture_num = self.title.split(" ")[1].split(":")[0]
        else:
            self.title, self.lecture_num = "empty", "empty"

    def loop_through_all_files(self):

        for subdir, dirs, files in os.walk(self.root_dir):

            for file in files:
                self.file_paths.append(os.path.join(subdir, file))

    def read_all_files(self):
        print("Reading all files", self.file_paths)
        for path in self.file_paths:
            self.readPdf(path)

    def saveAsJSON(self):
        print("Saving as JSON file")
        # Serializing json
        json_object = json.dumps(self.contentsByPage, indent=4)

        # Writing to sample.json
        with open("../sample.json", "w") as outfile:
            outfile.write(json_object)


pdfExtractor = PdfExtractor()
# pdfExtractor.readPerPage('assets\RAA\17a.pdf')

pdfExtractor.loop_through_all_files()
pdfExtractor.read_all_files()
pdfExtractor.saveAsJSON()

# loop_through_all_files('assets\ppt')
# readPerPage('assets/test.pdf')
# saveAsJSON()
#
# readPerPage('test.pdf')
# print(" ".join(contentsByPage))
