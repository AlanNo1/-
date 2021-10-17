# 定义测试类
import time
from config import BaseDir
import pytest

from page.mis.home_page import HomeProxy
from utils import UtilsDriver, is_exist, get_case_data

case_data_addnews = get_case_data(BaseDir + "/data/mp/test_addnews_data.json", ifSingle=True, key='title')


@pytest.mark.run(order=1002)
class TestAuditArticle:
    # 定义类级别的fixture初始化操作
    def setup_class(self):
        self.home_proxy = HomeProxy()

    # 定义类级别的fixture销毁操作
    def teardown_class(self):
        UtilsDriver.quit_mis_driver()

    # 定义检查发布的新闻的测试用例
    @pytest.mark.parametrize("title", case_data_addnews)
    def test_audit_article(self, title):
        time.sleep(1)
        result = self.home_proxy.audit_article_pass()
        assert is_exist(UtilsDriver.get_mis_driver(), result)
        print("当前用例能找到新闻标题：", title)
