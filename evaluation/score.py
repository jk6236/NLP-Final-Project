import sys
import re
import os
import random
import filecmp
import difflib

def checkline():
    with open('Answers.txt') as file_1:
        file_1_text = file_1.readlines()
  
    with open('Sample_Model_Output.txt') as file_2:
        file_2_text = file_2.readlines()
  
    # Find and print the diff:
    for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='Answers.txt', 
        tofile='Sample_Model_Output.txt', lineterm=''):
        print(line)
checkline()