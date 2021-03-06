#usr/bin/python
#encoding:utf-8
#综合版测试--创建任务并发送
import unittest
from time import sleep
from method56kon import createTask
from method56kon import changeBusiness
from method56kon import createDelivery
from method import setParam56kon

from appium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kon.setParam( self )

    def testCreateTaskDelivery(self):
        try:
            #切换企业
            changeBusiness.changeBusiness(self)

            # 点击创建任务
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_create_task").click()
            #创建任务
            createTask.createTask(self)

            #创建后直接发送
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/take_three").click()
            sleep(2)

            #发送
            createDelivery.createDelivery(self)
            self.driver.get_screenshot_as_file(setParam56kon.screenCapturePath+"delivery.png")

        except Exception as e:
            print("失败了呢")
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
