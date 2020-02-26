import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Testerhome:
    def setup_method(self):
        browser = os.getenv("browser", "").lower()
        print(browser)

        if browser == "headless":
            self.driver = webdriver.PhantomJS()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            options = webdriver.ChromeOptions()
            # 使用headless模式
            # options.add_argument("--headless")
            # options.add_argument("--window-size=1280,1696")

            # 使用已经存在的chrome进程
            # options.debugger_address="127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_testerhome(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(2)
        # element = (By.CSS_SELECTOR, "[data-name='霍格沃兹测试学院']")
        element = (By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name=霍格沃兹测试学院]').click()
        # self.driver.find_element(By.CSS_SELECTOR, '.topic-22235 .title > a').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def test_study(self):
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').click()
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys("MTSC2020")
        self.driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, '.result:nth-child(1) .topic a').click()
        self.driver.find_element(By.CSS_SELECTOR, '[data-toggle="dropdown"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.list-container ul li:nth-child(4) a').click()

    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        mywait = (By.PARTIAL_LINK_TEXT, '第六届中国互联网测试开发大会')
        self.wait(10, expected_conditions.element_to_be_clickable(mywait))
        self.driver.find_element(*mywait).click()
        print(self.driver.window_handles)
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '演讲申请').click()

    def test_js(self):
        # todo:专项测试时讲如何获取性能
        for code in [
            'return document.title',
            'return document.querySelector(".active").className',
            'return JSON.stringify(performance.timing)'
        ]:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self):
        sleep(2)
        self.driver.quit()
