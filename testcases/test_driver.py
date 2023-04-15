# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/11/25 23:10
# @Author: LYH
from time import sleep
from selenium import webdriver
from common.tools import get_project_path, sep

# 设置Chrome窗口大小,设置为1920*1080
options = webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080")
# 去除“Chrome正受到自动检测软件的控制”的提示
options.add_experimental_option("excludeSwitches", ["enable-automation"])
# 解决selenium无法访问https的问题
options.add_argument("--ignore-certificate-errors")
# 允许忽略localhost上的TLS/SSL错误
options.add_argument("--allow-insecure-localhost")
# 设置为无痕模式
options.add_argument("--incognito")
# 设置为无头模式
# options.add_argument("--headless")
# 解决卡顿  三个参数
options.add_argument("--disable-gpu")  # 禁用gpu硬件加速
options.add_argument("--no-sandbox")  # 禁用sandbox
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("http://www.tcpjwtester.top")
sleep(3)
driver.quit()
