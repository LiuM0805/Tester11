import datetime
import os

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            udid = os.getenv("udid", None)
            if udid is not None:
                caps["udid"] = os.getenv("udid", "")
            # caps["noReset"] = True  # 是否清理数据
            # caps["dontStopAppOnReset"] = True  # 不杀app进程
            # 测试webview时启动下面的代码
            # caps["chromedriverExecutable"] = "/Users/liumiao/chromedriver/appium/2.20/chromedriver"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # Grid模式
            # self._driver = webdriver.Remote("http://localhost:4444/wd/hub", caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(self._package, self._activity)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            return False

        WebDriverWait(self._driver, 20).until(wait_load)
        # lambda表达式写法
        # WebDriverWait(self._driver, 20).until(lambda x: "同意" in self._driver.page_source)
        return Main(self._driver)
