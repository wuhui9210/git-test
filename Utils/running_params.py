#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : running_params.py
# @Time  : 2020-12-11 15:09
# @Author: WU
# ==============================
import argparse

"""
    parse.add_argument(....) 参数说明
    * -d            短参数命令
    * --devices     长参数命令，两种命令可同时存在
    * type          需要传入的参数类型
    * required      True为必填惨，False为非必选惨
    * help          参数说明
    * default       指定参数默认值
    * choice        指定的选项集，list形式
"""


class RunningParams:
    """ 运行参数类 """

    def __init__(self):
        # 创建解析对象
        parse = argparse.ArgumentParser()
        # 运行时指定设备
        parse.add_argument('-d', '--devices', type=str, required=True, help='连接的设备')
        # 运行时指定用例，非必填
        parse.add_argument('-c', '--case', type=str, required=False, help='指定的用例', default='all')
        #
        # 解析参数
        self.args = parse.parse_args()

    def get_devices(self):
        """ 获取连接的设备 """
        return self.args.devices

    def get_case(self):
        """ 获取要执行的用例 """
        return self.args.case


if __name__ == '__main__':
    running = RunningParams()
    d = running.get_devices()
    print(d)
    c = running.get_case()
    print(c)
