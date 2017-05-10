from time import sleep
from method import commonMethod
from method import setParam56kongps

shotPath = setParam56kongps.screenCapturePath + "任务详情/"+setParam56kongps.now

def taskInfo(self, status):

    #任务详情
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/ll_more" ).click( )

    e1 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_package_material_key" )
    e2 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_task_status_key" )
    self.driver.drag_and_drop( e1, e2 )

    e1 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_goods_quantity_key" )
    e2 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_package_type_key" )
    self.driver.drag_and_drop( e1, e2 )

    # 提货地址地图页
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_pickup_addr" ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( shotPath+'pickupaddr.png')
    # 返回
    self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )
    # 联系人信息
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_pickup" ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( shotPath+'contactsInfo.png')
    # 返回
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_back" ).click( )

    e1 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_pickup_time_key" )
    e2 = self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_goods_quantity_key" )
    self.driver.drag_and_drop( e1, e2 )

    # 执行交接
    if commonMethod.isElement(self,"xpath",'//android.widget.TextView[contains(@text,"执行交接")]') and status == "pickup":
        self.driver.find_element_by_xpath( '//android.widget.TextView[contains(@text,"执行交接")]' ).click()
        self.driver.find_element_by_id( "com.yihu001.kon.driver:id/handover" ).click( )

    # 到货地址地图页
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_delivery_addr" ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( shotPath+'deliveryaddr.png')
    # 返回
    self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )

    # 联系人信息
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_delivery" ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( shotPath+"contactsInfo2.png" )
    # 返回
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_back" ).click( )

    if commonMethod.isElement(self,"xpath",'//android.widget.TextView[contains(@text,"执行交接")]') and status == "delivery":
        self.driver.find_element_by_xpath( '//android.widget.TextView[contains(@text,"执行交接")]' ).click()
        self.driver.find_element_by_id( "com.yihu001.kon.driver:id/handover" ).click( )

    '''调度详情'''
    self.driver.find_element_by_xpath( '//android.widget.TextView[@text="调度"]' ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( shotPath+"dispatchInfo.png" )

    '''照片详情'''
    self.driver.find_element_by_xpath( '//android.widget.TextView[@text="照片"]' ).click( )
    sleep( 2 )
    # 截图
    self.driver.get_screenshot_as_file( shotPath+"photoInfo.png" )

    '''定检详情'''
    self.driver.find_element_by_xpath( '//android.widget.TextView[@text="定检"]' ).click( )
    # 截图
    self.driver.get_screenshot_as_file( shotPath+"checkInfo.png" )

    #返回
    self.driver.find_element_by_class_name("android.widget.ImageButton").click()
