import os

import spacy

from PassageRetriever import PassageRetriever, readAsJSON

SPACY_MODEL = os.environ.get('SPACY_MODEL', 'en_core_web_sm')
# QA_MODEL = os.environ.get('QA_MODEL', 'distilbert-base-cased-distilled-squad')
nlp = spacy.load(SPACY_MODEL, disable=['ner', 'parser', 'textcat'])
passage_retriever = PassageRetriever(nlp)


def testPassage():
    question = "STRIPS"
    documents = readAsJSON()
    passage_retriever.fit(documents)
    passages = passage_retriever.most_similar(question)
    print(passages)


def reformatPdf():
    documents = readAsJSON()
    for i in documents.values():
        content = i['content']
        print(content)


testPassage()
