# 定义测试类
import logging
import allure
import pytest
from config import BaseDir
from page.mp.home_page import HomeProxy
from page.mp.login_page import LoginProxy
from page.mp.publish_page import PublishProxy
from utils import UtilsDriver, is_exist, get_case_data

case_data = get_case_data(BaseDir + "/data/mp/test_login_data.json")
case_data_addnews = get_case_data(BaseDir + "/data/mp/test_addnews_data.json")


@pytest.mark.run(order=1)
class TestPublishArticle:
    # 定义类级别的fixture初始化操作方法
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.publish_proxy = PublishProxy()

    # 定义类级别的fixture销毁操作方法
    def teardown_class(self):
        UtilsDriver.quit_mp_driver()

    # 定义登录的测试用例
    @allure.step(title="登录的测试用例")
    @pytest.mark.parametrize("username, code, expect", case_data)
    @allure.severity(allure.severity_level.CRITICAL)  # 添加严重级别
    def test_login(self, username, code, expect):
        logging.info("用例的数据如下：用户名：{}， 密码：{}， 预期结果：{}".format(username,
                                                             code, expect))
        print(username, code)
        self.login_proxy.login(username, code)  # 登录
        allure.attach(UtilsDriver.get_mp_driver().get_screenshot_as_png(), "登录截图", allure.attachment_type.PNG)
        username = self.home_proxy.get_username_msg()  # 获取登录后的用户名信息
        assert expect == username.upper()  # 根据获取到的用户名进行断言

    # 定义发布文章的测试用例
    @allure.step(title="发布文章的测试用例")
    @pytest.mark.parametrize("title, content, type , expect", case_data_addnews)
    @allure.severity(allure.severity_level.CRITICAL)  # 添加严重级别
    def test_publish_article(self, title, content, type, expect):
        logging.info("用例的数据如下：新闻标题：{}， 新闻内容：{}，新闻类型：{}， 预期结果：{}".format(title, content, type, expect))
        self.home_proxy.go_publish_page()  # 跳转到发布文章页面
        self.publish_proxy.publish_article(title, content, type)
        assert is_exist(UtilsDriver.get_mp_driver(), expect)
# pytest执行完毕可以用allure generate report/ -o report/html --clean产生allure报告