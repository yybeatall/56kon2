# usr/bin/python
# encoding:utf-8
# 综合版测试--货物档案
import unittest
import random
from time import sleep
from method import setParam56kon
from method56kon import changeBusiness


class MyTestCase( unittest.TestCase ):
    def setUp(self):
        self.driver = setParam56kon.setParam( self )

    def testGoods(self):
        goodsName = "每日货物"+str(random.randint(0, 9))+str(random.randint(0, 9))
        goodsModel = "YYYY"
        batch="001-111"
        manufacturer="丫丫工厂"
        manufactureradd="丫丫工厂地址"
        memo="自动测试备注"
        FindgoodsName = "每日货物"

        try:
            sleep(3)
            #切换企业
            changeBusiness.changeBusiness(self)

            #选择货物
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_goods").click()
            sleep(2)
            '''添加货物'''
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
            self.driver.find_element_by_class_name("android.widget.RelativeLayout").click()
            #包装类型
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/ll_package_type").click()
            self.driver.get_screenshot_as_file("packagetype.png")
            self.driver.find_element_by_class_name("android.widget.RelativeLayout").click()
            #包装材料
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/ll_package_material").click()
            self.driver.get_screenshot_as_file("packagematerial.png")
            self.driver.find_element_by_class_name("android.widget.RelativeLayout").click()
            #防护要求
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_protection").click()
            e1 = self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_protection")
            e2 = self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_goods_name")
            self.driver.scroll(e1, e2)
            self.driver.get_screenshot_as_file("protection.png")
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/rl_protection").click()
            #加载更多
            self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"更多货物信息")]').click()
            #
            e1 = self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_batch")
            e2 = self.driver.find_element_by_id("com.yihu001.kon.manager:id/ll_goods_type")
            self.driver.scroll(e1, e2)
            #
            self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"补充信息")]')
            #生产批次
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_batch").send_keys(batch)
            #
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_manufacturer").send_keys(manufacturer)
            #
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_manufacturer_address").send_keys(manufactureradd)
            #
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_memo").send_keys(memo)
            #完成
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/submit").click()
            '''菜单'''
            #显示菜单
            self.driver.find_element_by_class_name("android.widget.RelativeLayout").click()
            #货物信息
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_detail").click()
            sleep(2)
            self.driver.get_screenshot_as_file("goodsdetail.png")
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            #编辑货物
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_edit").click()
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/submit").click()
            #显示菜单
            self.driver.find_element_by_class_name("android.widget.RelativeLayout").click()
            #撤销核准
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_approve").click()
            #t通过核准
            self.driver.find_element_by_id( "com.yihu001.kon.manager:id/tv_approve" ).click( )
            #删除货物
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_delete").click()
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/btn_ok").click()
            #搜索
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/search").click()
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_goods_name").send_keys(FindgoodsName)
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/submit").click()
            #查询条件
            self.driver.find_element_by_id("com.yihu001.kon.manager:id/ll_option").click()
            sleep(1)
            #截图
            self.driver.get_screenshot_as_file("result.png")

        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit( )

if __name__ == '__main__':
    unittest.main( )














