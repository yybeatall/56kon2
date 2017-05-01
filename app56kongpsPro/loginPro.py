# usr/bin/python
# encoding:utf-8
# 足迹版测试--登录
import unittest
from time import sleep

from ddt import ddt, data, unpack

from method import setParam56kongps


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam( self )

    @data(("13900000417", "111111"))
    @unpack
    def testLogin(self, username, password):
        global exist

        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_name").send_keys(username)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_pwd").send_keys(password)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").click()

        sleep(3)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

