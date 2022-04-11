import sys
import re
import os
import random
import filecmp
import difflib

def checkline():
    answers_list = []
    sample_output_list = []
    with open('Answers.txt') as f1:
        for line in f1:
            answers_list.append(line)
    with open('Sample_Model_Output.txt') as f2:
        for line in f2:
            sample_output_list.append(line)
    #print(answers_list)
    #print(sample_output_list)
    count = 0
    for x in answers_list:
        result = -1
        base_word = answers_list[count]
        result = base_word.find(sample_output_list[count])
        if(result != -1):
            print(result)
        else:
            print(result)
        count = count + 1
    

checkline()