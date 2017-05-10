# usr/bin/python
# encoding:utf-8
# 足迹版测试--注销流程测试
import unittest
from time import sleep
import time

from method import setParam56kongps
from method56kongps import logout

now = time.strftime("%Y-%m-%d %H_%M_%S")
shotPath = setParam56kongps.screenCapturePath + "注销/"+now

class MyTestCase(unittest.TestCase):
    u"""注销流程测试"""
    def setUp(self):
        u"""setup"""
        self.driver = setParam56kongps.setParam( self )
    def testLogout(self):
        u"""注销流程测试"""
        logout.logout(self)
        sleep(3)
        self.driver.get_screenshot_as_file(shotPath+"logout.png")

    def tearDown(self):
        u"""teardown"""
        print("足迹版测试--注销")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
