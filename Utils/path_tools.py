#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : path_tools.py
# @Time  : 2020-12-17 10:12
# @Author: WU
# ==============================
import os


class PathTools:

    def __init__(self):
        self.curr_path = os.path.abspath(os.path.dirname(__name__))

    def get_project_path(self):
        """ 获取项目根路径 """
        root_path = self.curr_path.split('git-test')[0]
        project_path = os.path.join(root_path, 'git-test\\')
        return project_path


if __name__ == '__main__':
    path = PathTools()
    print(path.get_project_path())
