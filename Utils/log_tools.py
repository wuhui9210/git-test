#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : log_tools.py
# @Time  : 2020-12-17 9:03
# @Author: WU
# ==============================
import logging
import os
import time
from Utils.path_tools import PathTools


class Logs:

    def __init__(self):
        # 创建logger对象，设置级别
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(levelname)7s] - %(asctime)s - %(filename)s:[%(lineno)d] : %(message)s')

        # 创建日志文件
        date_format = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        log_path = os.path.join(PathTools().get_project_path(), 'output\\', 'logs\\')
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        # 将日志输出到文件
        filename = os.path.join(log_path, date_format) + '.log'
        handler = logging.FileHandler(filename=filename)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(fmt)
        # 将日志打印在控制台
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(fmt)

        self.logger.addHandler(handler)
        self.logger.addHandler(console)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        self.logger.error(msg)

    def warning(self, msg):
        self.logger.warning(msg)
