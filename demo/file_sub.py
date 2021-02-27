#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : file_sub.py
# @Time  : 2021-1-12 16:14
# @Author: WU
# ==============================


def write_file():
    with open('1.txt', 'w', encoding='utf-8') as f:
        for i in range(100):
            f.write(f'{i}' + '\n')


def read_file():
    files = open('1.txt', 'r', encoding='utf-8')
    for i in files:
        print(i.strip())
    files.close()


if __name__ == '__main__':
    # write_file()
    read_file()
