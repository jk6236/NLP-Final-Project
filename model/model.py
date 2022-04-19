from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

import torch
import tqdm

class Model:
    def __init__(self, model_name):
        #From hugging face documentation
        self.model = pipeline('question-answering', model=model_name, tokenizer=model_name)

    def query(self, question_corpus):
        result = self.model(question_corpus)
        return result





