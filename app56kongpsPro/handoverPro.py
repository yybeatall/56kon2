# usr/bin/python
# encoding:utf-8
# 足迹版测试--首页执行交接流程
import unittest
from time import sleep
from method56kongps import pickupDelivery
from method import setParam56kongps
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic
from method56kongps import share

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testHandover(self):
        try:
            '''从首页交接按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_handover").click()
            sleep(3)

            '''批量提到货'''
            # #提货交接
            # pickupDelivery.pickup(self)
            # sleep(3)
            # #到货交接
            # pickupDelivery.delivery(self)

            '''单个任务操作--提货'''
            self.driver.find_element_by_xpath( '//android.widget.TextView[@text="提"]' ).click( )
            self.driver.find_element_by_class_name("android.widget.LinearLayout").click()

            '''菜单操作项'''
            # 任务详情
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()
            taskInfo.taskInfo(self,"pickup")

            #提货交接
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_handover").click()
            #确认提货
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            # #拒绝任务
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_refuse").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()

            #上传照片
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_picture").click()
            uploadPic.uploadPicFirst(self,3)

            #返回
            self.driver.find_element_by_id("android.widget.ImageButton").click()

            #共享货跟
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            share.shareToContacts(self)

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            share.shareToGroup(self)

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            share.shareToPhone(self)

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            share.shareToAddrList(self)

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            share.cancle(self)

            #批量操作任务
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/toolbar_right").click()
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]').click()
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=1]' ).click( )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            share.shareToContacts( self )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            share.shareToGroup( self )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            share.shareToPhone( self )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            share.cancle( self )

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_cancel").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
            sleep(3)
            self.driver.find_element_by_id("android.widget.ImageButton").click()

            '''单个任务操作--到货'''
            #self.driver.find_element_by_xpath( '//android.widget.TextView[@text="提"]' ).click( )
            #self.driver.find_element_by_class_name("android.widget.LinearLayout").click()

            '''菜单操作项'''
            # 任务详情
            #self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()
            #taskInfo.taskInfo(self,"pickup")

            # #提货交接
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_handover").click()
            # #确认提货
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            # self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            # #拒绝任务
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_refuse").click()
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()

            #上传照片
            #self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_picture").click()
            #uploadPic.uploadPicFirst(self,3)

            #返回
            #self.driver.find_element_by_id("android.widget.ImageButton").click()

            #共享货跟
            #self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            #share.shareToContacts(self)

            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            # share.shareToGroup(self)
            #
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            # share.shareToPhone(self)
            #
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            # share.shareToAddrList(self)
            #
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            # share.cancle(self)

            #批量操作任务
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/toolbar_right").click()
            # self.driver.find_element_by_xpath(
            #     '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]').click()
            # self.driver.find_element_by_xpath(
            #     '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=1]' ).click( )
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            # share.shareToContacts( self )
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            # share.shareToGroup( self )
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            # share.shareToPhone( self )
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            # share.cancle( self )

            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_cancel").click()
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
            # sleep(3)
            # self.driver.find_element_by_id("android.widget.ImageButton").click()


            #选择到货任务

            #菜单操作

            #任务信息

            #运输轨迹

            #到货交接

            #上传照片

            #共享货跟


            #批量操作任务











            # '''到货的上传照片'''
            # # 上传照片
            # self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_task_picture" ).click( )
            # uploadPic.uploadPicFirst( self, 3 )
            #
            # # 向下滑动
            # e1 = self.driver.find_elements_by_xpath( '//android.widget.TextView[contains(@text,"到货")]' )
            # e2 = self.driver.find_elements_by_xpath( '//android.widget.TextView[contains(@text,"车况")]' )
            # self.driver.drag_and_drop( e1, e2 )
            #
            # uploadPic.uploadpicAgain( self, 2 )
            #
            # #运输轨迹
            # self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_track").click()
            # sleep(2)
            # # 截图
            # self.driver.get_screenshot_as_file( "track.png" )
            # trackInfo.trackInfo(self)


        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
