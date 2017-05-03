import unittest

from app56konPro import createSchedulePro
from app56konPro import createTaskDeliveryPro
from app56konPro import createTaskDispatchPro
from app56konPro import createTaskPro
from app56konPro import loginPro
from app56konPro import logoutPro

# mysuite = unittest.TestSuite()
# mysuite.addTest(loginsucc.MyTestCase("testLogIn"))
# mysuite.addTest(loginsucc.MyTestCase("testLoginsucc"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))

# 执行创建任务并调度
createTaskDispatchcases = unittest.TestLoader().loadTestsFromTestCase( createTaskDispatchPro.MyTestCase )

mysuite = unittest.TestSuite([createTaskDispatchcases])

# mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))

myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
