from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    # 添加成员按钮，使用高频，所以单独拿出来
    _add_member_button = (By.CSS_SELECTOR, '.js_has_member .js_add_member')

    def add_member(self):
        name_locator=(By.NAME, 'username')
        acctid_locator=(By.NAME, 'acctid')
        gender_locator=(By.CSS_SELECTOR, '.ww_label [value="2"]')
        mobile_locator=(By.NAME, 'mobile')
        save_locator=(By.CSS_SELECTOR, '.js_btn_save')
        self.find(name_locator).send_keys("测试")
        self.find(acctid_locator).send_keys("123")
        self.find(gender_locator).click()
        self.find(mobile_locator).send_keys("12345678901")
        self.find(save_locator).click()

    def search(self, name):
        pass

    def import_users(self, path):
        input_locator=(By.ID, 'js_upload_file_input')
        submin_locator=(By.ID, 'submit_csv')
        reload_locator=(By.ID, 'reloadContact')
        self.find(input_locator).send_keys(path)
        self.find(submin_locator).click()
        self.find(reload_locator).click()

    def export_users(self):
        pass

    def set_department(self, data):
        pass

    def delete(self):
        pass

    def invite(self):
        pass

    def add_department(self):
        pass
