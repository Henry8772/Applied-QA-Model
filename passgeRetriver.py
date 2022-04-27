from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def passageRetriver(documents):
    tfidf = TfidfVectorizer().fit_transform(documents)

    cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-5:-1]
    return related_docs_indices


# passageRetriver()
