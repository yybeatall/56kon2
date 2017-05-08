# usr/bin/python
# encoding:utf-8
# 足迹版测试--帮助站流程
import unittest
from time import sleep
from method56kongps import pickupDelivery
from method import setParam56kongps
from method import commonMethod
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic
from method56kongps import share
from method56kongps import node

class MyTestCase(unittest.TestCase):
    u"""帮助站流程测试"""

    def testHistoryTask(self):
        u"""帮助站流程测试"""
        # TODO:help
        try:
            e1 = self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_upload_photo")
            e2 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_city" )
            self.driver.drag_and_drop(e1, e2)

            '''热门推荐'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_img").click()
            sleep(3)
            self.driver.get_screenshot_as_file("热门推荐.png")


        except Exception as e:
            print(e)


    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
