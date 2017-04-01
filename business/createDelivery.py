from time import sleep

def createDelivery(self):
    sendUser = "13800000000"
    memo = "自动测试发送备注"

    self.driver.find_element_by_id("com.yihu001.kon.manager:id/et_phone").send_keys(sendUser)
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/memo").send_keys(memo)
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_menu").click()
    sleep(3)