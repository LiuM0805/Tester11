# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True  # 是否清理数据
        caps["dontStopAppOnReset"] = True  # 不杀app进程
        caps["unicodeKeyBoard"] = True  # 输入中文
        caps["resetKeyBoard"] = True  # 恢复输入法
        caps["autoGrantPermissions"] = True  # 取消弹窗提示

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def test_search(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el1.click()
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # el2.click()
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # # el3.send_keys("alibaba")
        # el3.send_keys("阿里巴巴")  # 配合是否输入中文使用
        # 输入阿里巴巴
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")

    def test_search_and_get_price(self):
        # self.driver.find_element(MobileBy.ID, "tv_agree").click()
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        # 输入阿里巴巴
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        # name默认点击搜索出来的第一只股票
        self.driver.find_element(MobileBy.ID, "name").click()
        # 断言股票价格是否大于160
        assert float(self.driver.find_element(MobileBy.ID, "current_price").text) > 160

    def test_scroll(self):
        # 获取窗口大小
        size = self.driver.get_window_size()
        # 循环10遍，long_press长按，move_to移动，release释放长按，perform执行以上步骤
        for i in range(10):
            TouchAction(self.driver) \
                .long_press(x=size["width"] * 0.5, y=size["height"] * 0.8) \
                .move_to(x=size["width"] * 0.5, y=size["height"] * 0.2) \
                .release().perform()

    def test_device(self):
        # 切后台5秒
        self.driver.background_app(5)

    # 作业2，搜索阿里巴巴后，点击股票分类，获取香港上市股票，并断言估价大于200
    def test_alibaba_hk(self):
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        stock = (MobileBy.XPATH, "//*[contains(@resource-id,'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        price = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]")
        assert float(self.driver.find_element(*price).text) > 160

    # 作业3，添加某只股票到自选，然后再次搜索并验证，股票是否加自选（不用使用文本判断，使用get_attribute）
    def test_attribute(self):
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='BABA']").click()
        stock = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        follow = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'follow_btn')]")
        self.driver.find_element(*follow).click()
        self.driver.find_element(MobileBy.ID, 'action_close').click()
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='BABA']").click()
        stock = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]//*[@text='股票']")
        self.driver.find_element(*stock).click()
        follow_status = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'followed_btn')]")
        attribute = self.driver.find_element(*follow_status).get_attribute("text")
        assert attribute == "已添加"

    def test_uislector(self):
        # 使用uiselector魔法滑屏效果
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("5小时前").instance(0));')
        # 直到滑屏内容包含：5小时前，进行点击操作
        self.driver.find_element(*scroll_to_element).click()

    def test_source(self):
        # 获取页面资源xml，可以验证xpath定位是否准确
        print(self.driver.page_source)

    def teardown(self):
        pass
        # sleep(5)
        # self.driver.quit()
