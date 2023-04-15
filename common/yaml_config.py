# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/11/24 22:16
# @Author: LYH

# file = open(r"D:\code\trading_system_autotest\config\environment.yaml", encoding="utf-8")
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()
# with open(r"D:\code\trading_system_autotest\config\environment.yaml", "r",
#           encoding="utf-8") as file:
#     # a = file.read()
#     for i in file.readlines():
#         print("======")
#         print(i)
import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_username_password(self, user):
        # return self.env["username"],self.env["password"]
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]

    def get_mysql_config(self):
        return self.env["mysql"]

    def get_redis(self):
        return self.env["redis"]


if __name__ == '__main__':
    print(GetConf().get_mysql_config())
