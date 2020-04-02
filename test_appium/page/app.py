from appium import webdriver

from test_appium.page.main import Main


class App:
    def start(self):
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
        caps["chromedriverExecutable"] = "/Users/liumiao/chromedriver/2.20/chromedriver"  # 指定driver文件，强制执行
        # caps["avd"] = "Pixel_2_API_23" # 启动模拟器

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main(self.driver)
