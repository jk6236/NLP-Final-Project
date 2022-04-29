import sys
import re
import os

def checkline():
    answers_list = []
    sample_output_list = []
    with open('Answers.txt', "r", encoding = "utf-8") as f1:
        for line in f1:
            answers_list.append(line.strip('\n').split('|'))
    with open('../model/model_baseline_param_25.txt', "r", encoding = "utf-8") as f2:
        for line in f2:
            sample_output_list.append(line.strip('\n'))
    count = 0
    correct = 0
   
    #print(answers_list[:5])
    #print(sample_output_list[:5])

    print ("There are ", len(answers_list), "line in answer key, and ", len(sample_output_list), "line in model output")
    
    for x in answers_list:
        result = -1
        base_word = answers_list[count]
        result = sample_output_list[count] in base_word
        #print(base_word, sample_output_list[count], result)
        if(result == False):
            count = count + 1
        else:
            correct = correct + 1
            count = count + 1

    accuracy = correct/count
    print("correct ", correct, " total ", count)
    print("Accuracy: ", accuracy)

checkline()
