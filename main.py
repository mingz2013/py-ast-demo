# -*- coding:utf-8 -*-
"""
"""
__date__ = "2019/11/22"
__author__ = "zhaojm"

import ast, astunparse

func_def = \
    """
    def add(x, y):
        return x + y
    print(add(3, 5))
    """

# r_node = ast.parse(func_def)
# print(ast.dump(r_node))
# print(astunparse.dump(r_node))
# print(astunparse.unparse(r_node))

import codecs

r_node = ast.parse(file('test.py').read())

print(type(r_node))
print(ast.dump(r_node))
print(astunparse.dump(r_node))
print(astunparse.unparse(r_node))
