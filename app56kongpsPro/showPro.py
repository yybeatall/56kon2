# usr/bin/python
# encoding:utf-8
# 足迹版测试--秀足迹流程测试
import unittest
from time import sleep
from method56kongps import pickupDelivery
from method import setParam56kongps
from method import commonMethod
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic
from method56kongps import share

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testShow(self):
        plateNo = "辽A12345"
        reportPhone = "13940914601"
        try:
            if commonMethod.isElement(self,"xpath",'//android.widget.TextView[@text="停止上报"]'):
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_start").click()

            '''从首页秀足迹按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_one_key").click()
            sleep(3)

            '''创建秀足迹'''
            # 选择车牌
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_select" ).click( )
            self.driver.find_elements_by_class_name( "android.widget.RelativeLayout" )[1].click( )

            #填入车牌
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_plate").clear()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_plate").send_keys(plateNo)

            #选择上报间隔
            #选择结束时间

            #添加报告对象
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_user").click()

            #授信企业
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_first").click()
            if commonMethod.isElement(self,"class","android.widget.RelativeLayout"):
                self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[0].click()
                self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )
            else:
                self.driver.find_elements_by_class_name("android.widget.ImageButton").click()

            # 添加报告对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 1:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-2].click( )

            #联系人
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_one").click()
            self.driver.find_element_by_xpath(
                '//android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget'
                '.RelativeLayout[contains(@index,0)]' ).click( )
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )

            # 添加报告对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 1:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-2].click( )

            #分组
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_two").click()
            self.driver.find_elements_by_class_name( "android.widget.RelativeLayout" )[0].click( )

            # 添加报告对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 1:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-2].click( )

            #手机号码
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_three").click()
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/et_phone" ).send_keys( reportPhone )
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_menu" ).click( )

            # 添加报告对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 1:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-2].click( )

            #通讯录,真机测试
            #self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_four").click()

            #取消
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_cancel").click()

            #开始上报
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_start").click()


        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
