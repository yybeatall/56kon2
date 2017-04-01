# usr/bin/python
# encoding:utf-8
# 综合测试--登录
import unittest
from time import sleep

from appium import webdriver
from ddt import ddt, data, unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 天天模拟器
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '127.0.0.1:6555'
        desired_caps['appPackage'] = 'com.yihu001.kon.manager'
        desired_caps['appActivity'] = '.activity.LoginActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        # desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(("13940914601", "123456"))
    @unpack
    def testLogin(self, username, password):
        global exist
        self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_username").send_keys(username)
        self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_password").send_keys(password)
        self.driver.find_element_by_id("com.yihu001.kon.manager:id/sign_in").click()

        sleep(3)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

