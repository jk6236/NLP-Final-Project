import sys
import re
import os

def checkline():
    answers_list = []
    sample_output_list = []
    with open('Answers.txt', "r", encoding = "utf-8") as f1:
        for line in f1:
            answers_list.append(line)
    with open('model_answers_dummy.txt', "r", encoding = "utf-8") as f2:
        for line in f2:
            sample_output_list.append(line)
    count = 0
    correct = 0
    
    print ("There are ", len(answers_list), "line in answer key, and ", len(sample_output_list), "line in model output")
    for x in answers_list:
        result = -1
        base_word = answers_list[count]
        result = base_word.find(sample_output_list[count])
        if(result != -1):
            count = count + 1
        else:
            correct = correct + 1
            count = count + 1

    accuracy = correct/count
    print("Accuracy: ", accuracy)

checkline()
