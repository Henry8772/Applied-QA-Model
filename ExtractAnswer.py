import operator

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, QuestionAnsweringPipeline


class ExtractAnswer:
    def __init__(self, model_name=None, tokenizer=None, model=None):
        # tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        # model = AutoModelForQuestionAnswering.from_pretrained(model)
        # self.nlp = QuestionAnsweringPipeline(model=model, tokenizer=tokenizer)
        self.model_name = model_name or "deepset/roberta-base-squad2"
        self.nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    def extract(self, question, passages):
        answers = []
        for passage in passages:
            try:
                answer = self.nlp(question=question, context=passage)
                answer['text'] = passage
                answers.append(answer)
            except KeyError:
                pass
        answers.sort(key=operator.itemgetter('score'), reverse=True)
        return answers
