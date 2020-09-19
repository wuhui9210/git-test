# -*- coding:utf-8 -*-
"""
# @Time   : 2020/9/8 16:45
# @Author : WU
# @file   : pytest
"""
import pytest
from selenium import webdriver


def driver():
    driver = webdriver.Chrome()