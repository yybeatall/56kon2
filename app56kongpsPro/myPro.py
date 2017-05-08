# usr/bin/python
# encoding:utf-8
# 足迹版测试--我的页面，应用设置，修改个人信息，二维码，更换头像，财富中心，车牌记录
import unittest
from time import sleep

from ddt import ddt, data, unpack

from method56kongps import pickupDelivery
from method import setParam56kongps
from method import commonMethod
from method56kongps import taskInfo
from method56kongps import trackInfo
from method56kongps import uploadPic
from method56kongps import share

@ddt
class MyTestCase(unittest.TestCase):
    u"""我的页面-测试流程"""
    
    def setUp(self):
        self.driver = setParam56kongps.setParam(self)   

    '''设置'''
    def testSet(self):
        u"""我的页面-设置流程测试"""
        # TODO：混合模式待调整
        oldPwd = "111111"
        newPwd = "111111"
        username = "13900000417"
        password = "111111"
        try:
            sleep(5)
            print( self.driver.contexts )
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"et_name" ).send_keys( username )
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"et_pwd" ).send_keys( password )
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"btn_sign" ).click( )

            sleep(3)

            #我的
            list = self.driver.find_elements_by_id( 'bottom_navigation_container')
            lens = len(list)
            print(lens)
            list[3].click()

            #进入设置页
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"btn_set").click()

            #地图模式
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"sc_lock").click()
            #语音设置
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"sc_voice").click()
            #缓存清理-图像文件
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"rl_image").click()
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"btn_ok").click()
            sleep(2)
            #缓存清理-轨迹数据
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"rl_track").click()
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"btn_ok").click()
            sleep(2)
            #修改密码
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"tv_pwd").click()
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"et_old").send_keys(oldPwd)
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"et_new" ).send_keys(newPwd)
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"tv_menu").click()
            sleep( 2 )
            #关于我们
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"tv_about").click()
            #应用介绍
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"tv_about").click()
            sleep(3)
            #截图
            self.driver.get_screenshot_as_file("about.png")
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            #帮助中心
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"tv_help").click()
            self.driver.switch_to.context( 'WEBVIEW_0' )
            self.driver.find_element_by_xpath("/html/body/div/a/div").click()
            self.driver.find_element_by_xpath('/html/body/div/ul/li[1]/a/span').click()
            self.driver.get_screenshot_as_file("help-q.png")
            #返回键
            self.driver.keyevent(4)

            #司机
            self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/a/i').click()
            #交接-列表模式
            self.driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[1]').click()
            self.driver.get_screenshot_as_file( "help-h1.png" )
            #返回键
            self.driver.keyevent(4)
            #交接-地图模式
            self.driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[2]').click()
            self.driver.get_screenshot_as_file( "help-h2.png" )
            #返回键
            self.driver.keyevent(4)
            #扫码交接
            self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[1]').click()
            self.driver.get_screenshot_as_file( "help-h3.png" )
            #返回键
            self.driver.keyevent(4)
            #上传照片
            self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]').click()
            self.driver.get_screenshot_as_file( "help-p.png" )
            #返回键
            self.driver.keyevent(4)
            #执行定检
            self.driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[1]').click()
            self.driver.get_screenshot_as_file( "help-n.png" )
            #返回键
            self.driver.keyevent(4)
            #秀足迹
            self.driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]').click()
            self.driver.get_screenshot_as_file( "help-s.png" )
            #返回键
            self.driver.keyevent(4)
            #竞价
            self.driver.find_element_by_xpath('/html/body/div/div[3]/div[4]/div').click()
            self.driver.get_screenshot_as_file( "help-q.png" )
            #返回键
            self.driver.keyevent(4)
            #返回键
            self.driver.keyevent(4)

            #账号
            self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a/i').click()
            #注册
            self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]').click()
            self.driver.get_screenshot_as_file( "help-r.png" )
            #返回键
            self.driver.keyevent(4)
            #忘记密码
            self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]').click()
            self.driver.get_screenshot_as_file( "help-f.png" )
            #返回键
            self.driver.keyevent(4)
            #我的二维码---获取不到位置
            # self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]').click()
            # self.driver.get_screenshot_as_file( "help-m.png" )
            # #返回键
            # self.driver.keyevent(4)
            #返回键
            self.driver.keyevent(4)

            #其他
            self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/a/i').click()
            #添加联系人
            self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div').click()
            self.driver.get_screenshot_as_file( "help-c.png" )
            #返回键
            self.driver.keyevent(4)
            #返回键
            self.driver.keyevent(4)
            #返回键
            self.driver.keyevent(4)

            self.driver.switch_to.context('NATIVE_APP')
            print( self.driver.contexts )
            #版本更新
            self.driver.find_element_by_xpath( '//android.widget.TextView[@text="版本更新"]' ).click( )
            #联系我们
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"tv_contact" ).click( )
            self.driver.get_screenshot_as_file( "contactus.png" )

        except Exception as e:
            print(e)

    '''个人信息修改以及财富中心'''
    def testPersonalInfo(self):
        u"""我的页面-个人信息修改以及财富中心"""
        # TODO：混合模式待调整
        try:
            self.driver.find_elements_by_id( setParam56kongps.appPackageName+"bottom_navigation_container" )[3].click( )
            #编辑个人信息
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"btn_edit").click()
            #个人二维码
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"btn_qrcode" ).click( )
            #修改头像
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"iv_icon" ).click( )
            #完善个人信息
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"rl_name" ).click( )
            #财富中心
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"iv_action_bg").click()

        except Exception as e:
            print(e)

    '''通讯录'''
    def testAddrList(self):
        u"""我的页面-通讯录操作流程测试"""
        # TODO：未完成
        try:
            self.driver.find_elements_by_id( setParam56kongps.appPackageName+"bottom_navigation_container" )[3].click( )
            #联系人
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"rl_contacts").click()
            #好友
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"rl_friends" ).click( )
            #分组
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"rl_groups" ).click( )
            #邀请成功
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"rl_invite_success" ).click( )
            #通讯录
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"rl_contact" ).click( )

        except Exception as e:
            print(e)

    @data("辽A12345","沪B111111","沪BB11111","沪AAAAAAA")
    def testPlateRecordAdd(self,plateNo):
        u"""我的页面-添加车牌记录流程"""
        try:
            '''进入我的页面'''
            self.driver.find_elements_by_id( setParam56kongps.appPackageName+"bottom_navigation_container" )[3].click( )

            e1 = self.driver.find_element_by_id(setParam56kongps.appPackageName+"state_layout")
            e2 = self.driver.find_element_by_id(setParam56kongps.appPackageName+"contact_layout")
            self.driver.drag_and_drop(e1,e2)

            '''点击车牌记录'''
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"rl_plate").click()
            #截图--无记录页的显示
            self.driver.get_screenshot_as_file("plate.png")

            #添加车牌
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"add").click()
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"et_plate").send_keys(plateNo)
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"tv_menu").click()


        except Exception as e:
            print(e)

    def testPlateRecordEdit(self):
        u"""我的页面-编辑车牌记录流程"""
        try:
            '''进入我的页面'''
            self.driver.find_elements_by_id( setParam56kongps.appPackageName+"bottom_navigation_container" )[3].click( )

            e1 = self.driver.find_element_by_id(setParam56kongps.appPackageName+"state_layout")
            e2 = self.driver.find_element_by_id(setParam56kongps.appPackageName+"contact_layout")
            self.driver.drag_and_drop(e1,e2)

            '''点击车牌记录'''
            self.driver.find_element_by_id(setParam56kongps.appPackageName+"rl_plate").click()

            '''编辑车牌'''
            self.driver.find_elements_by_id( setParam56kongps.appPackageName+"iv_edit" )[0].click( )
            self.driver.find_element_by_id( setParam56kongps.appPackageName+"tv_menu" ).click( )

            '''删除车牌'''
            self.driver.find_elements_by_id( setParam56kongps.appPackageName+"iv_delete" )[0].click( )

            '''设置默认车牌'''
            self.driver.find_elements_by_class_name( "android.widget.RelativeLayout" )[0].click( )

        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
