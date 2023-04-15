# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/11/30 14:00
# @Author: LYH


# 断言

# class TestAssert:
#     def test_assert(self):
#         # “==”，“！=”，“<”,">",">=","<="
#         assert "william" == "william"
#         assert "william-a" != "william-b"
#         assert 0 < 1
#         assert 2 > 1
#         assert 3 <= 7 - 2
#         assert 4 >= 1 + 2
#         # 包含和不包含
#         assert "william" in "william UI自动化测试"
#         assert "william" not in "UI自动化测试"
#         # true和false
#         assert 1
#         assert (9 < 10) is True
#         assert not False


import pytest
from pytest_assume.plugin import assume


class TestAssert:

    def test_assert(self):
        with assume: assert "william" in "UI autotest"
        pytest.assume(1 + 1 == 3)
        assert 1 + 1 == 2
        print("over")
