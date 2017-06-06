# usr/bin/python
# encoding:utf-8
# 微信小程序
import unittest
from time import sleep

from appium import webdriver
#from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # 天天模拟器
        # desired_caps['platformVersion'] = '4.4.4'
        # desired_caps['deviceName'] = '127.0.0.1:6555'

        # 夜神模拟器
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = '127.0.0.1:62001'

        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps["noReset"] = "true"
        desired_caps["automationName"] = "Selendroid"
        desired_caps["app"] = "/Users/yuyang/Downloads/weixin.apk"
        #desired_caps["autoWebview"] = "true"

        # option = webdriver.ChromeOptions()
        # option.add_experimental_option('androidProcess','com.tencent.mm:appbrand1')
        # desired_caps.update(option.to_capabilities())

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testApp(self):
        sleep(5)
        self.driver.find_elements_by_id("brd")[2].click()
        self.driver.find_elements_by_id("bs1")[6].click()
        sleep(3)
        self.driver.find_elements_by_id("j6")[0].click()
        sleep(1)

        print(self.driver.current_context)
        sleep(5)
        print(self.driver.page_source)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
