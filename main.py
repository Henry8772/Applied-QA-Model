from PassageRetriever import *
from pdfExtractor import *


def extractPDF():
    readPerPage('assets/test.pdf')
    saveAsJSON()


def passageRetrieve():
    documents = readAsJSON()
    pr = PassageRetriever()
    print(pr.findDoc(documents, "What is heap tree structure"))


if __name__ == '__main__':
    passageRetrieve()
