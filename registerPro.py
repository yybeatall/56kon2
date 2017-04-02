# encoding:utf-8
# 综合测试--注册
import unittest
from time import sleep

from appium import webdriver
from ddt import ddt, data, unpack

from method import commonMethod
from method import setParam


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        setParam.setParam(self)

    mobile = commonMethod.mobileNo("139")

    @data((mobile, "123456"))
    @unpack
    def testRegister(self, username, password):
        try:

            global exist
            sleep(3)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/reg_user").click()
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/agreement").click()
            sleep(3)
            # 服务协议截屏
            self.driver.get_screenshot_as_file("agreement.png")
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            # 注册
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/mobile_number").send_keys(username)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/get_checkcode").click()
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_password").send_keys(password)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/register").click()
            sleep(3)

        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
