# usr/bin/python
# encoding:utf-8
# 足迹版测试--我的页面，应用设置，修改个人信息，二维码，更换头像，财富中心，车牌记录
import unittest
from time import sleep

from ddt import ddt, data, unpack

from method56kongps import pickupDelivery
from method import setParam56kongps
from method import commonMethod
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic
from method56kongps import share

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)

    @data("辽A12345","沪B111111","沪BB11111","沪AAAAAAA")
    def testPlateRecordAdd(self,plateNo):
        try:
            '''进入我的页面'''
            self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/bottom_navigation_container" )[3].click( )

            e1 = self.driver.find_element_by_id("com.yihu001.kon.driver:id/state_layout")
            e2 = self.driver.find_element_by_id("com.yihu001.kon.driver:id/contact_layout")
            self.driver.drag_and_drop(e1,e2)

            '''点击车牌记录'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_plate").click()
            #截图--无记录页的显示
            self.driver.get_screenshot_as_file("plate.png")

            #添加车牌
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/add").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_plate").send_keys(plateNo)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_menu").click()


        except Exception as e:
            print(e)

    def testPlateRecordEdit(self):
        try:
            '''进入我的页面'''
            self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/bottom_navigation_container" )[3].click( )

            e1 = self.driver.find_element_by_id("com.yihu001.kon.driver:id/state_layout")
            e2 = self.driver.find_element_by_id("com.yihu001.kon.driver:id/contact_layout")
            self.driver.drag_and_drop(e1,e2)

            '''点击车牌记录'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_plate").click()

            '''编辑车牌'''
            self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_edit" )[0].click( )
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_menu" ).click( )

            '''删除车牌'''
            self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_delete" )[0].click( )

            '''设置默认车牌'''
            self.driver.find_elements_by_class_name( "android.widget.RelativeLayout" )[0].click( )

        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
