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
    # 接收外部传参给steps做参数替换用
    _params = {}

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

    def page_back(self):
        return self._driver.back()

    # 测试步骤的数据驱动函数方法：
    def steps(self, path):
        # 首先打开某路径下文件给变量f
        with open(path) as f:
            # 给steps声明list类型里面存放词典数据，并读取该文件
            steps: list[dict] = yaml.safe_load(f)
            # element变量用appium的WebElement类型，并给个初始值None
            element: WebElement = None
            # 让step循环读取yaml文件内容
            for step in steps:
                # 判断by定位符是否存在
                if "by" in step.keys():
                    # 在的话，find这个定位符给element
                    element = self.find(step["by"], step["locator"])
                # 在判断，action在不在
                if "action" in step.keys():
                    # 在的话，拿出值给action做后续判断
                    action = step["action"]
                    # 拿出来的值判断是不是find，如果是的话默认就find所以pass即可
                    if action == "find":
                        pass
                    # 否则如果是click的话
                    elif action == "click":
                        # 点击element定位符，后面都同理
                        element.click()
                    elif action == "text":
                        element.text
                        # TODO：这里不太明白
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    # 否则如果是一些输入操作，那就牵扯到外部传参的数据替换问题
                    elif action in ["send_keys", "input", "send"]:
                        # 先获取目前的yaml数据值
                        content: str = step["value"]
                        # 之后变量key从上边的词典里找外部传入的动态数据值
                        for key in self._params.keys():
                            # "{%s}"%key 这个key是你step读取出来yaml文件里面的值
                            # self._params[key]是动态的数据，替换进去
                            content = content.replace("{%s}" % key, self._params[key])
                        # 之后把新的数据值进行输入操作
                        element.send_keys(content)
