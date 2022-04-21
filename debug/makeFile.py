import os
import sys
import re
from pathlib import Path

path = Path(r"C:\Users\jkim6\Desktop\Natural Language Processing\NLP-Final-Project\Corpus")

for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        path_name = str(os.path.join(root, name))
        if(path_name.find("Qs.txt") > 0):
            with open(path_name, "r", encoding = "utf-8") as questionfile:
                with open("Questions.txt", "w", encoding = "utf-8") as Questionsfile:
                    for line in questionfile:
                        Questionsfile.write(line)
        elif(path_name.find("As.txt") > 0):
            with open(path_name, "r", encoding = "utf-8") as answerfile:
                with open("Sample_Model_Output.txt", "w", encoding = "utf-8") as samplefile:
                    for line in answerfile:
                        samplefile.write(line)