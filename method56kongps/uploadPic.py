from time import sleep


def uploadPicFirst(self):
    i = 0
    list = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_add_pic_b" )
    count = len(list)
    if count > 0:
        self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_add_pic_b" )[0].click( )
        cancel( self )
        while (i < count):
            self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_add_pic_b" )[0].click( )
            i = i + 1
            uploadPic( self )
    else:
        uploadpicAgain(self,3)


def uploadpicAgain(self,n):
    i = 0
    self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_add_pic_s" )[0].click( )
    cancel( self )
    while (i < n):
        self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/iv_add_pic_s" )[0].click( )
        i = i + 1
        uploadPic( self )


def uploadPic(self):
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_two" ).click( )
    self.driver.find_element_by_xpath( '//android.support.v7.widget.RecyclerView/'
                                       'android.widget.RelativeLayout[contains(@index,0)]' ).click( )
    self.driver.find_element_by_xpath( '//android.support.v7.widget.RecyclerView/'
                                       'android.widget.RelativeLayout[contains(@index,1)]' ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )
    # 继续添加
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/add" ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_two" ).click( )
    self.driver.find_element_by_xpath( '//android.support.v7.widget.RecyclerView/'
                                       'android.widget.RelativeLayout[contains(@index,0)]' ).click( )
    self.driver.find_element_by_xpath( '//android.support.v7.widget.RecyclerView/'
                                       'android.widget.RelativeLayout[contains(@index,1)]' ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_ok" ).click( )
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_upload" ).click( )
    sleep( 6 )
    self.driver.find_element_by_class_name("android.widget.ImageButton").click()

#def uploadTake(self):
    # 拍照
    # self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_one").click()
    # 真机测试

def cancel(self):
    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/btn_cancel" ).click( )
