# usr/bin/python
# encoding:utf-8
# 足迹版测试--从批量交接进入单个任务执行提货交接流程
# 数据准备：需要提到货相同的三个任务
import unittest
from time import sleep

from method import setParam56kongps
from method56kongps import share
from method56kongps import taskInfo
from method56kongps import uploadPic


class MyTestCase(unittest.TestCase):
    u"""从批量交接进入单个任务执行提货交接流程"""
    def setUp(self):
        self.driver = setParam56kongps.setParam(self,"")


    def testHandover(self):
        u"""从批量交接进入单个任务执行提货交接流程"""
        try:
            '''从首页交接按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_handover").click()
            sleep(3)

            '''提货'''

            '''单个任务操作--提货'''
            self.driver.find_element_by_xpath( '//android.widget.TextView[@text="提"]' ).click( )
            self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]').click()

            '''菜单操作项'''
            # 任务详情
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()
            taskInfo.taskInfo(self,"")
            u"""任务详情"""

            #上传照片
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_picture").click()
            uploadPic.uploadPicFirst(self)

            #返回
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

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

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/toolbar_right").click()
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]').click()
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=1]' ).click( )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            share.shareToGroup( self )

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/toolbar_right").click()
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]').click()
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=1]' ).click( )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            share.shareToPhone( self )

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/toolbar_right").click()
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]').click()
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=1]' ).click( )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/share").click()
            share.cancle( self )

            #批量交接
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_cancel").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
            sleep(3)
            #self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            #唤出菜单
            self.driver.find_element_by_xpath(
                '//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[@index=0]').click()

            # 提货交接
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_handover").click()

            # 确认提货
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_handover").click()
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()


        except Exception as e:
            print(e)


    def tearDown(self):
        print( "足迹版测试--从批量交接进入单个任务执行提货交接流程" )
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
