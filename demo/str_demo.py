# -*- coding:utf-8 -*-
"""
---------------------------------
# @Time   : 2020/9/9 10:50
# @Author : WU
# @file   : str_demo
---------------------------------
"""


def joinStr(varStr):
    # result = varStr.split(' ')
    # result1 = varStr.split(' ')[1:8]
    # n = 0
    # for i in result1:
    #     if int(i) // 10 == 0:
    #         i = '0' + i
    newStr = varStr.split(' ')
    for i in range(len(newStr)):
        if int(newStr[i]) // 10 == 0:
            x = '0' + newStr[i]
            newStr[i] = x
    result = ''.join(newStr)
    return result

    # return result


if __name__ == "__main__":
    result = joinStr("2020 8 11 23 5 59 8 6 999")
    # print(result)
