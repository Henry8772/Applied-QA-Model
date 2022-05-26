import operator

from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, QuestionAnsweringPipeline


class ExtractAnswer:
    def __init__(self, model_name=None, tokenizer=None, model=None):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        # self.nlp = QuestionAnsweringPipeline(model=model, tokenizer=tokenizer)
        self.model_name = model_name or "deepset/roberta-base-squad2"
        self.nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

    def extract(self, question, passages):
        answers = []
        for passage in passages:
            content = passage['content']
            try:
                answer = self.nlp(question=question, context=content)
                answer['text'] = content
                answer['lecture'] = passage['lecture'] + " " + passage['page']
                answer['relevance'] = passage['relevance']
                answers.append(answer)

            except KeyError:
                pass
        answers.sort(key=operator.itemgetter('score'), reverse=True)
        return answers

    def answerWithContext(self, question, content):
        answer = self.nlp(question=question, context=content)
        return answer

