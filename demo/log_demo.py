#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : log_demo.py
# @Time  : 2020-12-17 9:58
# @Author: WU
# ==============================
import logging
import os
import time

from Utils.path_tools import PathTools


def log_to_file():
    """ 将日志写到文件 """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter('[%(levelname)7s] - %(asctime)s - %(name)s:[%(lineno)d] : %(message)s')

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

    logger.addHandler(handler)
    logger.addHandler(console)

    return logger


def basic_log():
    """ 基本写法 """
    logging.basicConfig(level=logging.DEBUG,
                        format='[\t%(asctime)s] - %(name)s - %(levelname)s : [%(lineno)d] :  %(message)s')
    logger = logging.getLogger(__name__)

    logger.info('this is info')
    logger.warning('this is warning')
    logger.error('this is error')
    logger.debug('this is debug')


if __name__ == '__main__':
    log = log_to_file()
    log.info('this is info')
    log.warning('this is warning')
    log.error('this is error')
    log.debug('this is debug')
