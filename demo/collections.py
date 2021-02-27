# -*- coding:utf-8 -*-

# ================================
# @Time   : 2021/2/21 18:35
# @File   : collections.py
# @Author : WU
# ================================

class Collections:
    def __init__(self):
        self.s = set()

    def add(self, *args, **kwargs):
        self.s.update(*args)
        print(self.s)

    # def __str__(self):
    #     return '集合现有数据 %s' % self.s


if __name__ == '__main__':
    co = Collections()
    params = [1, 2, 3]
    co.add(params)
