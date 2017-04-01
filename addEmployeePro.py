# usr/bin/python
# encoding:utf-8
# 综合版测试--添加员工
import unittest
from time import sleep

from appium import webdriver


class MyTestCase( unittest.TestCase ):
    def setUp(self):
        # 天天模拟器
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '127.0.0.1:6555'
        desired_caps['appPackage'] = 'com.yihu001.kon.manager'
        desired_caps['appActivity'] = '.activity.HomeActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        # desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote( 'http://localhost:4723/wd/hub', desired_caps )

    def testAddEmployee(self):
        employee = "13900000331"
        try:
            sleep(3)
            #点击企业员工
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_staff").click()
            #点击帮助
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/help").click()
            sleep(3)
            #截屏
            self.driver.get_screenshot_as_file("com.yihu001.kon.manager:id/help")
            #返回
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            #滑动
            self.driver.swipe( 600, 470, 260, 470 )
            #邀请员工
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/iv_invite").click()
            # 滑动
            self.driver.swipe( 600, 470, 260, 470 )
            #删除员工
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/iv_delete" ).click( )
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/take_one").click()
            #点击添加员工
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/add").click()
            #员工手机
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_phone").send_keys(employee)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_menu").click()
            #联系人信息
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/iv_employee").click()
            sleep(1)
            # 截屏
            self.driver.get_screenshot_as_file( "com.yihu001.kon.manager:id/help" )
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/iv_back").click()

        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit( )


if __name__ == '__main__':
    unittest.main( )














