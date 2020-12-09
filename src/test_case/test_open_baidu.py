# -*- coding:utf-8 -*-
"""
# @Time   : 2020/9/8 14:56
# @Author : WU
# @file   : test_open_baidu
"""
import time
import pytest


class TestBaidu:

    def test_search(self, driver_init):
        driver = driver_init
        driver.get("http://www.baidu.com")

        driver.find_element_by_id('kw').send_keys('python')
        driver.find_element_by_id('su').click()
        time.sleep(1)
        assert 'python' in driver.title

        time.sleep(2)


if __name__ == '__main__':
    pytest.main(['-s', 'test_open_baidu.py'])
