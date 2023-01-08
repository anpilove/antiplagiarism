import argparse
import numpy
import ast
import tokenize
import re


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


def file_proc(file_name: str):
    print(file_name)
    with open(file_name) as file:
        code = file.read()

    node = ast.parse(code)
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
                print(list1[i])
                print(list2[i])
                print()
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
input_file = "input.txt"
output_file = "output.txt"
list_files = input_file_proc(input_file)

compare(list_files, output_file)
