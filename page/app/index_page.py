# 首页页面对象
# 定义对象库层
from selenium.webdriver.common.by import By
import time
from base.app.base import BasePage, BaseHandle
from utils import app_swipe_find


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        # 滑动的框（搜索按钮）
        self.scroll_element = By.ID, "com.android.settings:id/search"
        # 点击的设置按钮
        self.channel = By.XPATH, "//android.widget.TextView[@text='电池']"

    # 查找滑动框
    def find_scroll_element(self):
        return self.get_element(self.scroll_element)


# 定义操作层
class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()

    # 边滑动边查找对应的按钮
    def click_channel(self):
        xpath = self.index_page.channel[0], self.index_page.channel[1]
        return app_swipe_find(self.index_page.driver, self.index_page.find_scroll_element(), xpath)


# 定义业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 滑动到对应的设置按钮
    def find_channel(self):
        return self.index_handle.click_channel()
