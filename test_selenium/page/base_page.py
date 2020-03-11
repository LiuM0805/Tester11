from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver


# 这是专门存放driver的
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse is True:
                options = webdriver.ChromeOptions()
                # 使用已经存在的chrome进程
                # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --remote-debugging-port=9222
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                # indexPO会使用这个
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
        else:
            # login和register使用这个
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def elements(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)

    def wait(self, timeout, method):
        WebDriverWait(self._driver, timeout).until(method)

    def move_mouse(self, locator):
        webdriver.ActionChains(self._driver).move_to_element(locator).perform()

    def clear_input(self, locator):
        input_element=self.find(locator)
        try:
            input_element.clear()
        except Exception :
            print("清空输入框失败")
        else:
            print("清空成功")


    def close(self):
        sleep(3)
        self._driver.quit()
