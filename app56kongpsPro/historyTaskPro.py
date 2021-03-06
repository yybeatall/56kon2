# usr/bin/python
# encoding:utf-8
# 足迹版测试--历史任务流程测试
import unittest
from time import sleep

from method import commonMethod
from method import setParam56kongps
from method56kongps import node
from method56kongps import share
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic

shotPath = setParam56kongps.screenCapturePath + "历史任务流程测试/"+setParam56kongps.now

class MyTestCase(unittest.TestCase):
    u"""历史任务流程测试"""
    def setUp(self):
        self.driver = setParam56kongps.setParam(self,"")


    def testHistoryTask(self):
        u"""历史任务流程测试"""

        try:
            '''从首页历史任务按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_history").click()
            sleep(3)

            #调度单号筛选
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_scno").click()
            self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[4].click()
            sleep(3)

            #联系人信息
            self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_pickup_icon")[0].click()
            self.driver.get_screenshot_as_file(shotPath+"contactHistory.png")
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_back").click()


            '''菜单'''
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_order_no" ).click( )

            #任务信息
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()
            taskInfo.taskInfo(self,'')

            #运输轨迹
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_track").click()
            trackInfo.trackInfo(self)

            #上传照片
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_picture").click()
            uploadPic.uploadPicFirst(self)
            self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )

            #执行定检
            if commonMethod.isElement(self,"id","com.yihu001.kon.driver:id/tv_task_event"):
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_event").click()
                node.node(self)

            #共享货跟
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            share.shareToPhone(self)


        except Exception as e:
            print(e)
            print( "足迹版测试--历史任务流程测试" )


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
