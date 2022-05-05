import glob
import math
from tqdm import tqdm

from model import Model

import nltk
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords as sw


transformer = Model('deepset/roberta-base-squad2')

ps = PorterStemmer()

file_names = glob.glob('../Corpus/**/*.txt', recursive=True)
corpus_file_names = []

stopwords = sw.words('english')

for file_name in file_names:
    if file_name[-6:] != 'Qs.txt' and file_name[-6:] != 'As.txt':
        corpus_file_names.append(file_name)

#print(len(corpus_file_names))

tf_documents = dict()
idf_documents = dict()
num_docs = len(corpus_file_names)

def update_tf(tf_docs, token, doc_name):
    if doc_name not in tf_docs:
        tf_docs[doc_name] = {token: 1}
    else:
        if token not in tf_docs[doc_name]:
            tf_docs[doc_name][token] = 1
        else:
            tf_docs[doc_name][token] += 1   


def update_idf(idf_docs, token):
    if token not in idf_docs:
        idf_docs[token] = 1
    else:
        idf_docs[token] += 1

def calculate_tfidf(tf, idf, num_docs):
    return tf*math.log(float(num_docs)/float(idf))


for file_name in tqdm(corpus_file_names):
    with open(file_name, 'r') as file:
        contents = word_tokenize(file.read())
        for word in contents:
            if word not in stopwords:
                update_tf(tf_documents, word, file_name)
                if tf_documents[file_name][word] == 1:
                    update_idf(idf_documents, word)
            

#question = 'What is the only divisor besides 1 that a prime number can have?'
#question = 'What are numbers greater than 1 that can be divided by 3 or more numbers called?'
#question = 'What is it called when people in society rebel against laws they think are unfair?'
#question = 'How many US presidents are alumni of the school?'
#question = 'Where can tourists go when they visit Cambridge?'

k = 10

with open('model_timing_test_2.txt', 'w+') as output_file:
    with open('../evaluation/Questions.txt', 'r') as questions_file:
        questions = questions_file.readlines()
        for i in tqdm(range(len(questions))):
            question = questions[i][:-1]

            question_tokenized = word_tokenize(question)

            best_score = float('-inf')
            best_file = ''
            second_best_file = ''
            second_best_score = float('-inf')
            
            best_documents = []

            for file_name in corpus_file_names:
                mag_q = 0
                mag_doc = 0
                numerator = 0
                for word in question_tokenized:
                    if word not in stopwords:
                        mag_q += 1
                        if word in idf_documents:
                            if word in tf_documents[file_name]:
                                tf_val = tf_documents[file_name][word]
                            else:
                                tf_val = 0
                            idf_val = idf_documents[word]
                            res = calculate_tfidf(tf_val, idf_val, num_docs)
                            mag_doc += res**2
                            numerator += res

                if (math.sqrt(float(mag_q)) * math.sqrt(float(mag_doc))) == 0:
                    cosine = float('-inf')
                else:
                    cosine = float(numerator) / (math.sqrt(float(mag_q)) * math.sqrt(float(mag_doc)))
                '''
                if cosine >= best_score:
                    if best_file != '':
                        second_best_file = best_file
                    best_file = file_name
                    best_score = cosine 
                '''

                best_documents.append((cosine, file_name))
            best_documents.sort(key=lambda x: x[0])
            best_documents.reverse()
            
            top_k_docs = best_documents[:k]


            #best_files = [best_file, second_best_file]
            #best_files = [best_file]
            best_answer = 'No Answer'
            best_answer_val = 0
            for c, best_file_name in top_k_docs:
                if best_file_name == '':
                    continue
                with open(best_file_name, 'r') as file:
                    print('processing: ', best_file_name)
                    contents = file.read().split(' ')
                    print(len(contents))
                    for i in range(0, len(contents), 500):
                        subsection = contents[i:i+500]
                        subsection = ' '.join(subsection)
                        QA_input = {
                            'question': question,
                            'context': subsection}
                        res = transformer.query(QA_input)
                        if res['score'] > best_answer_val and res['score'] > 0.5:
                            best_answer = res['answer']
                            best_answer_val = res['score']
            output_file.write(best_answer+'\n')

        











