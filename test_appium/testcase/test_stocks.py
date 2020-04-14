from test_appium.page.app import App


class TestStocks:
    def setup(self):
        self.stocks = App().start().main()

    def test_stocks(self):
        assert "已添加" in self.stocks.goto_stocks().goto_search().search("jd").add_select().get_msg()
        self.stocks.page_back()
        assert "京东" in self.stocks.goto_stocks().stockname_select()

