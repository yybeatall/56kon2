#usr/bin/python
#encoding:utf-8
#综合版测试--创建任务
import unittest
from time import sleep

from business import createTask
from business import changeBusiness

from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        #天天模拟器
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '127.0.0.1:6555'
        desired_caps['appPackage'] = 'com.yihu001.kon.manager'
        desired_caps['appActivity'] = '.activity.HomeActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        #desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testCreateTask(self):
        try:
            #切换企业
            changeBusiness.changeBusiness(self)
            # 点击创建任务
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_create_task").click()
            #创建任务
            createTask.createTask(self)
            #取消
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_cancel").click()
            # 完成
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/submit" ).click()
            sleep(3)
            #直接创建
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/take_one").click()

        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()