from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.deiver = webdriver.Chrome()
        self.deiver.implicitly_wait(3)
        self.deiver.get("https://work.weixin.qq.com/")

    def test_register(self):
        # self.driver.find_element(By.LINK_TEXT, '立即注册').click()
        index = Index(self.deiver)
        # self.driver.find_element(By.ID, 'corp_name').send_keys("测试自动化")
        # self.driver.find_element(By.ID, 'iagree').click()
        # self.driver.find_element(By.ID, 'submit_btn').click()
        index.goto_register().register("霍格沃兹测试学院")
