# usr/bin/python
# encoding:utf-8
# 足迹版测试--执行定检流程测试
import unittest
from time import sleep

from method import setParam56kongps
from method56kongps import node
from method56kongps import share
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testNode(self):
        try:
            '''从首页定检按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_node").click()
            sleep(3)

            #联系人信息页
            self.driver.find_elements_by_id("com.yihu001.kon.driver:id/iv_pickup_icon")[0].click()
            #截图
            self.driver.get_screenshot_as_file("contactFromNode.png")
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_back").click()


            #点出菜单
            self.driver.find_element_by_class_name("android.widget.LinearLayout").click()

            '''菜单操作项'''
            #任务详情
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()
            taskInfo.taskInfo(self,'')
            print( "任务详情" )

            #运输轨迹
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_track").click()
            trackInfo.trackInfo(self)
            print("运输轨迹")

            #执行定检
            #扫码交接未实现
            #只实现两次滑动
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_event").click()
            #上传照片
            self.driver.find_elements_by_id("com.yihu001.kon.driver:id/btn_upload")[0].click()
            uploadPic.uploadPic(self)
            print("上传照片")

            #执行定检
            node.node(self)

            print( "执行定检" )

            #共享货跟
            #只选了一种共享方式--联系人
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()
            share.shareToContacts(self)
            print( "共享货跟" )

        except Exception as e:
            print(e)


    def tearDown(self):
        print("足迹版测试--执行定检流程测试")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
