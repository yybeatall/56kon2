# usr/bin/python
# encoding:utf-8
# 足迹版测试--首页执行交接流程
import unittest
from time import sleep
from method56kongps import pickupDelivery
from method import setParam56kongps
from method56kongps import taskInfo

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testHandover(self):
        try:
            '''从首页交接按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_handover").click()
            sleep(3)
            # #提货交接
            # pickupDelivery.pickup(self)
            # sleep(3)
            # #到货交接
            # pickupDelivery.delivery(self)

            self.driver.find_element_by_xpath( '//android.widget.TextView[@text="提"]' ).click( )
            self.driver.find_element_by_class_name("android.widget.LinearLayout").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()

            taskInfo.taskInfo(self,"pickup")


        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
