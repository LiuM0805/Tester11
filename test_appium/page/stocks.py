from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage
from test_appium.page.search import Search


class Stocks(BasePage):
    def goto_search(self):
        self.find(By.ID, "action_search").click()
        return Search(self._driver)

    def stocks_select(self):
        self.find()

