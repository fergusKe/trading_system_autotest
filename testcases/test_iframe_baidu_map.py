# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/11/29 21:53
# @Author: LYH

from time import sleep

from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.IframeBaiduMapPage import IframeBaiduMapPage


class TestIframeBaiduMap:

    def test_iframe_baidu_map(self, driver):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, "william")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(1)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        sleep(1)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        sleep(3)
        # driver.quit()
