from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.base_page import BasePage


class Manage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def material(self, path):
        self.find((By.CSS_SELECTOR, '[href="#material/text"]')).click()
        self.find((By.CSS_SELECTOR, '[href="#material/image"]')).click()
        self.find((By.CSS_SELECTOR, '.ww_commonCntHead_title a')).click()
        self.find((By.ID, 'js_upload_input')).send_keys(path)
        # 等待10秒上传图片成功后的删除icon
        self.wait(10, self._delete_element)
        self.find((By.LINK_TEXT, '完成')).click()
        return self

    def _delete_element(self, x):
        # 上传图片成功后，会返回图片的删除icon
        element = self.find(By.CSS_SELECTOR, '.js_delete_file span')
        return element

    def upload_status(self):
        # 返回一个数组，内容是图片名称，用于case断言使用
        result = []
        # 循环把获取到的图片列表内图片名称添加到数组内
        for pic_name in self.elements(By.CSS_SELECTOR, '.js_pic_name_show'):
            result.append(pic_name.text)
        return result
