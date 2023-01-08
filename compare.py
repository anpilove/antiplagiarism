import argparse

import numpy
import ast
import tokenize
import re

class Visitor(ast.NodeVisitor):

    def visit_For(self, node: ast.AST):
        print(node)
        self.generic_visit(node)


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
    print(node)
    print(node._fields)
    print(node.body)
    print(node.body[0]._fields)
    print(ast.dump(node))



def compare(list_pair: list):
    for pair in list_pair:
        file_path_text1 = pair[0]
        file_path_text2 = pair[1]
        file_proc(file_path_text1)
        file_proc(file_path_text2)
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

compare(list_files)
