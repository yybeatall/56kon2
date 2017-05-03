# encoding:utf-8
# 足迹测试--忘记密码
import unittest
from time import sleep

from ddt import ddt, data, unpack

from method import setParam56kongps


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam( self )


    @data(("13900000417", "111111"))
    @unpack
    def testRegister(self, username, password):
        try:

            global exist
            sleep(3)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_forget_pwd").click()

            sleep(3)

            # 忘记密码
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_mobile").send_keys(username)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_code").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_pwd").send_keys(password)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_reg").click()
            sleep(3)

            #重新登录
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_pwd").send_keys(password)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").click()

        except Exception as e:
            print("足迹测试--忘记密码")
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
