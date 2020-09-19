# -*- coding:utf-8 -*-
"""
---------------------------------
# @Time   : 2020/9/9 0:17
# @Author : WU
# @file   : article_demo
---------------------------------
"""
import time
from selenium import webdriver
import os


def save_file(file_name, content):
    base_path = "C:\\Users\\WU\\Desktop\\"
    dir_name = "blog"
    file_path = os.path.join(base_path, dir_name)
    flag = os.path.exists(file_path)
    if not flag:
        os.mkdir(file_path)
    else:
        print("文件已存在。。。")

    with open(file_path + "\\" + file_name + '.txt', 'w') as fp:
        fp.write(content)


def get_blog():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.get("http://wwhl.wang")  # 打开博客
    eles = driver.find_elements_by_xpath('//div[@class="item mb-5"]/div/div/h3/a')  # 获取首页所有博客链接

    for i in range(len(eles)):  # 遍历文章链接
        eles = driver.find_elements_by_xpath('//div[@class="item mb-5"]/div/div/h3/a')
        eles[i].click()  # 点击文章进入详情
        time.sleep(2)
        # 获取文章标题
        title_ele = driver.find_element_by_xpath('//header/h2')
        file_name = title_ele.text
        # 获取文章内容
        content_ele = driver.find_element_by_id('show-content')
        content = content_ele.text
        # 保存标题和内容
        save_file(file_name, content)

        # 返回首页
        back_ele = driver.find_element_by_id("backbtn")
        back_ele.click()
        driver.refresh()
        time.sleep(2)


if __name__ == '__main__':
    get_blog()
    # new_file('1', 'hello')
