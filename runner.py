import unittest
import loginPro, logoutPro
import createTaskPro
import createSchedulePro
import createTaskDeliveryPro
import createTaskDispatchPro


# mysuite = unittest.TestSuite()
# mysuite.addTest(loginsucc.MyTestCase("testLogIn"))
# mysuite.addTest(loginsucc.MyTestCase("testLoginsucc"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))


# 执行登录
logincases = unittest.TestLoader().loadTestsFromTestCase(loginPro.MyTestCase)
'''业务'''
# 执行创建任务
createTaskcases = unittest.TestLoader().loadTestsFromTestCase(createTaskPro.MyTestCase)
# 执行创建调度
createSchedulecases = unittest.TestLoader().loadTestsFromTestCase(createSchedulePro.MyTestCase)
# 执行创建任务并调度
createTaskDispatchcases = unittest.TestLoader().loadTestsFromTestCase(createTaskDispatchPro.MyTestCase)
# 执行创建任务并发送
createTaskDeliverycases = unittest.TestLoader().loadTestsFromTestCase(createTaskDeliveryPro.MyTestCase)
# 注销
logutcases = unittest.TestLoader().loadTestsFromTestCase(logoutPro.MyTestCase)

mysuite = unittest.TestSuite([logincases, createTaskcases, createSchedulecases, createTaskDeliverycases, logutcases])

# mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
