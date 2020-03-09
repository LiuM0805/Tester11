from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact
from test_selenium.page.message import Message


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_messagelist(self):
        all_locator = (By.LINK_TEXT, '显示全部')
        full_locator = (By.LINK_TEXT, '收起')
        content_locator = (By.CSS_SELECTOR, '.index_message_list li:nth-child(1)')
        self.find(all_locator).click()
        self.find(full_locator).click()
        self.find(content_locator).click()
        # return ManageTools(reuse=True)

    def goto_add_member(self):
        locator = (By.LINK_TEXT, '添加成员')
        self.find(locator).click()
        # 无法定位隐藏元素，使用下面执行脚本方法
        # self._driver.execute_script("arguments[0].click();", self.find(locator))
        return Contact(reuse=True)

    def goto_import_user(self):
        import_locator = (By.CSS_SELECTOR, '[node-type="import"]')
        self.find(import_locator).click()
        return Contact(reuse=True)

    def goto_message(self):
        locator = (By.CSS_SELECTOR, '[node-type="message"]')
        self.find(locator).click()
        return Message(reuse=True)
