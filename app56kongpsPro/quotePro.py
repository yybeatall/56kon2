# usr/bin/python
# encoding:utf-8
# 足迹版测试--询价流程测试
import unittest
from time import sleep
from method56kongps import pickupDelivery
from method import setParam56kongps
from method import commonMethod
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic
from method56kongps import quotePublishPost


class MyTestCase(unittest.TestCase):
    u"""询价流程测试"""
    # def setUp(self):
    #     self.driver = setParam56kongps.setParam(self)


    def testQuote(self):
        u"""询价流程测试"""
        # TODO:未完成

        try:
            result = quotePublishPost.testPost(self)
            print(result)

            # '''首页点击进入询价进行中页面'''
            # e1 = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/tv_upload_photo")
            # e2 = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_handover")
            # self.driver.drag_and_drop(e1,e2)
            #
            # self.driver.find_element_by_xpath('//android.widget.TextView[@text="立刻报价"]').click()
            #
            # #点击竞价进行中的询价
            # self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[@index,0]').click()
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_quote").click()



        except Exception as e:
            print(e)


    # def tearDown(self):
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
