from time import sleep

def changeBusiness(self):

    sleep(3)
    # 点击首页业务
    self.driver.find_elements_by_id("com.yihu001.kon.manager:id/bottom_navigation_container")[1].click()
    # 点击切换企业
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_select_enterprise").click()
    sleep(1)
    # 选择企业
    self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "一二三四五六七八九十一二三四五六七八九十")]').click()
    sleep(2)
