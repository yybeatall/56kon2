from time import sleep

from method import commonMethod
from method import setParam56kongps
from method56kongps import share
def trackInfo(self):
    #数据切换
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_type").click()
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_net").click()
    #刷新
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_refresh").click()
    sleep(3)
    #menu
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/fab_expand_menu_button").click()
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/fab_detail").click()
    #截图
    self.driver.get_screenshot_as_file(setParam56kongps.screenCapturePath+"trackdetail.png")
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/ll_root").click()
    # menu
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_expand_menu_button" ).click( )
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/fab_location").click()
    if commonMethod.isElement(self,"id","com.yihu001.kon.driver:id/iv_cancel"):
        #截图
        self.driver.get_screenshot_as_file(setParam56kongps.screenCapturePath+"tracklocation.png")
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_cancel").click()
    # menu
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_expand_menu_button" ).click( )
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/fab_timeline").click()
    #截图
    self.driver.get_screenshot_as_file(setParam56kongps.screenCapturePath+"tracktimeline.png")
    self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_close").click()
    # menu
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_expand_menu_button" ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_share" ).click( )

    #通讯录
    share.shareToContacts(self)

    # menu
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_expand_menu_button" ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_share" ).click( )

    #分组
    share.shareToGroup(self)

    # menu
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_expand_menu_button" ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_share" ).click( )

    #联系人
    share.shareToPhone(self)

    # menu
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_expand_menu_button" ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_share" ).click( )

    #通讯录
    share.shareToAddrList(self)

    # menu
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_expand_menu_button" ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/fab_share" ).click( )

    #取消
    share.cancle(self)

    # 退出地图页
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_close" ).click( )