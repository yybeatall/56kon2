#共享货跟
def shareToContacts(self):
    #联系人
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_one" ).click( )
    self.driver.find_element_by_xpath(
        '//android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget'
        '.RelativeLayout[contains(@index,0)]' ).click( )
    self.driver.find_element_by_xpath(
        '//android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.widget'
        '.RelativeLayout[contains(@index,1)]' ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )

def shareToGroup(self):
    # 分组
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_two" ).click( )
    self.driver.find_element_by_xpath(
        '//android.widget.RelativeLayout[contains(@index,0)]' ).click( )
    self.driver.find_element_by_xpath(
        '//android.widget.RelativeLayout[contains(@index,1)]' ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )

def shareToPhone(self):
    sharephone = "13800000000"
    # 手机号码
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_three" ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/et_phone" ).send_keys( sharephone )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_menu" ).click( )

def shareToAddrList(self):
    # 通讯录
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_four" ).click( )
    # 需要真机
    self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )

def cancle(self):
    # 取消
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_cancel" ).click( )