from passgeRetriver import *
from pdfExtractor import *


def extractPDF():

    readPerPage('assets/test.pdf')
    saveAsJSON()


if __name__ == '__main__':
    extractPDF()
