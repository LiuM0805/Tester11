
from selenium import webdriver

from test_selenium.test_hogwarts import Test_Testerhome


class Test_Browser(Test_Testerhome):
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)


    def test_case(self):
        Test_Testerhome.test_testerhome(self)