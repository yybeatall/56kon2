# usr/bin/python
# encoding:utf-8
# 综合版测试--添加企业好友
import unittest
from time import sleep
from method import setParam
from business import changeBusiness


class MyTestCase( unittest.TestCase ):
    def setUp(self):
        setParam.setParam(self)

    def testAddEnterpriseFriends(self):
        enterpriseNo = "test8"
        try:
            sleep(3)
            #切换企业
            changeBusiness.changeBusiness(self)

            #选择企业好友
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_archives").click()
            sleep(2)
            #滑动
            self.driver.swipe( 850, 310, 750, 310 )
            # 删除企业好友
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/iv_delete").click()
            # 点击确定
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/btn_ok").click()
            #点击添加企业好友
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/create").click()
            #输入搜索企业号
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_code").send_keys(enterpriseNo)
            #回车
            self.driver.keyevent(66)
            sleep(3)
            #点击添加好友
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/btn_add" ).click( )
            #返回
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/iv_back").click()

        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit( )


if __name__ == '__main__':
    unittest.main( )














