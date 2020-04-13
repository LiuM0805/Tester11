import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging


class BasePage:
    # 初始化日志，给定日志级别
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    # 黑名单
    _black_list = [
        (By.ID, "tv_agree"),
        (By.XPATH, "//*[@text='确定']"),
        (By.ID, "image_cancel"),
        (By.ID, "tv_left")
    ]
    _error_max = 10
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # todo:当有广告、评价等各种弹框出现的时候，要进行异常处理
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        try:
            # 查找控件
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # 如果查找成功，清空错误计数
            self._error_count = 0
            return element

        except Exception as e:
            # 统计异常处理次数，超出指定次数，直接报错
            if self._error_count > self._error_max:
                raise e
            # 记录异常次数
            self._error_count += 1
            # 让element把黑名单内容都拿出来
            for element in self._black_list:
                logging.info(element)
                # 用elements找黑名单是因为找不到也不报错
                elements = self._driver.find_elements(*element)
                # 如果elements大于0，证明找到了匹配的弹框
                if len(elements) > 0:
                    # 找到了就点了它
                    elements[0].click()
                    # 继续寻找原来的控件
                    return self.find(locator, value)
            # 如果所有都没找到，也报错
            logging.warn("black list no one found")
            raise e
            # 如果黑名单也没有，还可以继续find一次，如果还没有，直接报错
            # return self.find(locator, value)
            # raise e

    # todo: 通用异常 通过装饰器让函数自动处理异常
    def find_and_get_text(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        try:
            # 查找控件
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # 如果查找成功，清空错误计数
            self._error_count = 0
            return element.text

        except Exception as e:
            # 统计异常处理次数，超出指定次数，直接报错
            if self._error_count > self._error_max:
                raise e
            # 记录异常次数
            self._error_count += 1
            # 让element把黑名单内容都拿出来
            for element in self._black_list:
                logging.info(element)
                # 用elements找黑名单是因为找不到也不报错
                elements = self._driver.find_elements(*element)
                # 如果elements大于0，证明找到了匹配的弹框
                if len(elements) > 0:
                    # 找到了就点了它
                    elements[0].click()
                    # 继续寻找原来的控件
                    return self.find_and_get_text(locator, value)
            # 如果所有都没找到，也报错
            logging.warn("black list no one found")
            raise e
            # 如果黑名单也没有，还可以继续find一次，如果还没有，直接报错
            # return self.find(locator, value)
            # raise e

    def get_toast(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        return self.find(self.text(key))

    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send_keys", "input", "send"]:
                        element.send_keys(step["value"])
