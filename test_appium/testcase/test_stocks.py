from test_appium.page.app import App


class TestStocks:
    def setup(self):
        self.stocks = App().start().main()

    def test_stocks(self):
        self.stocks.goto_stocks().goto_search().search("jd").add_select().un_select()
