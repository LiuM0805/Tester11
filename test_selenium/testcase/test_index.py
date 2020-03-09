from test_selenium.page.index import Index


# 测试主页
class TestIndex():
    def setup(self):
        self.index = Index(reuse=True)

    def test_register(self):
        self.index.goto_register().register("霍格沃兹测试学院")

    def test_login(self):
        register_page = self.index.goto_login().goto_register().register("tester11")
        print(register_page.get_error_message())
        assert "请选择所属行业" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
