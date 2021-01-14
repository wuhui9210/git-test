#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : caps.py
# @Time  : 2020-12-16 17:41
# @Author: WU
# ==============================
import os
import yaml
from appium import webdriver
from Utils.running_params import RunningParams
from Utils.path_tools import PathTools


def get_driver():
    root_path = PathTools().get_project_path()
    caps_path = os.path.join(root_path, 'config\\', 'caps.yml')
    with open(caps_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    device = RunningParams().get_devices()

    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': data['platformVersion'],
        'deviceName': f'{device}:5555',
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset'],
        'noSign': data['noSign'],
        'autoLaunch': data['autoLaunch'],
        'automationName': data['automationName']
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
