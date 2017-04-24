# usr/bin/python
# encoding:utf-8
# 足迹版测试--首页执行批量交接流程
# 数据准备：需要提到货任务
import unittest
from time import sleep

from method import setParam56kongps
from method56kongps import pickupDelivery


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testHandoverBatch(self):
        try:
            '''从首页交接按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_handover").click()
            sleep(3)

            '''批量提到货'''
            #提货交接
            pickupDelivery.pickup(self)
            sleep(5)
            #到货交接
            pickupDelivery.delivery(self)

        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()