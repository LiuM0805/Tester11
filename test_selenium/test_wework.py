from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeWork:
    def setup(self):
        chromeoptions=Options()
        chromeoptions.add_experimental_option("debuggerAddress","127.0.0.1:9222")
        self.driver = webdriver.Chrome(options=chromeoptions)
        self.driver.implicitly_wait(5)

    def test_wework(self):
        self.driver.find_element(By.ID, 'menu_contacts').click()
        WebDriverWait(self.driver, 10).until(self.clickelement)
        self.driver.find_element(By.ID, 'username').send_keys("abc")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("123")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("13717947136")
        self.driver.find_element(By.CSS_SELECTOR, '.js_member_editor_form div:nth-child(1) .js_btn_save').click()

    def clickelement(self, x):
        size = len(self.driver.find_elements(By.ID, 'username'))
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member .js_add_member').click()
        return size >= 1

    def teardown(self):
        sleep(2)
        self.driver.quit()