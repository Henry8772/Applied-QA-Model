import os

from components.ExtractAnswer import ExtractAnswer
from components.PassageRetriever import *
from components.QueryProcessor import QueryProcessor
import spacy
from flask import Flask, render_template, jsonify, request

SPACY_MODEL = os.environ.get('SPACY_MODEL', 'en_core_web_sm')
# QA_MODEL = os.environ.get('QA_MODEL', 'distilbert-base-cased-distilled-squad')
nlp = spacy.load(SPACY_MODEL, disable=['ner', 'parser', 'textcat'])
query_processor = QueryProcessor(nlp)
passage_retriever = PassageRetriever(nlp)
answer_extractor = ExtractAnswer("deepset/roberta-base-squad2")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/answer-question', methods=['POST'])
def analyzer():
    data = request.get_json()
    question = data.get('question')

    # query = query_processor.generate_query(question)

    documents = readAsJSON()
    passage_retriever.fit(documents)
    passages = passage_retriever.most_similar(question)
    # passages = passage_retriever.findPassage(documents, question)
    answers = answer_extractor.extract(question, passages)

    return jsonify(answers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    analyzer()
