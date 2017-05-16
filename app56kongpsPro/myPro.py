# usr/bin/python
# encoding:utf-8
# 足迹版测试--我的页面，应用设置，修改个人信息，二维码，更换头像，财富中心，车牌记录
import unittest
from time import sleep
import time

from ddt import ddt, data, unpack

from method import setParam56kongps
from method import commonMethod
from method56kongps import contacts

shotPath = setParam56kongps.screenCapturePath + "我的页面-测试流程/"+setParam56kongps.now
appPackageNameForS = ''
oldPwd = "111111"
newPwd = "111111"
username = "13900000417"
password = "111111"
name = "姓名"+time.strftime('%d%X' ,time.localtime())
nickName = "昵称"+time.strftime('%d%X' ,time.localtime())
nameN = "姓名新"+time.strftime('%d%X' ,time.localtime())
nickNameN = "昵称新"+time.strftime('%d%X' ,time.localtime())
search = "yuyang"
memoName = "于洋备注"
sendMess = "聊个天吧"
addPhone = commonMethod.mobileNo("138")

@ddt
class MyTestCase(unittest.TestCase):
    u"""我的页面-测试流程"""
    
    def setUp(self):
        self.driver = setParam56kongps.setParam(self,"S")

    '''设置'''
    # def testSet(self):
    #     u"""我的页面-设置流程测试"""
    #     # TODO：混合模式待调整
    #     try:
    #         sleep(5)
    #         #print (self.driver.current_context)
    #         # self.driver.find_element_by_id( setParam56kongps.appPackageName+"et_name" ).send_keys( username )
    #         # self.driver.find_element_by_id( setParam56kongps.appPackageName+"et_pwd" ).send_keys( password )
    #         # self.driver.find_element_by_id( setParam56kongps.appPackageName+"btn_sign" ).click( )
    #
    #         sleep(3)
    #
    #         #我的
    #         list = self.driver.find_elements_by_id("bottom_navigation_container")
    #         lens = len(list)
    #         print(lens)
    #         list[3].click()
    #
    #         #进入设置页
    #         self.driver.find_element_by_id(appPackageNameForS+"btn_set").click()
    #
    #         #地图模式
    #         self.driver.find_element_by_id(appPackageNameForS+"sc_lock").click()
    #         #语音设置
    #         self.driver.find_element_by_id(appPackageNameForS+"sc_voice").click()
    #         #缓存清理-图像文件
    #         self.driver.find_element_by_id(appPackageNameForS+"rl_image").click()
    #         self.driver.find_element_by_id(appPackageNameForS+"btn_ok").click()
    #         sleep(2)
    #         #缓存清理-轨迹数据
    #         self.driver.find_element_by_id(appPackageNameForS+"rl_track").click()
    #         self.driver.find_element_by_id(appPackageNameForS+"btn_ok").click()
    #         sleep(2)
    #         #修改密码
    #         self.driver.find_element_by_id(appPackageNameForS+"tv_pwd").click()
    #         self.driver.find_element_by_id(appPackageNameForS+"et_old").send_keys(oldPwd)
    #         self.driver.find_element_by_id( appPackageNameForS+"et_new" ).send_keys(newPwd)
    #         self.driver.find_element_by_id(appPackageNameForS+"tv_menu").click()
    #         sleep( 2 )
    #         #关于我们
    #         self.driver.find_element_by_id(appPackageNameForS+"tv_about").click()
    #         #应用介绍
    #         self.driver.find_element_by_id(appPackageNameForS+"tv_about").click()
    #         sleep(1)
    #         #截图
    #         self.driver.get_screenshot_as_file(shotPath+"about.png")
    #         sleep( 1 )
    #         self.driver.find_element_by_class_name("android.widget.ImageButton").click()
    #
    #         #帮助中心
    #         self.driver.find_element_by_id(appPackageNameForS+"tv_help").click()
    #         self.driver.switch_to.context( 'WEBVIEW_0' )
    #         self.driver.find_element_by_xpath("/html/body/div/a/div").click()
    #         self.driver.find_element_by_xpath('/html/body/div/ul/li[1]/a/span').click()
    #         self.driver.get_screenshot_as_file(shotPath+"help-q.png")
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #
    #         #司机
    #         self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/a/i').click()
    #         #交接-列表模式
    #         self.driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[1]').click()
    #         sleep( 1 )
    #         self.driver.get_screenshot_as_file( shotPath+"help-h1.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #交接-地图模式
    #         self.driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[2]').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-h2.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #扫码交接
    #         self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[1]').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-h3.png" )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #上传照片
    #         self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-p.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #执行定检
    #         self.driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[1]').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-n.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #秀足迹
    #         self.driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[2]').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-s.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #竞价
    #         self.driver.find_element_by_xpath('/html/body/div/div[3]/div[4]/div').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-q.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #返回键
    #         self.driver.keyevent(4)
    #
    #         #账号
    #         self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/a/i').click()
    #         #注册
    #         self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-r.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #忘记密码
    #         self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-f.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #我的二维码---获取不到位置
    #         # self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]').click()
    #         # self.driver.get_screenshot_as_file( "help-m.png" )
    #         # #返回键
    #         # self.driver.keyevent(4)
    #         #返回键
    #         self.driver.keyevent(4)
    #
    #         #其他
    #         self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/a/i').click()
    #         #添加联系人
    #         self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div').click()
    #         self.driver.get_screenshot_as_file( shotPath+"help-c.png" )
    #         sleep( 1 )
    #         #返回键
    #         self.driver.keyevent(4)
    #         #返回键
    #         self.driver.keyevent(4)
    #         #返回键
    #         self.driver.keyevent(4)
    #
    #         self.driver.switch_to.context('NATIVE_APP')
    #         #print( self.driver.current_context )
    #         #版本更新
    #         # TOdO:定位不到
    #         #self.driver.find_element_by_xpath( '//*[@id="root"]/div/div[3]/div/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr/td[2]' ).click( )
    #         #联系我们
    #         self.driver.find_element_by_id( appPackageNameForS+"tv_contact" ).click( )
    #         self.driver.get_screenshot_as_file( shotPath+"contactus.png" )
    #         sleep( 1 )
    #
    #     except Exception as e:
    #         print(e)

    '''个人信息修改以及财富中心'''
    # def testPersonalInfo(self):
    #     u"""我的页面-个人信息修改以及财富中心"""
    #     try:
    #         self.driver.find_elements_by_id( appPackageNameForS+"bottom_navigation_container" )[3].click( )
    #         #编辑个人信息
    #         self.driver.find_element_by_id(appPackageNameForS+"btn_edit").click()
    #         self.driver.find_element_by_id( appPackageNameForS + "et_real_name" ).clear()
    #         self.driver.find_element_by_id(appPackageNameForS+"et_real_name").send_keys(name)
    #         self.driver.find_element_by_id( appPackageNameForS + "et_nickname" ).clear()
    #         self.driver.find_element_by_id( appPackageNameForS+"et_nickname" ).send_keys( nickName )
    #         self.driver.find_element_by_id( appPackageNameForS+"tv_menu" ).click()
    #
    #         #个人二维码
    #         self.driver.find_element_by_id( appPackageNameForS+"btn_qrcode" ).click( )
    #         sleep(2)
    #         #截图
    #         self.driver.get_screenshot_as_file(shotPath+"qrcode.png")
    #         self.driver.find_element_by_class_name("android.widget.ImageButton").click()
    #
    #         #修改头像
    #         self.driver.find_element_by_id( appPackageNameForS+"iv_icon" ).click( )
    #         sleep(1)
    #         #查看
    #         self.driver.find_element_by_id(appPackageNameForS+"btn_one").click()
    #         sleep(2)
    #         self.driver.keyevent( 4 )
    #
    #         #修改头像
    #         self.driver.find_element_by_id( appPackageNameForS+"iv_icon" ).click( )
    #
    #         self.driver.find_element_by_id( appPackageNameForS+"btn_three" ).click( )
    #         sleep(1)
    #         self.driver.find_element_by_id(appPackageNameForS+"picture_image").click()
    #         self.driver.find_element_by_id(appPackageNameForS+"check").click()
    #         sleep(2)
    #
    #         #完善个人信息
    #         self.driver.find_element_by_id( appPackageNameForS+"rl_name" ).click( )
    #         self.driver.find_element_by_id( appPackageNameForS + "et_real_name" ).clear()
    #         self.driver.find_element_by_id(appPackageNameForS+"et_real_name").send_keys(nameN)
    #         self.driver.find_element_by_id( appPackageNameForS + "et_nickname" ).clear()
    #         self.driver.find_element_by_id( appPackageNameForS+"et_nickname" ).send_keys( nickNameN )
    #         self.driver.find_element_by_id( appPackageNameForS+"tv_menu" ).click( )
    #
    #         # #财富中心
    #         # self.driver.find_element_by_id(appPackageNameForS+"iv_action_bg").click()
    #         # self.driver.get_screenshot_as_file(shotPath+"action.png")
    #
    #     except Exception as e:
    #         print(e)

    '''通讯录'''
    def testAddrList(self):
        u"""我的页面-通讯录操作流程测试"""
        # TODO：未完成
        try:
            self.driver.find_elements_by_id( "bottom_navigation_container" )[3].click( )

            '''联系人'''
            self.driver.find_element_by_id(appPackageNameForS+"rl_contacts").click()
            sleep(1)
            self.driver.find_element_by_id(appPackageNameForS+"rl_search").click()
            self.driver.find_element_by_id(appPackageNameForS+"edit").send_keys(search)
            sleep(1)
            self.driver.find_element_by_id(appPackageNameForS+"root").click()

            #联系人信息页操作
            contacts.contacts(self,shotPath,memoName,sendMess,'S')

            #返回通讯录页
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            #查看联系人信息
            self.driver.find_element_by_id(appPackageNameForS+"root").click()
            # 联系人信息页操作
            contacts.contacts( self, shotPath, memoName, sendMess,'S')

            list = self.driver.find_element_by_id(appPackageNameForS+"tv_add")
            count = len(list)

            if count > 0:
                self.driver.find_elements_by_id(appPackageNameForS+"tv_add")[0].click()
                self.driver.find_element_by_id( appPackageNameForS+"tv_menu" ).click( )

            e1 = self.driver.find_element_by_id(appPackageNameForS+"phone_number")
            e2 = self.driver.find_element_by_id(appPackageNameForS+"user_icon")
            self.driver.drag_and_drop(e1,e2)

            #修改备注名
            self.driver.find_element_by_id(appPackageNameForS+"iv_edit").click()
            self.driver.find_element_by_id( appPackageNameForS + "et_name" ).clear()
            self.driver.find_element_by_id( appPackageNameForS+"et_name" ).send_keys( memoName )
            self.driver.find_element_by_id( appPackageNameForS+"tv_menu" ).click( )

            e1 = self.driver.find_element_by_id(appPackageNameForS+"phone_number")
            e2 = self.driver.find_element_by_id(appPackageNameForS+"user_icon")
            self.driver.drag_and_drop(e1,e2)

            #删除
            self.driver.find_element_by_id( appPackageNameForS+"iv_icon_2" ).click( )
            self.driver.find_element_by_id( appPackageNameForS+"btn_cancel" ).click( )

            self.driver.find_element_by_id(appPackageNameForS+"iv_delete").click()

            #切换好友
            self.driver.find_element_by_id(appPackageNameForS+"ll_friends").click()
            #切换分组
            self.driver.find_element_by_id(appPackageNameForS+"ll_groups").click()

            self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )

            '''好友'''
            self.driver.find_element_by_id( appPackageNameForS+"rl_friends" ).click( )
            self.driver.find_element_by_id(appPackageNameForS+"rl_search").click()
            self.driver.find_element_by_id(appPackageNameForS+"edit").send_keys(search)
            self.driver.find_element_by_id(appPackageNameForS+"root").click()

            #联系人信息页操作
            contacts.contacts(self,shotPath,memoName,sendMess,'S')

            self.driver.find_element_by_id(appPackageNameForS+"add_contact").click()
            self.driver.find_element_by_id(appPackageNameForS+"et_mobile").send_keys(addPhone)
            self.driver.find_element_by_id(appPackageNameForS+"btn_invite").click()

            #从通讯录中选择
            # TODO:真机
            #self.driver.find_element_by_id(appPackageNameForS+"tv_mobile").click()

            #返回通讯录页
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            '''分组'''
            self.driver.find_element_by_id( appPackageNameForS+"rl_groups" ).click( )
            self.driver.find_element_by_id(appPackageNameForS+"root").click()

            # 添加分组成员
            list = self.driver.find_elements_by_id(appPackageNameForS+"iv_user")
            count = len(list)
            if count > 1:
                self.driver.find_elements_by_id( appPackageNameForS+"iv_user" )[count-2].click( )

            self.driver.find_element_by_xpath(
                '//android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget'
                '.RelativeLayout[contains(@index,0)]' ).click( )
            self.driver.find_element_by_id( appPackageNameForS+"btn_ok" ).click( )

            # 移除分组成员
            list = self.driver.find_elements_by_id(appPackageNameForS+"iv_user")
            count = len(list)
            if count > 2:
                self.driver.find_elements_by_id( appPackageNameForS+"iv_user" )[count-1].click( )
                self.driver.find_element_by_id(appPackageNameForS+"iv_delete").click()
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            self.driver.find_element_by_id(appPackageNameForS+"btn_delete").click()
            self.driver.find_element_by_id(appPackageNameForS+"btn_cancel").click()

            self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )

            #左滑删除
            e1 = self.driver.find_element_by_id(appPackageNameForS+"tv_count")
            e2 = self.driver.find_element_by_id(appPackageNameForS+"tv_name")
            self.driver.drag_and_drop(e1,e2)

            self.driver.find_element_by_id(appPackageNameForS+"iv_delete").click()
            self.driver.find_element_by_id(appPackageNameForS+"btn_cancel").click()

            #返回通讯录页
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            #邀请成功
            self.driver.find_element_by_id( appPackageNameForS+"rl_invite_success" ).click( )

            #返回通讯录页
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()

            #通讯录
            self.driver.find_element_by_id( appPackageNameForS+"rl_contact" ).click( )


        except Exception as e:
            print(e)




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
