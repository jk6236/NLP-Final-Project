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
    print(answers_list)
    print(sample_output_list)

checkline()