#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : base.py
# @Time  : 2020-12-11 11:49
# @Author: WU
# ==============================
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.adb_tools import AdbTools
from Utils.running_params import RunningParams
from src.base.caps import get_driver


class BasePage:
    """ 所有页面的基类 """

    def __init__(self, driver: WebDriver = get_driver()):
        self._driver = driver

        device = RunningParams().get_devices()
        self._adb = AdbTools(device_id=device)

    def find_element(self, element, timeout=10, poll=0.1):
        """
        查找单个元素
        :param element: 要查找的元素
        :param timeout: 超时时间
        :param poll:  间隔时间
        :return:
        """
        try:
            return WebDriverWait(self._driver, timeout, poll).until(lambda x: x.find_element(*element))
        except NoSuchElementException:
            print('查找元素异常')

    def find_elements(self, element, timeout=10, poll=0.1):
        """
        查找一组元素
        :param element: 要查找的元素
        :param timeout: 超时时间
        :param poll:  间隔时间
        :return:
        """
        try:
            return WebDriverWait(self._driver, timeout, poll).until(lambda x: x.find_element(*element))
        except NoSuchElementException:
            print('查找元素异常')
