import random

#生成随机手机号码
#参数mobileStart为手机号开头前三位

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
