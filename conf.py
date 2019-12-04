# -*- coding:utf-8 -*-
"""
"""
__date__ = "2019/11/22"
__author__ = "zhaojm"


class Conf(object):
    def __init__(self):
        self.A = [1, 2, Conf()]
        self.B = 2
        self.C = '1'
        pass


c = Conf()
