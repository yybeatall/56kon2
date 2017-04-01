import unittest
import loginPro, logoutPro
import createTaskPro
import createSchedulePro


# mysuite = unittest.TestSuite()
# mysuite.addTest(loginsucc.MyTestCase("testLogIn"))
# mysuite.addTest(loginsucc.MyTestCase("testLoginsucc"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))


# 执行登录
logincases = unittest.TestLoader().loadTestsFromTestCase(loginPro.MyTestCase )
'''业务'''
# 执行创建任务
createTaskcases = unittest.TestLoader().loadTestsFromTestCase(createTaskPro.MyTestCase )
# 执行创建调度
createDeliverycases = unittest.TestLoader().loadTestsFromTestCase(createSchedulePro.MyTestCase )
# 注销
logutcases = unittest.TestLoader().loadTestsFromTestCase(logoutPro.MyTestCase )

mysuite = unittest.TestSuite([logincases, createTaskcases, createDeliverycases, logutcases])

# mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
