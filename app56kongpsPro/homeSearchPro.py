# usr/bin/python
# encoding:utf-8
# 足迹版测试--首页搜索流程
import unittest
from time import sleep
from method56kongps import pickupDelivery
from method import setParam56kongps
from method import commonMethod
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic
from method56kongps import share
from method56kongps import node
from appium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testHomeSearch(self):
        searchContent = '1'

        try:
            '''从首页搜索框进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_search").click()
            sleep(2)

            #输入搜索内容
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/edit").send_keys(searchContent)
            self.driver.remove_app("io.appium.android.ime")
            self.driver.keyevent(66)

            sleep(3)

            #排序筛选
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_sort_by").click()
            self.driver.find_elements_by_class_name("android.widget.RelativeLayout")[1].click()
            sleep( 2 )

            #状态筛选
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_status").click()
            self.driver.find_elements_by_class_name( "android.widget.RelativeLayout" )[4].click( )
            sleep( 2 )

            '''菜单'''
            if commonMethod.isElement( self, "id","com.yihu001.kon.driver:id/tv_code"):
                self.driver.find_elements_by_id("com.yihu001.kon.driver:id/tv_code")[0].click( )
            else:
                print("没有搜索结果")

            #任务信息
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()
            taskInfo.taskInfo(self,'')

            #运输轨迹
            if commonMethod.isElement(self,"id","com.yihu001.kon.driver:id/tv_task_track"):
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_track").click()
                trackInfo.trackInfo(self)

            #拒接任务
            if commonMethod.isElement(self,"id","com.yihu001.kon.driver:id/tv_task_refuse"):
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_refuse").click()
                #任务拒绝后换出下一个任务的菜单
                if commonMethod.isElement( self, "id","com.yihu001.kon.driver:id/tv_code"):
                    commonMethod.isElement( self, "id", "com.yihu001.kon.driver:id/tv_code" ).click( )
                else:
                    print( "拒绝任务后没有搜索结果" )

           #提货/到货交接
            if commonMethod.isElement(self,"id","com.yihu001.kon.driver:id/tv_task_handover"):
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_handover").click()
                self.driver.find_element_by_id( "com.yihu001.kon.driver:id/handover" ).click( )


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


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
