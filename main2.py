# -*- coding:utf-8 -*-
"""
"""
__date__ = "2019/12/4"
__author__ = "zhaojm"

import ast

import astunparse


def init_module():
    node = ast.Module(body=[])

    date_assign = ast.Assign(targets=[ast.Name(id='__date__', ctx=ast.Store())], value=ast.Str(s='2019/11/22'))

    node.body.append(date_assign)

    author_assign = ast.Assign(targets=[ast.Name(id='__author__', ctx=ast.Store())], value=ast.Str(s='zhaojm'))

    node.body.append(author_assign)

    return node


def new_class_def():
    node = ast.ClassDef(
        name='Conf',
        bases=[
            ast.Name(
                id='object',
                ctx=ast.Load()
            )],
        body=[
            ast.FunctionDef(
                name='__init__',
                args=ast.arguments(
                    args=[ast.Name(
                        id='self',
                        ctx=ast.Param())],
                    vararg=None,
                    kwarg=None,
                    defaults=[]),
                body=[
                    ast.Assign(
                        targets=[ast.Attribute(
                            value=ast.Name(
                                id='self',
                                ctx=ast.Load()),
                            attr='AA',
                            ctx=ast.Store())],
                        value=ast.List(
                            elts=[],
                            ctx=ast.Load())),
                    ast.Assign(
                        targets=[ast.Attribute(
                            value=ast.Name(
                                id='self',
                                ctx=ast.Load()),
                            attr='BB',
                            ctx=ast.Store())],
                        value=ast.Num(n=2))
                ],
                decorator_list=[]
            )
        ],
        decorator_list=[]
    )
    return node


m = init_module()

m.body.append(new_class_def())

print(astunparse.unparse(m))
