import io
import json
import os
import re
import sys
import pandas as pd

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage
from os import listdir
from os.path import isfile, join
from pdfminer.high_level import extract_text

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


class PdfExtractor:

    def __init__(self, root_dir=None):
        self.current_file_content = {}
        self.current_file_df = pd.DataFrame(columns=["title", "paragraphs"])
        self.root_dir = root_dir or '../assets/FDS_PPT'
        self.file_paths = []
        self.title = ""
        self.lecture_num = ""



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
                content['title'] = self.title
                content['page'] = str(page_no)
                self.current_file_content[self.lecture_num + "_" + str(pageNumber)] = content
                content = {}

            retstr.truncate(0)
            retstr.seek(0)

            page_no += 1
        print("Finished")

    def process_content(self, content):
        # For RAA
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
        json_object = json.dumps(self.current_file_content, indent=4)

        # Writing to sample.json
        with open("../sample.json", "w") as outfile:
            outfile.write(json_object)

    def convert_pdf(self, min_length=200, include_line_breaks=False):
        """
        Function to convert PDFs to Dataframe with columns as title & paragraphs.

        Parameters
        ----------

        min_length : integer
            Minimum character length to be considered as a single paragraph

        include_line_breaks: bool
            To concatenate paragraphs less than min_length to a single paragraph



        Returns
        -------------
        df : Dataframe


        Description
        -----------------
        If include_line_breaks is set to True, paragraphs with character length
        less than min_length (minimum character length of a paragraph) will be
        considered as a line. Lines before or after each paragraph(length greater
        than or equal to min_length) will be concatenated to a single paragraph to
        form the list of paragraphs in Dataframe.

        Else paragraphs are appended directly to form the list.

        """
        list_file = os.listdir(self.root_dir)
        list_pdf = []
        for file in list_file:
            if file.endswith("pdf"):
                list_pdf.append(file)
        pdf_content = pd.DataFrame(columns=["title", "content"])
        for i, pdf in enumerate(list_pdf):
            try:
                pdf_content.loc[i] = [pdf.replace(".pdf", ''), None]
                raw = extract_text(os.path.join(self.root_dir, pdf))
                s = raw.strip()
                paragraphs = re.split("\n\n(?=\u2028|[A-Z-0-9])", s)
                list_par = []
                temp_para = ""  # variable that stores paragraphs with length<min_length
                # (considered as a line)
                for p in paragraphs:
                    if not p.isspace():  # checking if paragraph is not only spaces
                        if include_line_breaks:  # if True, check length of paragraph
                            if len(p) >= min_length:
                                if temp_para:
                                    # if True, append temp_para which holds concatenated
                                    # lines to form a paragraph before current paragraph p
                                    list_par.append(temp_para.strip())
                                    temp_para = (
                                        ""
                                    )  # reset temp_para for new lines to be concatenated
                                    list_par.append(
                                        p.replace("\n", "")
                                    )  # append current paragraph with length>min_length
                                else:
                                    list_par.append(p.replace("\n", ""))
                            else:
                                # paragraph p (line) is concatenated to temp_para
                                line = p.replace("\n", " ").strip()
                                temp_para = temp_para + f" {line}"
                        else:
                            # appending paragraph p as is to list_par
                            list_par.append(p.replace("\n", " "))
                    else:
                        if temp_para:
                            list_par.append(temp_para.strip())
                # pdf_content.at[i, "content"] = "\n".join(list_par)
                pdf_content.at[i, "content"] = list_par

            except:
                print("Unexpected error:", sys.exc_info()[0])
                print("Unable to process file {}".format(pdf))

        return pdf_content

    def save_df_as_json(self, content):
        data = content.to_json('../export.json', orient='index')

    # def readPdf(self, path_to_pdf):
    #     print("Reading", path_to_pdf)
    #     fp = open(path_to_pdf, 'rb')
    #     rsrcmgr = PDFResourceManager()
    #     retstr = io.StringIO()
    #     codec = 'utf-8'
    #     laparams = LAParams()
    #     device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    #     interpreter = PDFPageInterpreter(rsrcmgr, device)
    #
    #     page_no = 0
    #     content = {}
    #     for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
    #         interpreter.process_page(page)
    #         context = retstr.getvalue()
    #         if pageNumber == page_no and pageNumber == 0:
    #
    #             self.process_front_page(context)
    #
    #             m = re.search('\n1 Video: (.+?)1', context)
    #             if m:
    #                 context = m.group(1)
    #             content['content'] = context
    #             content['lecture'] = self.title
    #             content['page'] = str(page_no)
    #             self.current_file_content[self.title + "_" + str(pageNumber)] = content
    #             content = {}
    #
    #         elif pageNumber == page_no and self.title != "empty":
    #             print("Reading page", pageNumber)
    #
    #             data = self.process_content(context)[:-1]
    #             content['content'] = data
    #             content['lecture'] = self.title
    #             content['page'] = str(page_no)
    #             self.current_file_content[self.title + "_" + str(pageNumber)] = content
    #             content = {}
    #
    #         retstr.truncate(0)
    #         retstr.seek(0)
    #
    #         page_no += 1
    #     print("Finished")

pdfExtractor = PdfExtractor()
# pdfExtractor.readPerPage('assets\RAA\17a.pdf')

# pdfExtractor.loop_through_all_files()
# pdfExtractor.read_all_files()
# pdfExtractor.saveAsJSON()


df = pdfExtractor.convert_pdf()
df.head()
pdfExtractor.save_df_as_json(df)

# loop_through_all_files('assets\ppt')
# readPerPage('assets/test.pdf')
# saveAsJSON()
#
# readPerPage('test.pdf')
# print(" ".join(contentsByPage))
