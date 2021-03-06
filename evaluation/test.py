import sys
import re
import os

def checkline():
    answers_list = []
    sample_output_list = []
    with open('Answers.txt', "r", encoding = "utf-8") as f1:
        for line in f1:
            answers_list.append(line.strip('\n').split('|'))
    with open('../model/model_final_1_50.txt', "r", encoding = "utf-8") as f2:
        for line in f2:
            sample_output_list.append(line.strip('\n'))
    count = 0
    correct = 0
    
    #groundTruth_modelOutput, F = NoAnswer, T = AnswerExists
    F_F = 0
    T_F = 0
    F_T = 0
    T_T = 0
    model_no_answer = 0


    #print(answers_list[:5])
    #print(sample_output_list[:5])

    print ("There are ", len(answers_list), "line in answer key, and ", len(sample_output_list), "line in model output")
    
    for x in answers_list:
        result = -1
        base_word = answers_list[count]
        result = sample_output_list[count] in base_word
        

        if base_word[0] == 'No Answer':
            if sample_output_list[count] == 'No Answer':
                F_F += 1
            else:
                F_T += 1
        else:
            if sample_output_list[count] == 'No Answer':
                T_F += 1
            else:
                T_T += 1

        if result == False:
            if sample_output_list[count] == 'No Answer':
                model_no_answer += 1


        if(result == False):
            count = count + 1
        else:
            correct = correct + 1
            count = count + 1

    accuracy = correct/count
    print("correct ", correct, " total ", count)
    print("Accuracy: ", accuracy)

    print("F_F : ", F_F, "F_T : ", F_T, "T_F : ", T_F, "T_T : ", T_T)
    print(model_no_answer)

checkline()
