# 定义工具类
import json
import time

from selenium import webdriver
from appium import webdriver as app_driver
from selenium.webdriver.common.by import By


class UtilsDriver:
    _mp_driver = None  # 表示的是djang网站的浏览器驱动
    _mis_driver = None  # 表示的是django管理页面的浏览器驱动
    _app_driver = None  # 表示的是app的驱动

    __quit_mis_driver = True  # 后台管理系统退出驱动的标识

    # 定义修改私有属性的方法
    @classmethod
    def set_quit_driver(cls, mark):
        cls.__quit_mis_driver = mark

    # 定义获取djang后台管理系统的浏览器驱动
    @classmethod
    def get_mp_driver(cls):
        if cls._mp_driver is None:
            cls._mp_driver = webdriver.Chrome()
            cls._mp_driver.maximize_window()
            cls._mp_driver.get("http://152.32.128.199/admin/")
        return cls._mp_driver

    # 定义退出djang后台管理系统的浏览器驱动
    @classmethod
    def quit_mp_driver(cls):
        if cls._mp_driver is not None:
            cls.get_mp_driver().quit()
            cls._mp_driver = None

    # 定义获取Django网站的浏览器驱动
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver = webdriver.Chrome()
            cls._mis_driver.maximize_window()
            cls._mis_driver.get("http://152.32.128.199")
        return cls._mis_driver

    # 定义退出Django网站操作方法
    @classmethod
    def quit_mis_driver(cls):
        if cls._mis_driver and cls.__quit_mis_driver:
            cls.get_mis_driver().quit()
            cls._mis_driver = None

    # 定义获取app的驱动
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            des_cap = {
                "platformName": "android",  # 表示的是android  或者ios
                "platformVersion": "5.1.1",  # 表示的是平台系统的版本号
                "deviceName": "****",  # 表示的是设备的ID名称（如果只有一个设备可以用****来代替）
                # adb shell dumpsys window | findstr "usedApp"获取应用启动名和包名
                "appPackage": "com.android.settings",  # 表示app的包名
                "appActivity": ".Settings",  # 表示的是app的界面名
                "noReset": True,  # 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
                "resetKeyboard": True,  # 重置设备的输入键盘
                "unicodeKeyboard": True  # 采用unicode编码输入
            }
            cls._app_driver = app_driver.Remote("http://127.0.0.1:4723/wd/hub", des_cap)
        return cls._app_driver

    # 定义退出app驱动的方法
    @classmethod
    def quit_app_driver(cls):
        if cls._app_driver is not None:
            cls.get_app_driver().quit()
            cls._app_driver = None


# 封装一个选择新闻类型的方法
def choice_type(driver, element, type):
    """
    :param driver:  浏览器驱动对象
    :param element:  元素对象
    :param channel:  要选择的文本内容
    :return:
    """
    element.click()
    time.sleep(1)
    xpath = "//*[@id='id_newType']/option[@value='{}']".format(type)
    driver.find_element(By.XPATH, xpath).click()


# 封装一个方法判断元素是否存在
def is_exist(driver, text):
    """
    :param driver:  浏览器驱动对象
    :param text:   定位元素的文本内容
    :return:
    """
    xpath = "//*[contains(text(), '{}')]".format(text)
    # //*[contains(text(),'成功添加了 新闻')]
    try:
        time.sleep(2)
        return driver.find_element(By.XPATH, xpath)
    except Exception as e:
        return False


# 定义app中边滑动边查找的方法
def app_swipe_find(driver, element, target_ele):
    """
    :param driver: 表示的是app的驱动
    :param element: 表示的滑动的元素对象
    :param target_ele: 表示的是要查找的元素的定位的值
    :return:
    """
    i = 0
    location = element.location  # 获取元素的坐标点位置
    x = location["x"]  # 获取坐标点X的值
    y = location["y"]  # 获取坐标点y的值
    size = element.size
    width = size["width"]
    height = size["height"]
    start_x = x + 0.9 * width
    end_x = start_x
    start_y = 500
    end_y = 10
    page_source = driver.page_source
    try:
        driver.swipe(start_x, start_y, end_x, end_y, duration=1500)
        time.sleep(5)
        driver.find_element(*target_ele).click()
        return True
    except Exception as e:
        return False


# 封装获取测试数据的方法
def get_case_data(filename, ifSingle=False, key="请输入json的键"):
    with open(filename, encoding='utf-8') as f:
        case = json.load(f)
    list_case_data = []
    for case_data in case.values():
        if ifSingle:
            list_case_data.append(case_data[key])
        else:
            list_case_data.append(tuple(case_data.values()))
    return list_case_data
