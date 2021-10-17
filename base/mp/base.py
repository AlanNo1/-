# 定义djang后台管理系统的基类
from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver


# 对象库层基类封装
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_mp_driver()  # 获取djang后台管理系统浏览器驱动

    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element


# 操作层基类封装
class BaseHandle:
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
