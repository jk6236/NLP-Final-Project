import sys
import re
import os
import random
import filecmp

def checkline():
    f1 = open('Answers.txt', 'r')
    file_contents1 = f1.read()
    print (file_contents1)
    f1.close()
    f2 = open('Sample_Model_Output.txt', 'r')
    file_contents2 = f2.read()
    print(file_contents2)
    f2.close()
checkline()