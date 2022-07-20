import itertools
import json
import os

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import linear_kernel
from gensim.summarization.bm25 import BM25


def readAsJSON():
    with open('export.json', 'rb') as f:
        data = json.load(f)

    return data


class PassageRetriever:

    def __init__(self, nlp):
        self.tokenize = lambda text: [token.lemma_ for token in nlp(text)]
        self.bm25 = None
        self.passages = None

    def preprocess(self, doc):
        passages = [p for p in doc.split('\n') if p and not p.startswith('=')]
        return passages

    def fit(self, docs):
        # passages = list(itertools.chain(*map(self.preprocess, docs)))
        corpus = [self.tokenize(p['content']) for p in docs.values()]
        self.bm25 = BM25(corpus)
        self.passages = docs

    def most_similar_passages(self, question, topn=3):
        tokens = self.tokenize(question)
        scores = self.bm25.get_scores(tokens)
        indices = argsort(scores)[-topn:]
        doc_key = list(self.passages)
        related_passage = [self.passages[doc_key[i]] for i in indices]

        for ind, x in enumerate(indices):
            related_passage[ind]['relevance'] = scores[x]

        # related_passages = [ == scores[i] for i in range(len(indices))]
        return related_passage

        # return indices

    # def most_similiar_paragraphs(self, passges_index):


    # def findPassage(self, documents, question):
    #     # documents['question'] = question
    #     tfidf = TfidfVectorizer().fit_transform(documents)
    #     tf_que = TfidfVectorizer().fit_transform(question)
    #     cosine_similarities = linear_kernel(tf_que, tfidf).flatten()
    #     related_docs_indices = cosine_similarities.argsort()[:-5:-1]
    #     # doc_key = list(documents)
    #     related_passage = [documents[doc_key[i]] for i in related_docs_indices]
    #     return related_passage


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


