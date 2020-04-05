# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["noReset"] = True  # 是否清理数据
        caps["dontStopAppOnReset"] = True  # 不杀app进程
        # caps["unicodeKeyBoard"] = True  # 输入中文
        # caps["resetKeyBoard"] = True  # 恢复输入法
        # caps["autoGrantPermissions"] = True  # 忽略权限，但还是有权限访问，比如相机权限，不能和清理数据一起使用
        # caps["skipServerInstallation"] = True  # 跳过uiautomator2 server的安装
        # caps["chromedriverExecutableDir"] = "/Users/liumiao/chromedriver/2.20" # 指定driver路径，让系统选择合适的版本
        caps["chromedriverExecutable"] = "/Users/liumiao/chromedriver/appium/2.20/chromedriver"  # 指定driver文件，强制执行
        # caps["avd"] = "Pixel_2_API_23" # 启动模拟器

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

    # 使用原生定位方式测试webview组件
    def test_webview_native(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易" and contains(@resource-id, "tab")]').click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'A股开户').click()
        # self.driver.find_element(MobileBy.ID, 'phone-number').send_keys("18810143185")
        phone = (MobileBy.ACCESSIBILITY_ID, '输入11位手机号')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(phone))
        self.driver.find_element(*phone).click()
        print(self.driver.page_source)
        print(self.driver.find_element(*phone).get_attribute("content-desc"))
        # 使用原生定位时，send_keys失败
        self.driver.find_element(*phone).send_keys("18810143185")

    # 使用chrome调试模式定位，测试webview组件
    def test_webview_debug(self):
        # 下面代码表示：在原生页面点击交易进入webview页面
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易" and contains(@resource-id, "tab")]').click()

        # 测试webview时，用于分析当前的上下文
        # for i in range(5):
        #     print(self.driver.contexts)
        #     sleep(1)
        # print(self.driver.page_source)

        # 坑1：webview上下文的出现大概有3s延迟，所以加显示等待和表达式
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.contexts) > 1)
        # 坑2：chromedriver的版本与Chrome版本必须对应
        # 坑3：chromedriver出现无法对应版本的情况，需要使用caps的MappingFile或者Executable
        # Spawning chromedriver with: /Users/liumiao/chromedriver/2.20/chromedriver --url-base=wd/hub --port=8000 --adb-port=5037 --verbose
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.page_source)

        # 测试webview时，用于分析当前的窗口句柄
        # print(self.driver.window_handles)
        # 坑4：学会使用chrome的inspect分析页面控件，需要翻墙，需要Chrome62版本
        self.driver.find_element(By.CSS_SELECTOR, '.trade_home_info_3aI').click()
        # for i in range(5):
        #     print(self.driver.window_handles)
        #     sleep(1)

        # 坑5：可能会出现多窗口，注意等待、判断、切换
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.window_handles) > 3)
        # 下面代码表示：由于进入A股开户后，新增了多个窗口，切换到输入手机号的窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 等待手机号元素在dom中显示
        phone = (By.ID, 'phone-number')
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_all_elements_located(phone))
        self.driver.find_element(*phone).send_keys("18810143184")

    def test_xueqiu_webview(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易" and contains(@resource-id, "tab")]').click()
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR, '.trade_home_xueying_SJY').click()
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.XPATH, "//input[@placeholder='请输入手机号']")
        code = (By.XPATH, "//input[@placeholder='请输入验证码']")
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_all_elements_located(phone))
        self.driver.find_element(*phone).send_keys("18810143184")
        self.driver.find_element(*code).send_keys("1234")
        button = (By.CSS_SELECTOR, '.open_form-submit_1Ms')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(button))
        self.driver.find_element(*button).click()
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[0])
        returned = (MobileBy.ID, "action_bar_back")
        # closed=(MobileBy.ID, '.action_bar_close')
        # WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(closed))
        # self.driver.find_element(*closed).click()
        self.driver.find_element(*returned).click()

    def test_performance(self):
        # 获取性能数据
        for q in self.driver.get_performance_data_types():
            print(q)

            print(self.driver.get_performance_data("com.xueqiu.android", q, 10))

    def teardown(self):
        pass
        # sleep(5)
        # self.driver.quit()
