# coding=utf-8
import unittest
import time

import requests



def testPost(self):
   orderno = time.strftime('%Y%m%d%X' ,time.localtime()).split(':')
   memo = "我是备注啊"
   latitude = '31.23577592339'
   longitude = '121.41764361893'
   participate_count = '10'
   task_id = '107271'
   order_no = '03292313'
   goods_name = '货物F'



   #header部分的配置
   headers = {
   'Host':'api.56come.cn',
   'User - Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
   'Accept':'application/json, text/plain, */*',
   'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
   'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
   'X-Requested-With':'XMLHttpRequest',
   'Referer':'https://api.56come.cn/proxy.html?r04181011',
   'Content-Length': '1069',
   'Cookie':'Hm_lvt_01d0eb3aac496cdccf683c3ed0c10aff=1468463586,1468896676,1468993393,1469088919; AccessToken=qFmrbUBh7F9FyErAfu9po8OkI5gjs6PB6pP3ZRoX; _gat=1; _ga=GA1.2.1163943480.1489752384; KONAPISID=eyJpdiI6IkQ4K2xjXC9ZbGhEUjN3eWFFV0paSDV3PT0iLCJ2YWx1ZSI6IlBPZXNMNjRCczhySmhyODNySnlGRUhnaVZ5U2FRWFJKMmpXRWZmUnplRkI3NkRKdGp5QkxxK2ZvdWJKdzNTOXBvZGp1ODlxcElcL3ZSTDNHc2NBTExEdz09IiwibWFjIjoiYmMxNTY2YTgwODM4NWFhOGMzNTlmZTg2ODFhMWEyZjk0ZmMxY2YzYmM0MDY0NTAzYmUyOTY3ZmM5MmFkMTAwOCJ9; KONAPISID=7d038c0d11f318c49dd93c38fe6252ca193e161f',
   'Connection':'keep-alive'
   }

   #cookie部分的配置



   keyword = {
       'orderInfo[no]':orderno,
       #10是报价吧
       'orderInfo[type]':'10',
       'orderInfo[total_price]':'',
       'orderInfo[memo]':memo,
       #
       'drivers[0][participant_type]':'1',
       'drivers[0][driver_id]':'7469',
       'drivers[0][driver_name]':'1127',
       'drivers[0][driver_mobile]':'1390001127',
       #
       'conditions[type]':'7',
       'conditions[latitude]':latitude,
       'conditions[longitude]':longitude,
       'conditions[radius]':'10000',
       'conditions[the_time]':'2017-04-19 23:29:04',
       'conditions[participate_count]':participate_count,
       'conditions[memo]':'上海市上海市普陀区谈家渡路28号',
       #
       'conditions[on_footprint]':'1',
       'tasks[0][task_id]':task_id,
       'tasks[0][order_no]':order_no,
       'tasks[0][quantity]':'1',
       'tasks[0][weight]':'1',
       'tasks[0][volume]':'0',
       'tasks[0][goods_name]':goods_name,
       'tasks[0][delivery_time]':'2017-03-30 23:59:37',
       'tasks[0][end_city]':'上海',
       'tasks[0][start_city]':'上海',
       'tasks[0][pickup_time]':'2017-03-29 23:59:37'

   }

   #post请求的构造
   res = requests.post('https://api.56come.cn/servlet/rfq/order/publish?KONAPISID=7d038c0d11f318c49dd93c38fe6252ca193e161f',
                      headers=headers,
                       data=keyword,verify=False)

   print(res.text)
   print(res.status_code)

   #验证
   #self.assertTrue(u'true' in res.text)

   return res.text




