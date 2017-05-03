# usr/bin/python
# encoding:utf-8
# 足迹版测试--我的共享流程测试
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


    def testShare(self):
        sharePhone = "13940914601"
        try:
            '''从首页我的共享按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_share").click()
            sleep(3)

            #按从老到新排序
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_sort_by").click()
            self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()
            sleep(3)

            #联系人信息
            self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_pickup_icon")[0].click()
            self.driver.get_screenshot_as_file("contactShare.png")
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_back").click()

            #筛选已完成
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_status").click()
            self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[5].click()
            sleep(3)


            '''菜单'''
            self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/boot" )[0].click( )

            #任务信息
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()
            taskInfo.taskInfo(self,'')

            #运输轨迹
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_track").click()
            trackInfo.trackInfo(self)

            #编辑共享
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_edit_share").click()

            # 添加共享对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 3:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-2].click( )
            elif count == 2:
                self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")[1].click()

            #联系人
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_one").click()
            self.driver.find_element_by_xpath(
                '//android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget'
                '.RelativeLayout[contains(@index,0)]' ).click( )
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )

            # 添加共享对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 3:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-2].click( )
            elif count == 2:
                self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")[1].click()

            #分组
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_two").click()
            self.driver.find_elements_by_class_name( "android.widget.RelativeLayout" )[0].click( )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()


            # 添加共享对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 3:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-2].click( )
            elif count == 2:
                self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")[1].click()

            #手机号码
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_three").click()
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/et_phone" ).send_keys( sharePhone )
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_menu" ).click( )

            # 添加共享对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 3:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-2].click( )
            elif count == 2:
                self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")[1].click()

            #通讯录,真机测试
            #self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_four").click()

            #取消
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_cancel").click()

            # 移除共享对象
            list = self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")
            count = len(list)
            if count > 3:
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_user" )[count-1].click( )
            elif count == 2:
                self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_user")[1].click()

            self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_delete")[0].click()

            self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            #撤回共享
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_revoke_share").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()


        except Exception as e:
            print(e)


    def tearDown(self):
        print( "足迹版测试--我的共享流程测试" )
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
