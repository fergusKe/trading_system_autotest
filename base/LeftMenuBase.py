# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/11/26 16:05
# @Author: LYH

class LeftMenuBase:

    def level_one_menu(self,menu_name):
        """
        一级菜单栏
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_menu(self,menu_name):
        """
        二级菜单栏
        :param menu_name:
        :return:
        """
        return "//aside[@class ='el-aside']//span[text()='" + menu_name + "']/parent::li"
if __name__ == '__main__':
    #print(LeftMenuBase().level_one_menu("产品"))
    print(LeftMenuBase().level_two_menu("我的商品列表"))



