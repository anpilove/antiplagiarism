import argparse
import ast
import numpy as np


def LevenshteinDistance(code1, code2):
    m, n = len(code1), len(code2)
    generator_array = [[0] * (n + 1) for i in range(m + 1)]
    array = np.array(generator_array)

    for i in range(m + 1):
        array[i][0] = i
    for j in range(n + 1):
        array[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if code1[i - 1] == code2[j - 1]:
                array[i][j] = array[i - 1][j - 1]
            else:
                array[i][j] = 1 + min(array[i - 1][j], array[i][j - 1], array[i - 1][j - 1])

    return array[-1][-1]


def input_file_proc(name: str) -> list:
    """Processing of input file and get a list of file pairs for comparison"""
    list_files = []

    with open(name, "r", encoding="utf-8") as file:
        for line in file:
            list_files.append(line.rstrip("\n").split())

    return list_files


def file_proc(file_path: str):
    with open(file_path) as file:
        code = file.read()

    node = ast.parse(code)
    list_text = []
    for i in node.body:
        list_text.append(ast.dump(i))
    return list_text



def compare(list_pair: list, file_name: str):

    list_scores = []  # list for write all scores

    for pair in list_pair:  # compare pairs of files
        file_path_text1 = pair[0]
        file_path_text2 = pair[1]
        list1 = sorted(file_proc(file_path_text1))  # get code1
        list2 = sorted(file_proc(file_path_text2))  # get code2

        len_list1 = len(list1)  # parts of code1
        len_list2 = len(list2)  # parts of code2

        """Equalize the length"""
        if len_list1 > len_list2:
            for i in range(len_list1 - len_list2):
                list2.append([])

        elif len_list1 < len_list2:
            for i in range(len_list2 - len_list1):
                list1.append([])

        list_similarity = []
        for i in range(max(len(list1), len(list2))):

            if list1[i] != list2[i] and list1[i] != [] and list2[i] != []:
                code1 = " ".join(sorted(list1[i].split(',')))
                code2 = " ".join(sorted(list2[i].split(',')))
                similarity = 1 - (LevenshteinDistance(code1, code2) / max(len(code1), len(code2)))
                list_similarity.append(similarity)

        for i in range(min(len_list1,len_list2) - len(list_similarity)):
            list_similarity.append(1)

        list_scores.append(sum(list_similarity) / len(list_similarity))

        with open(file_name,"w", encoding= "utf-8") as file:
            for score in list_scores:
                file.write(str(score) + '\n')



parser = argparse.ArgumentParser()

parser.add_argument("input_file", help='File for input')
parser.add_argument("output_file", help='File for output')

args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file


input_file = "input.txt"
output_file = "output.txt"
list_files = input_file_proc(input_file)

compare(list_files, output_file)

