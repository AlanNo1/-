# django网站的发布新闻页面对象
from selenium.webdriver.common.by import By

from base.mp.base import BasePage, BaseHandle

# 定义对象库层
from utils import UtilsDriver, choice_type


class PublishPage(BasePage):
    def __init__(self):
        super().__init__()
        # 新闻标题输入框
        self.title = By.XPATH, "//input[@id='id_title']"
        # iframe元素对象
        self.iframe_ele = By.ID, "ueditor_0"
        # 新闻内容输入框
        self.content = By.XPATH, "/html/body[@class='view']"
        # 新闻类型
        self.news_type = By.XPATH, "//*[@id='id_newType']/option[1]"
        # 发布时间
        # 浏览量
        # 保存按钮
        self.publish_btn = By.XPATH, "//*[@id='mynew_form']/div/div/input[@value='保存']"

    # 找新闻的标题
    def find_title(self):
        return self.get_element(self.title)

    # 找切换的iframe
    def find_iframe(self):
        return self.get_element(self.iframe_ele)

    # 找新闻内容输入框
    def find_input_kw(self):
        return self.get_element(self.content)

    # 定位新闻类型
    def find_news_type(self):
        return self.get_element(self.news_type)

    # 定位保存按钮
    def find_publish_btn(self):
        return self.get_element(self.publish_btn)


# 定义操作层
class PublishHandle(BaseHandle):
    def __init__(self):
        self.publish_page = PublishPage()
        self.driver = UtilsDriver.get_mp_driver()

    # 输入新闻标题
    def input_title(self, title):
        self.input_text(self.publish_page.find_title(), title)

    # 输入新闻内容
    def input_content(self, content):
        # 切换到iframe当中
        self.driver.switch_to.frame(self.publish_page.find_iframe())
        # 输入文章内容
        self.input_text(self.publish_page.find_input_kw(), content)
        # 切回到默认首页（退出Iframe)
        self.driver.switch_to.default_content()

    # 选择新闻类型
    def choice_newstype(self, type):
        choice_type(self.driver, self.publish_page.find_news_type(), type)

    # 点击发布按钮
    def click_publish_btn(self):
        self.publish_page.find_publish_btn().click()


# 定义业务层
class PublishProxy:
    def __init__(self):
        self.publish_handle = PublishHandle()

    # 发布新闻
    def publish_article(self, title, content, type):
        # 输入文章标题
        self.publish_handle.input_title(title)
        self.publish_handle.input_content(content)
        self.publish_handle.choice_newstype(type)
        self.publish_handle.click_publish_btn()
