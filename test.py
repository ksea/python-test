
#! /usr/bin/env python

"""
param A :袋过滤的列表
return ：过滤所有数字后的列表
"""

# A = [1,2,3,'a','b','4','m','8','9', [2,1]]

# def x(a):
#     func = filter(lambda x: [y for l in x for y in func(l)] if type(x) is list else x , a)
#     return filter(lambda s: isinstance(s, list) is True, a)

# print (list(x(A)));


import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

idx = 0
#往paho/temperature 一直发送内容
while True:
    print("send success")
    publish.single("paho/temperature",
               payload="this is message:%s"%idx,
               hostname="127.0.0.1",
               client_id="lora1",
               # qos = 0,
               # tls=tls,
               port=1883,
               protocol=mqtt.MQTTv311)
    idx += 1



