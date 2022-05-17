import os

import spacy

from PassageRetriever import PassageRetriever, readAsJSON
from app import answer_extractor

SPACY_MODEL = os.environ.get('SPACY_MODEL', 'en_core_web_sm')
# QA_MODEL = os.environ.get('QA_MODEL', 'distilbert-base-cased-distilled-squad')
nlp = spacy.load(SPACY_MODEL, disable=['ner', 'parser', 'textcat'])
passage_retriever = PassageRetriever(nlp)

def testPassage():
    question = "What is the runtime of insertion sort"
    documents = readAsJSON()
    passage_retriever.fit(documents)
    passages = passage_retriever.most_similar(question)
    print(passages)
    answers = answer_extractor.extract(question, passages)
    print(answers)

testPassage()