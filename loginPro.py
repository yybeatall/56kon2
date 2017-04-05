# usr/bin/python
# encoding:utf-8
# 综合测试--登录
import unittest
from time import sleep
from method import setParam
from appium import webdriver
from ddt import ddt, data, unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam.setParam(self)

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

