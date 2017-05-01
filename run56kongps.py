import unittest

from app56kongpsPro import *


# mysuite = unittest.TestSuite()
# mysuite.addTest(loginsucc.MyTestCase("testLogIn"))
# mysuite.addTest(loginsucc.MyTestCase("testLoginsucc"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))

#注册
registerCases = unittest.TestLoader().loadTestsFromTestCase(registerPro.MyTestCase)

#注销
logutCases = unittest.TestLoader().loadTestsFromTestCase(logoutPro.MyTestCase )

#忘记密码
forgotPwdCases = unittest.TestLoader().loadTestsFromTestCase(forgotPwdPro.MyTestCase)

#执行登录
loginCases = unittest.TestLoader().loadTestsFromTestCase( loginPro.MyTestCase )

'''业务'''



mysuite = unittest.TestSuite([registerCases, logutCases, forgotPwdCases, loginCases])

# mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
