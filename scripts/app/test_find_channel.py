# 定义测试类
import pytest
from config import BaseDir
from page.app.index_page import IndexProxy
from utils import UtilsDriver
from utils import UtilsDriver, is_exist, get_case_data

case_data_addnews = get_case_data(BaseDir + "/data/mp/test_addnews_data.json", ifSingle=True, key='title')


@pytest.mark.run(order=2000)
class TestFindChannel:
    # 定义类级别的fixture初始化方法
    def setup_class(self):
        self.indxe_proxy = IndexProxy()

    # 定义类级别的fixture销毁方法
    def teardown_class(self):
        UtilsDriver.quit_app_driver()

    # @pytest.mark.parametrize("title", case_data_addnews)
    # 测试用例
    def test_find_channel(self):
        find_news = self.indxe_proxy.find_channel()
        assert find_news
        print("手机设置页面测试成功")
