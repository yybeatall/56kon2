#usr/bin/python
#encoding:utf-8
#综合版测试--创建任务并调度
import unittest
from time import sleep
import time

from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        #天天模拟器
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '127.0.0.1:6555'
        desired_caps['appPackage'] = 'com.yihu001.kon.manager'
        desired_caps['appActivity'] = '.activity.HomeActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        #desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testCreateDispatchSch(self):
        taskorder = time.strftime('%Y%m%d%X',time.localtime())
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

        memo = "自动测试"

        scheduleNo = time.strftime('%Y%m%d%X',time.localtime())
        truckNo = "辽A12345"
        driverContact = "13900001127"
        driverName = "1127"


        try:
            sleep(3)
            # 点击首页业务
            self.driver.find_elements_by_id("com.yihu001.kon.manager:id/bottom_navigation_container")[1].click()
            # 点击切换企业
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_select_enterprise").click()
            sleep(1)
            # 选择企业
            self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "一二三四五六七八九十一二三四五六七八九十")]').click()
            sleep(2)

            '''创建任务'''

            # 点击创建任务
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_create_task").click()
            '''基本信息'''
            # 输入任务编号
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/task_order").send_keys(taskorder)
            # 输入货物名称
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_goods_name").send_keys(goodsName)
            # 输入货物数量
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/goods_quantity").send_keys(goodsCount)
            # 输入货物重量
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/goods_weight").send_keys(goodsWeight)
            # 输入货物体积
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/goods_volume").send_keys(goodsVolume)

            '''提货信息'''
            # 输入发货方
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/seller").send_keys(seller)
            # 将页面向上滑动
            #els = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
            self.driver.swipe(500,1000,500,400)
            # 输入发货方联系电话
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/seller_contact").send_keys(sellerContact)
            # 输入提货城市
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_start_city").send_keys(startCity)
            # 输入提货地址
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/from_where").send_keys(fromWhere)

            '''到货信息'''
            # 将页面向上滑动
            #els = self.driver.find_elements_by_class_name("android.widget.RelativeLayout")
            self.driver.swipe(500,1000,500,400)
            # 输入收货方
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/buyer").send_keys(buyer)
            # 输入收货方联系电话
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/buyer_contact").send_keys(buyerContact)
            # 输入收货城市
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_end_city").send_keys(endCity)
            # 输入收货地址
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/to_where").send_keys(toWhere)

            '''备注信息'''
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/memo").send_keys(memo)

            #完成
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/submit").click()

            #创建后直接调度
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/take_two").click()
            sleep(2)

            '''创建调度'''
            # 输入调度单号
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/schedule_no").send_keys(scheduleNo)
            # 输入车牌号
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/truck_no").send_keys(truckNo)
            # 输入司机手机
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_enterprise_type").send_keys(driverContact)
            # 输入司机姓名
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/name").send_keys(driverName)
            #备注信息
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/memo").send_keys(memo)

            #完成
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/submit").click()
            sleep(2)

        except Exception as e:
            print("失败了呢")
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
