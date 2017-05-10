from time import sleep


def logout(self):
    # 点击我的
    self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/bottom_navigation_container" )[3].click( )
    # 点击设置按钮
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_set" ).click( )
    # 滑动
    # self.driver.swipe(500,1000,500,400)
    e1 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_pwd" )
    e2 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/rl_image" )
    self.driver.scroll( e1, e2 )
    sleep( 2 )
    # 点击退出
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_exit" ).click( )
    # 确定
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/ok" ).click( )
    sleep( 3 )
    # 切换用户
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_back" ).click( )
