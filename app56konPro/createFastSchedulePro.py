# usr/bin/python
# encoding:utf-8
# 综合版测试--极速配货
import unittest
from time import sleep
import time
from method56kon import changeBusiness
from method import setParam56kon

from appium import webdriver


class MyTestCase( unittest.TestCase ):
    def setUp(self):
        self.driver = setParam56kon.setParam( self )

    def testCreateTaskDispatch(self):
        try:
            # 切换企业
            changeBusiness.changeBusiness( self )

            # 点击创建任务
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/rl_fast_schedule" ).click( )

            # 创建任务
            goodsName = "每日货物"
            goodsCount = "10"
            goodsWeight = "100"
            goodsVolume = "200"

            seller = "发货方"
            sellerContact = "13811111111"
            startCity = "北京"
            fromWhere = "北京市朝阳区望京东园523号融科望京中心B座"

            buyer = "收货方"
            buyerContact = "13822222222"
            endCity = "上海"
            toWhere = "上海市浦东新区浦东大道国际航运金融大厦"

            #调度部分
            scheduleNo = time.strftime( '%Y%m%d%X', time.localtime( ) )
            truckNo = "辽A12345"
            driverContact = "13900001127"
            driverName = "1127"

            '''基本信息'''
            # 输入货物名称
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/tv_goods_name" ).send_keys( goodsName )
            # 输入货物数量
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/goods_quantity" ).send_keys( goodsCount )
            # 输入货物重量
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/goods_weight" ).send_keys( goodsWeight )
            # 输入货物体积
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/goods_volume" ).send_keys( goodsVolume )

            '''提货信息'''
            # 输入发货方
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/seller" ).send_keys( seller )
            # 将页面向上滑动
            # els = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
            self.driver.swipe( 500, 1000, 500, 400 )
            # 输入发货方联系电话
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/seller_contact" ).send_keys( sellerContact )
            # 输入提货城市
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/tv_start_city" ).send_keys( startCity )
            # 输入提货地址
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/from_where" ).send_keys( fromWhere )

            '''到货信息'''
            # 将页面向上滑动
            # els = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
            self.driver.swipe( 500, 1000, 500, 400 )
            # 输入收货方
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/buyer" ).send_keys( buyer )
            # 输入收货方联系电话
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/buyer_contact" ).send_keys( buyerContact )
            # 输入收货城市
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/tv_end_city" ).send_keys( endCity )
            # 输入收货地址
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/to_where" ).send_keys( toWhere )

            # 完成
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/submit" ).click()
            sleep( 3 )

            # 输入调度单号
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/schedule_no" ).send_keys( scheduleNo )
            # 输入车牌号
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/truck_no" ).send_keys( truckNo )
            # 输入司机手机
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/et_driver_mobile" ).send_keys( driverContact )
            # 输入司机姓名
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/name" ).send_keys( driverName )
            #完成
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/submit" ).click()


        except Exception as e:
            print( "失败了呢" )
            print( e )

    def tearDown(self):
        self.driver.quit( )


if __name__ == '__main__':
    unittest.main( )
