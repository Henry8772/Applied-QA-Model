import os

import spacy

from components.PassageRetriever import PassageRetriever, readAsJSON
from components.ExtractAnswer import ExtractAnswer



SPACY_MODEL = os.environ.get('SPACY_MODEL', 'en_core_web_sm')
# QA_MODEL = os.environ.get('QA_MODEL', 'distilbert-base-cased-distilled-squad')
nlp = spacy.load(SPACY_MODEL, disable=['ner', 'parser', 'textcat'])
passage_retriever = PassageRetriever(nlp)
answer_extractor = ExtractAnswer("deepset/roberta-base-squad2")



def testPassage():
    question = "what are problems with high dimensional data"
    documents = readAsJSON()
    passage_retriever.fit(documents)
    passages = passage_retriever.most_similar(question)
    print(passages)
    # answers = answer_extractor.extract(question, passages)
    # print(answers)

def testAnswerWithContent():
    content = "There is also another problem with high-dimensional data, called the curse of dimensionality: essentially a large number of dimensions makes is harder for distance-based methods such as clustering\nand nearest neighbours to work effectively – we’ll come back to the curse of dimensionality in the\nfollowing lectures on clustering and nearest-neighbour methods."
    answer = answer_extractor.answerWithContext("what are problems with high dimensional data", content)
    print(answer)


testAnswerWithContent()
