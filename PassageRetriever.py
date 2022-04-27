import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def readAsJSON():
    with open('sample.json', 'r') as f:
        data = json.load(f)

    return data


class PassageRetriever:

    def __int__(self):
        self.n = 0

    def findDoc(self, documents, question):
        documents['0'] = question
        print(documents)
        tfidf = TfidfVectorizer().fit_transform(documents)
        print(tfidf[-1])
        cosine_similarities = linear_kernel(tfidf[-1], tfidf).flatten()
        related_docs_indices = cosine_similarities.argsort()[:-5:-1]
        return related_docs_indices
