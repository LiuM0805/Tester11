from test_appium.page.app import App
from test_appium.page.base_page import BasePage


class TestDD:
    def test_dd(self):
        base = BasePage()
        base.steps("../page/steps.yaml")

    def test_search(self):
        # 使用测试步骤的数据驱动执行case
        App().start().main().goto_search_page().search("jd")
