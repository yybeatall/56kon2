#执行定检
from method import commonMethod

def node(self):
    list = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_execute" )
    count = len( list )
    if count > 0:
        i = 0
        while (i < count):
            self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_execute" )[0].click( )
            if commonMethod.isElement( self, "id", "com.yihu001.kon.driver:id/tv_execute" ):
                if self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).text == "跳过":
                    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).click( )
                    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/content" ).send_keys( "自动测试跳过" )
                    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/toolbar_right" ).click( )
                else:
                    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).click( )

            elif commonMethod.isElement( self, "id", "com.yihu001.kon.driver:id/handover" ):
                self.driver.find_element_by_id( "com.yihu001.kon.driver:id/handover" ).click( )

            else:
                # 需要扫码交接的暂不处理
                self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_back" ).click( )
                self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )
                break
            i = i + 1
    else:
        e1 = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_upload" )[1]
        e2 = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_upload" )[0]
        self.driver.scroll( e1, e2 )
        list = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_execute" )
        if count > 0:
            i = 0
            while (i < count):
                self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_execute" )[0].click( )
                if commonMethod.isElement( self, "id", "com.yihu001.kon.driver:id/tv_execute" ):
                    if self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).text == "跳过":
                        self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).click( )
                        self.driver.find_element_by_id( "com.yihu001.kon.driver:id/content" ).send_keys(
                            "自动测试跳过" )
                        self.driver.find_element_by_id( "com.yihu001.kon.driver:id/toolbar_right" ).click( )
                    else:
                        self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).click( )

                elif commonMethod.isElement( self, "id", "com.yihu001.kon.driver:id/handover" ):
                    self.driver.find_element_by_id( "com.yihu001.kon.driver:id/handover" ).click( )
                i = i + 1
        else:
            self.driver.find_element_by_class_name( "android.widget.ImageButton" ).click( )