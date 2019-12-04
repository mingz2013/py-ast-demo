# -*- coding:utf-8 -*-
"""
"""
__date__ = "2019/12/4"
__author__ = "zhaojm"


class Test(object):
    A = 1

    def __init__(self):
        self.data = {
            'B': 1
        }

        self.__dict__['C'] = 2

    def __getattribute__(self, item):
        return self.data.get(item)

    def __getattr__(self, item):
        return self.data.get(item)

    def __getitem__(self, item):
        return self.data.get(item)
