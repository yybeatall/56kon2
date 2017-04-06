import time
from time import sleep

def createschedule(self):

    scheduleNo = time.strftime('%Y%m%d%X' ,time.localtime())
    truckNo = "辽A12345"
    driverContact = "13900001127"
    driverName = "1127"
    memo = "自动测试调度备注"

    # 输入调度单号
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/schedule_no").send_keys(scheduleNo)
    # 输入车牌号
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/truck_no").send_keys(truckNo)
    # 输入司机手机
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/tv_enterprise_type").send_keys(driverContact)
    # 输入司机姓名
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/name").send_keys(driverName)
    # 备注信息
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/memo").send_keys(memo)

    # 完成
    self.driver.find_element_by_id("com.yihu001.kon.manager:id/submit").click()
    sleep(2)