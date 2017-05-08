# usr/bin/python
# encoding:utf-8
# 足迹版测试--首页提货交接流程
# 数据准备：需要存在预提时间5天内的提货任务
import unittest
from time import sleep

from method import setParam56kongps
from method import commonMethod
from method56kongps import pickupDelivery


class MyTestCase(unittest.TestCase):
    u"""首页提货交接流程测试"""
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testHandoverBatch(self):
        u"""首页提货交接流程测试"""
        try:
            '''从首页待提区域进入'''
            if commonMethod.isElement(self,"id","com.yihu001.kon.driver:id/tv_pickup_count"):
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_pickup_count").click()
                sleep(3)

                '''批量提货'''
                #提货交接
                pickupDelivery.pickup(self)
                sleep(5)

                self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            else:
                print("不存在提货任务")

        except Exception as e:
            print(e)


    def tearDown(self):
        print("足迹版测试--首页提货交接流程")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
