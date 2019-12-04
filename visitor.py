# -*- coding:utf-8 -*-
"""
"""
__date__ = "2019/12/4"
__author__ = "zhaojm"

import ast


class CodeVisitor(ast.NodeVisitor):
    # def visit_BinOp(self, node):
    #     if isinstance(node.op, ast.Add):
    #         node.op = ast.Sub()
    #     self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if node.name == '__init__':
            self.generic_visit(node)
            # func_log_stmt = ast.Print(
            #     dest=None,
            #     values=[ast.Str(s='calling func: %s' % node.name, lineno=0, col_offset=0)],
            #     nl=True,
            #     lineno=0,
            #     col_offset=0,
            # )

            stmt = ast.Assign(
                targets=[ast.Attribute(
                    value=ast.Name(
                        id='self',
                        ctx=ast.Load()),
                    attr='AA',
                    ctx=ast.Store())],
                value=ast.List(
                    elts=[],
                    ctx=ast.Load()))

            stmt_num = ast.Assign(
                targets=[ast.Attribute(
                    value=ast.Name(
                        id='self',
                        ctx=ast.Load()),
                    attr='BB',
                    ctx=ast.Store())],
                value=ast.Num(n=2)
            )

            node.body.insert(0, stmt)
            node.body.insert(1, stmt_num)



            # def visit_(self, node):
