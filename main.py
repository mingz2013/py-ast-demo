# -*- coding:utf-8 -*-
"""
"""
__date__ = "2019/11/22"
__author__ = "zhaojm"

import ast, astunparse
from visitor import CodeVisitor
import codecs

r_node = ast.parse(file('conf.py').read())

visitor = CodeVisitor()
visitor.visit(r_node)
# print(type(r_node))
# print(ast.dump(r_node))
print(astunparse.dump(r_node))
s = astunparse.unparse(r_node)
print(s)

with codecs.open('conf2.py', mode='w', encoding='utf8') as f:
    f.write(s)



# exec compile(r_node, '<string>', 'exec')
