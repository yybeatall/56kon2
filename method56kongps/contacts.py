from method import commonMethod

def contacts(self,shotPath,memoName,sendMess,mode):
    if mode == "S":
        appPackageNameForS = ""
    else:
        appPackageNameForS = "com.yihu001.kon.driver:id/"

    # 联系人信息截图
    self.driver.get_screenshot_as_file( shotPath + "searchContacts.png" )
    self.driver.find_element_by_id( appPackageNameForS+"iv_user_icon_cover" ).click( )
    # 返回键
    self.driver.keyevent( 4 )
    # 修改备注名
    self.driver.find_element_by_id( appPackageNameForS+"iv_icon_1" ).click( )
    self.driver.find_element_by_id( appPackageNameForS + "et_name" ).clear()
    self.driver.find_element_by_id( appPackageNameForS+"et_name" ).send_keys( memoName )
    self.driver.find_element_by_id( appPackageNameForS+"tv_menu" ).click( )

    # 拨打
    # TODO:真机
    # self.driver.find_element_by_id( appPackageNameForS+"iv_icon_4" ).click( )

    # 删除
    self.driver.find_element_by_id( appPackageNameForS+"iv_icon_2" ).click( )
    self.driver.find_element_by_id( appPackageNameForS+"btn_cancel" ).click( )

    # 添加好友/对话
    # self.driver.find_element_by_id( appPackageNameForS+"iv_icon_3" ).click( )
    # TODO：待开发修改
    # if commonMethod.isElement(self,"id",appPackageNameForS+"tv_menu"):
    #     self.driver.find_element_by_id(appPackageNameForS+"tv_menu").click( )
    # else:
    #     self.driver.find_element_by_id( appPackageNameForS+"content" ).send_keys( sendMess )
    #     self.driver.find_element_by_id( appPackageNameForS+"send" ).click( )
    #     self.driver.find_element_by_id( appPackageNameForS+"send" ).click( )

    # 返回
    self.driver.find_element_by_id( appPackageNameForS+"iv_back" ).click( )