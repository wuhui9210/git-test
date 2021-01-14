#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : path_demo.py
# @Time  : 2020-12-16 17:54
# @Author: WU
# ==============================
import os

from Utils.log_tools import Logs

logger = Logs().logger

if __name__ == '__main__':
    logger.info('hello info')
    logger.debug('hello debug')
    logger.error('hello error')
    logger.warning('hello waring')
