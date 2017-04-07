# usr/bin/python
# encoding:utf-8
# 足迹版测试--首页执行交接流程
import unittest
from time import sleep
from method56kongps import pickupDelivery
from method import setParam56kongps
from method56kongps import taskInfo
from method56kongps import trackInfo
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)


    def testHandover(self):
        try:
            '''从首页交接按钮进入'''
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_handover").click()
            sleep(3)
            # #提货交接
            # pickupDelivery.pickup(self)
            # sleep(3)
            # #到货交接
            # pickupDelivery.delivery(self)

            #选择提货任务
            self.driver.find_element_by_xpath( '//android.widget.TextView[@text="提"]' ).click( )
            self.driver.find_element_by_class_name("android.widget.LinearLayout").click()

            '''菜单操作项'''
            #self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_detail").click()
            #任务详情
            #taskInfo.taskInfo(self,"pickup")

            #提货交接
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_handover").click()
            #确认提货
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/handover").click()
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            #拒绝任务
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_refuse").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()

            #上传照片
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_picture").click()
            self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/android.widget.LinearLayout/'
                                              'android.widget.RelativeLayout/android.widget.ImageView[contains(@index,0)]')
            #拍照
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_one").click()
            #真机测试

            #从手机相册选择
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_two").click()
            self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                              'android.widget.RelativeLayout[1]/android.widget.ImageView[contains(@index,0)]')
            self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                              'android.widget.RelativeLayout[1]/android.widget.ImageView[contains(@index,1)]')
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
            #继续添加
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/add").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_two").click()
            self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                              'android.widget.RelativeLayout[1]/android.widget.ImageView[contains(@index,0)]')
            self.driver.find_element_by_xpath('//android.support.v7.widget.RecyclerView/'
                                              'android.widget.RelativeLayout[1]/android.widget.ImageView[contains(@index,1)]')
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_upload").click()
            #返回
            self.driver.find_element_by_id("android.widget.ImageButton").click()

            #继续添加---这里可以自己掉自己了

            #取消
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_cancel").click()

            #共享货跟
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_share").click()

            #批量操作任务



            #选择到货任务

            #菜单操作

            #任务信息

            #运输轨迹

            #到货交接

            #上传照片

            #共享货跟


            #批量操作任务

















            #运输轨迹
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_task_track").click()
            sleep(2)
            # 截图
            self.driver.get_screenshot_as_file( "track.png" )
            trackInfo.trackInfo(self)


        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
