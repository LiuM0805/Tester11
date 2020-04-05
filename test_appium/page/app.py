from appium import webdriver
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
            caps["noReset"] = True  # 是否清理数据
            # caps["dontStopAppOnReset"] = True  # 不杀app进程
            caps["chromedriverExecutable"] = "/Users/liumiao/chromedriver/appium/2.20/chromedriver"
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(15)
        else:
            self._driver.start_activity(self._package, self._activity)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main(self._driver)
