
def pickup(self):

    # 点击上传照片
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_picture" ).click( )
    # 点击车况
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_one" ).click( )
    # 点击确定
    self.driver.find_element_by_id( "android:id/button3" ).click( )
    # 点击确认提货
    self.driver.find_element_by_xpath( '//android.widget.Button[contains(@text, "确认提货")]' ).click( )
    # 点击取消
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_cancel" ).click( )
    # 再次点击确认提货
    self.driver.find_element_by_xpath( '//android.widget.Button[contains(@text, "确认提货")]' ).click( )
    # 点击确定
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )

def delivery(self):

    # 点击上传照片
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_picture" ).click( )
    # 点击回单
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_four" ).click( )
    # 点击确定
    self.driver.find_element_by_id( "android:id/button3" ).click( )
    # 点击确认到货
    self.driver.find_element_by_xpath( '//android.widget.Button[contains(@text, "确认到货")]' ).click( )
    # 点击取消
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_cancel" ).click( )
    # 再次点击确认到货
    self.driver.find_element_by_xpath( '//android.widget.Button[contains(@text, "确认到货")]' ).click( )
    # 点击确定
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )