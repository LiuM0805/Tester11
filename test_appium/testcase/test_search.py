import pytest
import yaml

from test_appium.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start().main()

    def test_search(self):
        assert self.main.goto_search_page().search("alibaba").get_price("BABA") > 187

    def test_add_select(self):
        assert "已添加" in self.main.goto_search_page().search("JD").add_select().get_msg()

    # @pytest.mark.parametrize("key, stock_type, price", [
    #     ("alibaba", "BABA", 170),
    #     ("JD", "JD", 30)
    # ])

    @pytest.mark.parametrize("key, stock_type, price", yaml.safe_load(open("data.yaml")))
    def test_search_data(self, key, stock_type, price):
        assert self.main.goto_search_page().search(key).get_price(stock_type) > price
