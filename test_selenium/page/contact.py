from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    # 添加成员按钮，使用高频，所以单独拿出来
    _add_member_button = (By.CSS_SELECTOR, '.js_has_member .js_add_member')
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def main_add_member(self, name, acctid, moblie):
        add_locator = (By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member')
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        gender_locator = (By.CSS_SELECTOR, '.ww_label [value="2"]')
        mobile_locator = (By.NAME, 'mobile')
        save_locator = (By.CSS_SELECTOR, '.js_btn_save')
        self.find(add_locator).click()
        self.find(name_locator).send_keys(name)
        self.find(acctid_locator).send_keys(acctid)
        self.find(gender_locator).click()
        self.find(mobile_locator).send_keys(moblie)
        self.find(save_locator).click()
        return self

    # 添加成员流程
    def add_member(self, name, acctid, moblie):
        add_locator = (By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member')
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        gender_locator = (By.CSS_SELECTOR, '.ww_label [value="2"]')
        mobile_locator = (By.NAME, 'mobile')
        save_locator = (By.CSS_SELECTOR, '.js_btn_save')
        self.find(add_locator).click()
        self.find(name_locator).send_keys(name)
        self.find(acctid_locator).send_keys(acctid)
        self.find(gender_locator).click()
        self.find(mobile_locator).send_keys(moblie)
        self.find(save_locator).click()
        return self

    def import_users(self, path):
        input_locator = (By.ID, 'js_upload_file_input')
        submin_locator = (By.ID, 'submit_csv')
        reload_locator = (By.ID, 'reloadContact')
        self.find(input_locator).send_keys(path)
        self.find(submin_locator).click()
        self.find(reload_locator).click()

    # 使用鼠标悬停操作，进入编辑页
    # todo:还没有实现悬停不同的数据后点击编辑
    def edit_member1(self):
        move_element_locator = self.find(By.CSS_SELECTOR, '.member_colRight_memberTable_td')
        # edit_button = (By.CSS_SELECTOR, '.ww_table_tr_Hover')
        edit_button = (By.CSS_SELECTOR, '.js_dropdown_menuBtn')
        click_edit = (By.CSS_SELECTOR, '.smart_menu_a')
        self.move_mouse(move_element_locator)
        self.find(edit_button).click()
        self.find(click_edit).click()

    # 使用普通流程编辑
    def edit_member2(self, name, mobile):
        data_locator = (By.CSS_SELECTOR, '#member_list tr:nth-child(2)')
        edit_locator = (By.CSS_SELECTOR, '.js_edit')
        name_locator = (By.NAME, 'username')
        mobile_locator = (By.NAME, 'mobile')
        save_locator = (By.CSS_SELECTOR, '.js_member_editor_form div:nth-child(1) .js_save')
        return_locator = (By.CSS_SELECTOR, '.js_back')
        self.find(data_locator).click()
        self.find(edit_locator).click()
        self.clear_input(name_locator)
        self.find(name_locator).send_keys(name)
        self.clear_input(mobile_locator)
        self.find(mobile_locator).send_keys(mobile)
        self.find(save_locator).click()
        self.find(return_locator).click()

    def delete_member(self):
        user_locator = (By.CSS_SELECTOR, '#member_list tr:nth-child(2) .ww_checkbox')
        delete_locator = (By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_delete')
        sleep(2)
        ok_locator = (By.CSS_SELECTOR, '.ww_dialog_foot .ww_btn_Blue')
        self.find(user_locator).click()
        self.find(delete_locator).click()
        self.find(ok_locator).click()

    # 返回添加、编辑成员成功的文本内容
    def assert_value(self):
        contactlist = (By.ID, 'js_tips')
        self.wait(10, expected_conditions.visibility_of_all_elements_located(contactlist))
        print(self.find(contactlist))
        return self.find(contactlist).text
