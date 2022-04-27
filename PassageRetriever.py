import itertools
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def readAsJSON():
    with open('sample.json', 'r') as f:
        data = json.load(f)

    return data


class PassageRetriever:

    def __init__(self, nlp=None):
        self.tokenize = lambda text: [token.lemma_ for token in nlp(text)]
        self.bm25 = None
        self.passages = None

    def findPassage(self, documents, question):
        documents['0'] = question
        tfidf = TfidfVectorizer().fit_transform(documents)
        cosine_similarities = linear_kernel(tfidf[-1], tfidf).flatten()
        related_docs_indices = cosine_similarities.argsort()[:-5:-1]
        related_passage = [documents[str(i)] for i in related_docs_indices]
        return related_passage
