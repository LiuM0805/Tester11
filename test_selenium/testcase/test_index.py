from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.index=Index()

    def test_register(self):
        self.index.goto_register().register("霍格沃兹测试学院")

