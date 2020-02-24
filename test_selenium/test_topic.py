from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Testerhome:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_testerhome(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(2)
        # element = (By.CSS_SELECTOR, "[data-name='霍格沃兹测试学院']")
        element=(By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name=霍格沃兹测试学院]').click()
        # self.driver.find_element(By.CSS_SELECTOR, '.topic-22235 .title > a').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def teardown(self):
        sleep(1)
        self.driver.quit()
