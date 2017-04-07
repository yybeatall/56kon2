from time import sleep


def taskInfo(self, status):

    #任务详情
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/more_layout" ).click( )

    e1 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/package_material_key" )
    e2 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/task_no_key" )
    self.driver.drag_and_drop( e1, e2 )

    e1 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/goods_quantity_key" )
    e2 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/package_type_key" )
    self.driver.drag_and_drop( e1, e2 )

    # 提货地址地图页
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/pickup_addr_image" ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( "pickupaddr.png" )
    # 返回
    self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )
    # 联系人信息
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/pickup_icon" ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( "contactsInfo.png" )
    # 返回
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_back" ).click( )

    e1 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/pickup_time_key" )
    e2 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/goods_quantity_key" )
    self.driver.drag_and_drop( e1, e2 )

    # 执行交接
    if status == "pickup":
        self.driver.find_element_by_xpath( '//android.widget.TextView[contains(@text,"执行交接")]' )

    # 到货地址地图页
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/delivery_addr_image" ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( "deliveryaddr.png" )
    # 返回
    self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )

    # 联系人信息
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/delivery_icon" ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( "contactsInfo2.png" )
    # 返回
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_back" ).click( )

    '''调度详情'''
    self.driver.find_element_by_xpath( '//android.widget.TextView[@text="调度"]' ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( "dispatchInfo.png" )

    '''照片详情'''
    self.driver.find_element_by_xpath( '//android.widget.TextView[@text="照片"]' ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( "photoInfo.png" )

    '''定检详情'''
    self.driver.find_element_by_xpath( '//android.widget.TextView[@text="定检"]' ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( "checkInfo.png" )

    #返回
    self.driver.find_element_by_id("android.widget.ImageButton").click()
