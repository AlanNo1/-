# 定义Django网站首页面对象
# 定义对象库层
from utils import UtilsDriver, choice_type
import time

from selenium.webdriver.common.by import By

from base.mis.base import BasePage, BaseHandle


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 新闻动态
        self.content_audit = By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[3]/ul/li[1]/a[2]"

    # 定位新闻动态
    def find_content_audit(self):
        return self.get_element(self.content_audit)


# 定义操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()
        self.driver = UtilsDriver.get_mis_driver()
        # 执行下拉操作
        self.driver.execute_script(f"document.documentElement.scrollTop={100 * 10}")

    # 获取新闻动态内容
    def click_content_audit(self):
        return self.home_page.find_content_audit().text


# 定义业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 返回新闻动态内容
    def audit_article_pass(self):
        return self.home_handle.click_content_audit()
