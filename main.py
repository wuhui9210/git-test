#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : main.py
# @Time  : 2020-12-14 14:56
# @Author: WU
# ==============================
from Utils.adb_tools import AdbTools
from Utils.running_params import RunningParams

if __name__ == '__main__':
    device = RunningParams().get_devices()
    a = AdbTools(device_id=device)
    r = a.get_devices()
    print(r)
    p = a.get_current_package()
    print(p)

