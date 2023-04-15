# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/12/2 20:53
# @Author: LYH

import random

import pytest


class TestRerun:

    def test_rerun(self):
        num = random.randint(1, 3)
        print("num", num)
        if num != 1:
            print("失败")
            raise Exception("出错了")
        else:
            print("成功")
