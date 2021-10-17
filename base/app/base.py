# 定义app的基类
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver import Remote
from utils import UtilsDriver
import time


# 对象库层基类封装
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_app_driver()  # 获取app驱动

    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element


# 操作层基类封装
class BaseHandle:
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
        time.sleep(2)
        # 回车键
        # self.driver.keyevent(66)
