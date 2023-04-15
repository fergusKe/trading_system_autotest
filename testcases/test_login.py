# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/11/26 8:44
# @Author: LYH

from time import sleep
import allure
import pytest
from common.report_add_img import add_img_2_report

from page.LoginPage import LoginPage


class TestLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录")
    def test_login(self, driver):
        """
        使用错误的账号登录
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login(driver, "failure")
            sleep(3)
            add_img_2_report(driver, "登录")
