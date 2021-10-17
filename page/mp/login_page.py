# django网站的登录页面对象
import allure
from selenium.webdriver.common.by import By

from base.mp.base import BasePage, BaseHandle


# 定义对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.mobile = By.XPATH, "// *[@id='id_username']"

        # 密码输入框
        self.code = By.XPATH, "//*[@id='id_password']"
        # 登录按钮
        self.login_btn = By.XPATH, "//input[@value='登录']"

    # 定位用户名输入框
    def find_mobile(self):
        return self.get_element(self.mobile)

    # 定位密码输入框
    def find_code(self):
        return self.get_element(self.code)

    # 定位登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 定义操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入账号
    @allure.step(title="输入账号")
    def input_mobile(self, mobile):
        self.input_text(self.login_page.find_mobile(), mobile)

    # 输入密码
    @allure.step(title="输入密码")
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 点击登录按钮
    @allure.step(title="点击登录按钮")
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务
    def login(self, mobile, code):
        self.login_handle.input_mobile(mobile)  # 输入账号
        self.login_handle.input_code(code)  # 输入密码
        self.login_handle.click_login_btn()  # 点击登录按钮
