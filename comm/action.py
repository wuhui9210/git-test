#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : action.py
# @Time  : 2020-12-25 14:38
# @Author: WU
# ==============================
from appium.webdriver.webdriver import WebDriver


class Action(object):
    """ 常见的操作 """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_size(self):
        """ 获取屏幕大小 """
        x = self.driver.get_window_size('width')
        y = self.driver.get_window_size('height')
        return x, y

    def swipe_left(self, t=500):
        """ 向左滑动  t: 时间 """
        size = self.get_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.5)
        x2 = int(size[0] * 0.25)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t=500):
        """ 向右滑动  t: 时间 """
        size = self.get_size()
        x1 = int(size[0] * 0.25)
        y1 = int(size[1] * 0.5)
        x2 = int(size[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_up(self, t=500):
        """ 向上滑动  t: 时间 """
        size = self.get_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.75)
        y2 = int(size[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t=500):
        """ 向下滑动  t: 时间 """
        size = self.get_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.25)
        y2 = int(size[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)
