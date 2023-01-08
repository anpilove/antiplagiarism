import argparse
import ast
import tokenize
import re

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

class DictVisitor(ast.NodeVisitor):

    def visit_Dict(self,node):
        print('Node type: Dict\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)


    def visit_Constant(self,node):
        print('Node type: Constant\nFields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)


class Visitor(ast.NodeVisitor):

    def visit(self, node: ast.AST):
        list1 = []
        list1.append(ast.dump(node))
        self.generic_visit(node)
        return list1


def input_file_proc(name: str) -> list:
    """Processing of input file and get a list of file pairs for comparison"""
    list_files = []

    with open(name, "r", encoding="utf-8") as file:
        for line in file:
            list_files.append(line.rstrip("\n").split())

    return list_files


def file_proc(file_path: str):
    print(file_path)
    with open(file_path) as file:
        code = file.read()

    node = ast.parse(code)
    print(ast.dump(node, indent=4, ))
    list1 = Visitor().visit(node)
    # print(len(list1))
    # print(node)
    # print(node._fields)
    # print(node.body)
    list_text = []
    for i in node.body:
        list_text.append(ast.dump(i))
        ast.dump(i)
    print(list_text)
    return list_text
    # print(node.body[0]._fields)
    # json_code = ast.dump(node)
    # print(json_code)
    # print(type(json_code))


def compare(list_pair: list, file_name: str):
    for pair in list_pair:
        file_path_text1 = pair[0]
        file_path_text2 = pair[1]
        list1 = file_proc(file_path_text1)
        list2 = file_proc(file_path_text2)
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                print(sorted(list1[i].split(',')))
                print(sorted(list2[i].split(',')))
                word1 = " ".join(sorted(list1[i].split(',')))
                word2 = " ".join(sorted(list2[i].split(',')))
                print(LevenshteinDistance(word1,word2) , len(word1))
        break


# parser = argparse.ArgumentParser()
#
# parser.add_argument("input_file", help='File for input')
# parser.add_argument("output_file", help='File for output')
#
# args = parser.parse_args()
#
# input_file = args.input_file
# output_file = args.output_file


# input_file = "input.txt"
# output_file = "output.txt"
# list_files = input_file_proc(input_file)
#
# compare(list_files, output_file)


