#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================
# @File  : my_adb_tools.py
# @Time  : 2020-12-11 16:12
# @Author: WU
# ==============================
import os
import platform


class AdbTools:
    """ adb工具类 """

    def __init__(self, device_id=''):
        self.__system = platform.system()
        self.__find = ''
        self.__command = ''
        self.__device_id = device_id
        self.__get_find()
        self.__check_adb()
        self.__connect_device()

    def __get_find(self):
        """ 判断系统类型，Windows用findstr， Linux用grep"""
        if self.__system is 'Windows':
            self.__find = 'findstr'
        else:
            self.__find = 'grep'

    def __check_adb(self):
        """ 检查adb有没有配置环境变量 ANDROID_HOME"""
        if 'ANDROID_HOME' in os.environ:
            if self.__system == 'Windows':
                path = os.path.join(os.environ['ANDROID_HOME'], 'platform-tools', 'adb.exe')
                if os.path.exists(path):
                    self.__command = path
                else:
                    raise EnvironmentError(f'adb not found in {os.environ["ANDROID_HOME"]}')
            else:
                path = os.path.join(os.environ['ANDROID_HOME'], 'platform-tools', 'adb')
                if os.path.exists(path):
                    self.__command = path
                else:
                    raise EnvironmentError(f'adb not found in {os.environ["ANDROID_HOME"]}')
        else:
            raise EnvironmentError(f'adb not found in {os.environ["ANDROID_HOME"]}')

    def __connect_device(self):
        """ 指定设备连接 """
        if self.__device_id == '':
            return
        self.__device_id = '-s %s' % self.__device_id

    def adb(self, args):
        """ adb命令 """
        cmd = '%s %s %s' % (self.__command, self.__device_id, str(args))
        return os.popen(cmd)

    def adb_shell(self, args):
        """ adb shell 命令 """
        cmd = '%s %s shell %s' % (self.__command, self.__device_id, str(args))
        return os.popen(cmd)

    def devices(self):
        """ 查看连接的设备 """
        result = self.adb('devices').readlines()
        print(result)
        devices_list = [i.strip() for i in result[1:] if i ]
        return devices_list

    def connect(self):
        """ 连接设备 """
        cmd = '%s connect %s' % (self.__command, self.__device_id)
        return os.popen(cmd)


if __name__ == '__main__':
    adb = AdbTools(device_id='192.168.3.4')
    print(adb.devices())
