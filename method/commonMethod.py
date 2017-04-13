import random

#生成随机手机号码
#参数mobileStart为手机号开头前三位
from time import sleep


def mobileNo(mobileStart):
    mobile = []
    mobileNo = ''
    mobile.append(mobileStart)
    i = 1
    while (i < 9):
        mobile.append(str(random.randint(0, 9)))
        i = i + 1

    mobileNo = mobileNo.join(mobile)
    return mobileNo

def isElement(self,identifyBy,c):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    sleep(1)
    flag=None
    try:
        if identifyBy == "id":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_id(c)
        elif identifyBy == "xpath":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath(c)
        elif identifyBy == "class":
            self.driver.find_element_by_class_name(c)
        elif identifyBy == "link text":
            self.driver.find_element_by_link_text(c)
        elif identifyBy == "partial link text":
            self.driver.find_element_by_partial_link_text(c)
        elif identifyBy == "name":
            self.driver.find_element_by_name(c)
        elif identifyBy == "tag name":
            self.driver.find_element_by_tag_name(c)
        elif identifyBy == "css selector":
            self.driver.find_element_by_css_selector(c)
        flag = True

    except Exception as e:
        flag = False
    finally:
        return flag
