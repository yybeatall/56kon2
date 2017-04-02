#usr/bin/python
#encoding:utf-8
#综合版测试--创建任务并调度
import unittest
from time import sleep
from business import createTask
from business import createschedule
from business import changeBusiness
from method import setParam

from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        setParam.setParam(self)

    def testCreateTaskDispatch(self):
        try:
            #切换企业
            changeBusiness.changeBusiness(self)

            # 点击创建任务
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_create_task").click()
            #创建任务
            createTask.createTask(self)

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
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
