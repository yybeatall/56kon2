#usr/bin/python
#encoding:utf-8
#足迹版测试--登录
import unittest
from method import location
from time import sleep

from appium import webdriver
from ddt import ddt, data, unpack
from method import commonMethod
from method56kongps import logout

@ddt
class MyTestCase(unittest.TestCase):
    u"""登陆失败测试"""
    def setUp(self):
        #天天模拟器
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # 天天模拟器
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '127.0.0.1:6555'
        #小米真机
        # desired_caps['platformVersion'] = '5.1.1'
        # desired_caps['deviceName'] = 'd727fe13'
        desired_caps['appPackage'] = 'com.yihu001.kon.driver'
        desired_caps['appActivity'] = '.ui.activity.MainActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        #desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(*location.getDdtExcel('test.xlsx'))
    # @data(("13900000217","123456",False),#用户不存在
    #       ("13900001127","12345",False),#密码错误
    #       ("1390000112","123456",False),#手机位数不对
    #       ("13900001127","123456",True)#正常输入
    #       )

    @unpack
    def testLogIn(self, username, password, expectedresult):
        u"""登陆失败测试"""
        global exist
        if not commonMethod.isElement( self, "id", "com.yihu001.kon.driver:id/tv_reg" ):
            # 判断是否登录，如果已登录需注销
            logout.logout( self )
            sleep( 2 )
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_name").send_keys(username)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_pwd").send_keys(password)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").click()

        sleep(3)
        # try:
        #     if self.driver.find_element_by_link_text(toastmessage).is_displayed():
        #         toastexist = True
        # except Exception as e:
        #     toastexist = False
        try:
            if self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").is_displayed():
                exist = 'False'
        except Exception as e:
            exist = 'True'

        self.assertEqual(exist,expectedresult)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
