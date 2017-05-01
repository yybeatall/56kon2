#执行定检
from method import commonMethod

def node(self):
    list = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_execute" )
    count = len( list )
    if count > 0:
        nodeEx(self, count)
    else:
        e1 = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_upload" )[1]
        e2 = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_upload" )[0]
        self.driver.scroll( e1, e2 )
        list = self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_execute" )
        count = len(list)
        nodeEx(self,count)
    self.driver.find_element_by_class_name("android.widget.ImageButton").click()


def nodeEx(self,count):
    i = 0
    j = 0
    while (i < count):
        self.driver.find_elements_by_id( "com.yihu001.kon.driver:id/btn_execute" )[j].click( )
        if commonMethod.isElement( self, "id", "com.yihu001.kon.driver:id/tv_execute" ):
            if self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).text == "跳过":
                  self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).click( )
                  self.driver.find_element_by_id( "com.yihu001.kon.driver:id/content" ).send_keys( "自动测试跳过" )
                  self.driver.find_element_by_id( "com.yihu001.kon.driver:id/toolbar_right" ).click( )
            else:
                  self.driver.find_element_by_id( "com.yihu001.kon.driver:id/tv_execute" ).click( )

        elif commonMethod.isElement( self, "id", "com.yihu001.kon.driver:id/handover" ):
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/handover" ).click( )

        elif commonMethod.isElement(self,"id","com.yihu001.kon.driver:id/iv_back"):
            # 需要扫码交接的暂不处理
            self.driver.find_element_by_id( "com.yihu001.kon.driver:id/iv_back" ).click( )
            j = j + 1
        else:
            # 需要扫码交接的暂不处理
            self.driver.find_element_by_class_name("android.widget.ImageButton").click()
            j = j + 1
        i = i + 1