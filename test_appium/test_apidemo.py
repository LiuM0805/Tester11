# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        # caps["noReset"] = True  # 是否清理数据
        # caps["dontStopAppOnReset"] = True  # 不杀app进程
        # caps["unicodeKeyBoard"] = True  # 输入中文
        # caps["resetKeyBoard"] = True  # 恢复输入法
        caps["autoGrantPermissions"] = True  # 取消弹窗提示

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def test_toast(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Make a Popup!').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Search"]').click()
        # 使用toast的xpath定位，//*[@class="android.widget.Toast"]
        toast = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "Search" in toast
        assert "Clicked" in toast

    def teardown(self):
        pass
        # sleep(5)
        # self.driver.quit()
