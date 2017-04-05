# usr/bin/python
# encoding:utf-8
# 综合版测试--货物档案
import unittest
from time import sleep
from method import setParam
from business import changeBusiness


class MyTestCase( unittest.TestCase ):
    def setUp(self):
        setParam.setParam(self)

    def testGoods(self):
        goodsName = "每日货物"
        goodsModel = "YYYY"
        batch="001-111"
        manufacturer="丫丫工厂"
        manufactureradd="丫丫工厂地址"
        memo="自动测试备注"




        try:
            sleep(3)
            #切换企业
            changeBusiness.changeBusiness(self)

            #选择货物
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_archives").click()
            sleep(2)
            #添加货物
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/create").click()
            #货物名称
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_goods_name").send_keys(goodsName)
            #
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_goods_model").send_keys(goodsModel)
            #货物类型
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/ll_goods_type").click()
            #规格型号
            self.driver.get_screenshot_as_file("goodstype.png")
            #选择
            self.driver.find_element_by_class("android.widget.RelativeLayout").click()
            #包装类型
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/ll_package_type").click()
            self.driver.get_screenshot_as_file("packagetype.png")
            self.driver.find_element_by_class("android.widget.RelativeLayout").click()
            #包装材料
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/ll_package_material").click()
            self.driver.get_screenshot_as_file("packagematerial.png")
            self.driver.find_element_by_class("android.widget.RelativeLayout").click()
            #防护要求
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_protection").click()
            e1 = self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_protection")
            e2 = self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_goods_name")
            self.driver.scroll(e1, e2)
            self.driver.get_screenshot_as_file("protection.png")
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_protection").click()
            #加载更多
            self.driver.find_element_by_class("android.widget.TextView").click()
            #
            e1 = self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_batch")
            e2 = self.driver.find_element_by_id("com.yihu001.kon.manager:id/ll_goods_type")
            self.driver.scroll(e1, e2)
            #
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_batch").senf_keys(batch)
            #
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_manufacturer").send_keys(manufacturer)
            #
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_manufacturer_address").send_keys(manufactureradd)
            #
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_memo").send_keys(memo)
            #完成
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/submit").click()






















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














