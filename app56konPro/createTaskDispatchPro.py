#usr/bin/python
#encoding:utf-8
#综合版测试--创建任务并调度
import unittest
from time import sleep

from ddt import ddt,data,unpack

from method56kon import createTask
from method56kon import createschedule
from method56kon import changeBusiness
from method import setParam56kon
from method import location

from appium import webdriver

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kon.setParam( self )

    @data( *location.getDdtExcel('task.xlsx') )
    @unpack
    def testCreateTaskDispatch(self,goodsName,goodsCount,goodsWeight,goodsVolume,
               seller,sellerContact,startCity,fromWhere,
               buyer,buyerContact,endCity,toWhere,
               memo):
        try:
            #切换企业
            changeBusiness.changeBusiness(self)

            # 点击创建任务
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_create_task").click()
            #创建任务
            createTask.createTask(self,goodsName,goodsCount,goodsWeight,goodsVolume,
               seller,sellerContact,startCity,fromWhere,
               buyer,buyerContact,endCity,toWhere,
               memo)

            #创建后直接调度
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/take_two").click()
            sleep(2)

            #调度
            createschedule.createschedule( self )
            #调度提示图
            self.driver.get_screenshot_as_file("dispatch.png")

        except Exception as e:
            print("失败了呢")
            print(e)


    def tearDown(self):
        print("综合版测试--创建任务并调度")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
