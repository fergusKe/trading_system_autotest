# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/11/29 21:29
# @Author: LYH


from time import sleep

# from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.AccountPage import AccountPage


class TestPersonalInfo:
    def test_uplode_personal_avatar(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, "william")
        LeftMenuPage().click_level_one_menu(driver, "账户设置")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "个人资料")
        sleep(2)
        AccountPage().upload_avatar(driver, "个人头像二.jpg")
        sleep(3)
        AccountPage().click_save(driver)
        sleep(3)
        # driver.quit()
