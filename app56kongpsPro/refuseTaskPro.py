# usr/bin/python
# encoding:utf-8
# 足迹版测试--司机拒绝任务流程
# 数据准备：需要提到货相同的三个任务
import unittest
from time import sleep

from method import setParam56kongps


class MyTestCase(unittest.TestCase):
    u"""司机拒绝任务流程测试"""
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testHandover(self):
        u"""司机拒绝任务流程测试"""
        try:
            '''从首页交接按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_handover").click()
            sleep(3)

            '''单个任务操作--提货'''
            self.driver.find_element_by_xpath( '//android.widget.TextView[@text="提"]' ).click( )
            self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]').click()

            #拒绝任务
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_refuse").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()

            #验证


        except Exception as e:
            print("足迹版测试--司机拒绝任务流程")
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
