# ！ /usr/bin/python3
# coding-utf-8
# @Time: 2022/12/2 19:41
# @Author: LYH


import pytest

from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report
from common.process_redis import Process


def pytest_collection_finish(session):
    # 所有用例个数
    total = len(session.items)
    # 充值用隔离进度和失败用例名称
    Process().reset_all()
    # 初始化进度
    Process().init_process(total)


@pytest.fixture()
def driver():
    global get_driver
    get_driver = DriverConfig().driver_config()
    yield get_driver  # fixture先实例化浏览器驱动然后通过yield返回到测试用例中（入参）做完操作之后返回到driver中，然后执行下一步，关闭浏览器
    get_driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    report.description = str(item.function.__doc__)

    if report.when == "call":
        if report.failed:
            # 失败了就截图
            add_img_2_report(get_driver, "失败截图", need_sleep=False)
            # 更新失败用例个数
            Process().update_fail()
            # 增加失败用例名称
            Process().insert_into_fail_testcase_name(report.description)
        elif report.passed:
            # 更新成功用例个数
            Process().update_success()
        else:
            pass
        process = Process().get_process()
        process(process)
