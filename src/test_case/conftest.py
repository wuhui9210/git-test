# -*- coding:utf-8 -*-
"""
---------------------------------
# @Time   : 2020/9/19 23:47
# @Author : WU
# @file   : conftest.py
---------------------------------
"""
import pytest
from selenium import webdriver


@pytest.fixture()
def driver_init():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
