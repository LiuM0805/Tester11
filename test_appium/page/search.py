from appium.webdriver.common.mobileby import MobileBy
from test_appium.page.base_page import BasePage


class Search(BasePage):
    def search(self, key: str):
        self._driver.find_element(MobileBy.ID, "search_input_text").send_keys(key)
        self._driver.find_element(MobileBy.ID, "name").click()
        return self

    def get_price(self, key: str) -> float:
        price = float(self._driver.find_element(MobileBy.ID, "current_price").text)
        return price
