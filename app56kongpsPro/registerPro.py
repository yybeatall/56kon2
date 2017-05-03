# encoding:utf-8
# 足迹版测试--注册
import unittest
from time import sleep

from ddt import ddt, data, unpack

from method import commonMethod
from method import setParam56kongps


@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setParam56kongps.setParam( self )

    mobile = commonMethod.mobileNo("139")
    name = mobile[-4:]+"姓名"

    @data((mobile, "123456",name))
    @unpack
    def testRegister(self, username, password,name):
        try:

            global exist
            sleep(3)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/tv_reg").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/agreement").click()
            sleep(3)
            # 服务协议截屏
            self.driver.get_screenshot_as_file("agreement.png")
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            # 注册
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_mobile").send_keys(username)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_code").click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_pwd").send_keys(password)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_reg").click()
            sleep(3)

            self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_nickname").send_keys(name)
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_icon").click()

            #拍照
            #self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_one").click()

            #从相册中选择
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_two").click()
            self.driver.find_elements_by_id("com.yihu001.kon.driver:id/picture_image")[0].click()
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/check").click()
            sleep(3)

            #完成
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/bt_complete").click()
            print(username)


        except Exception as e:
            print(e)

    def tearDown(self):
        print( "足迹版测试--注册" )
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
