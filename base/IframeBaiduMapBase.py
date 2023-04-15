# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/11/29 21:47
# @Author: LYH


class IframeBaiduMapBase:

    def search_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"
