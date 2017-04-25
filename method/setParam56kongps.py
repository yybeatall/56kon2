from appium import webdriver

screenCapturePath = '/Users/YUY/PycharmProjects/56kon2/app56kongpsPro/screenCapture/'
def setParam(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    # 天天模拟器
    # desired_caps['platformVersion'] = '4.4.4'
    # desired_caps['deviceName'] = '127.0.0.1:6555'

    # 夜神模拟器
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = '127.0.0.1:62001'

    desired_caps['appPackage'] = 'com.yihu001.kon.driver'
    desired_caps['appActivity'] = '.ui.activity.MainActivity'
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    # desired_caps["automationName"] = "Selendroid"
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return self.driver
