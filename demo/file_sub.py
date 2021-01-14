#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : file_sub.py
# @Time  : 2021-1-12 16:14
# @Author: WU
# ==============================
import os

filename = r'C:\Users\dell\Desktop\file.txt'
with open(filename, 'r', encoding='utf-8') as f:
    for i in f:
        print(i.strip())
