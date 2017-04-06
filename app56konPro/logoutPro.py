# usr/bin/python
# encoding:utf-8
# 足迹版测试--注销
import unittest
from time import sleep

from method import setParam56kon


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kon.setParam( self )
    def testLogout(self):
        #点击我的
        self.driver.find_elements_by_id("com.yihu001.kon.manager:id/bottom_navigation_container")[3].click()
        #点击设置按钮
        self.driver.find_element_by_id("com.yihu001.kon.manager:id/ib_profile_set").click()
        #滑动
        #self.driver.swipe(500,1000,500,400)
        e1=self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_update_password")
        e2=self.driver.find_element_by_id("com.yihu001.kon.manager:id/image_cache_layout")
        self.driver.scroll(e1,e2)
        sleep(2)
        #点击退出
        self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_loginout").click()
        #确定
        self.driver.find_element_by_id("com.yihu001.kon.manager:id/dialog_button_ok").click()
        sleep(3)
        #切换用户
        self.driver.find_element_by_id("com.yihu001.kon.manager:id/login_type").click()
        sleep(3)
        self.driver.get_screenshot_as_file("logout.png")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
