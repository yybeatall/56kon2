# encoding:utf-8
# 综合测试--忘记密码
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
        desired_caps['appActivity'] = '.activity.HomeActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        # desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    @data(("13940914601", "123456"))
    @unpack
    def testRegister(self, username, password):
        try:

            global exist
            sleep(3)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/forget_pwd").click()

            sleep(3)

            # 忘记密码
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/mobile_number").send_keys(username)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/get_checkcode").click()
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_password").send_keys(password)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/register").click()
            sleep(3)

            #重新登录
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_password").send_keys(password)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/sign_in").click()

        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
