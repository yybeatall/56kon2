#usr/bin/python
#encoding:utf-8
#综合版测试--创建调度
import unittest
from time import sleep
from business import createschedule
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

    def testCreateSchedule(self):
        try:
            #切换企业
            changeBusiness.changeBusiness(self)
            # 点击创建调度
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_create_schedule").click()
            #创建调度
            createschedule.createschedule(self)
            #点击加号
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/add").click()
            #返回
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/ic_back").click()
            #点击添加任务按钮
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/no_data_create").click()
            #搜索
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/search_edit").send_keys("每日货物")
            #回车
            self.driver.keyevent(66)
            #添加任务
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/add_task").click()
            #返回
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/ic_back").click()
            #完成调度
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/submit_layout").click()
            sleep(3)

        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()