#-*-coding:utf-8-*-
#-*-coding:utf-8-*-
import sys
reload(sys)   
sys.setdefaultencoding('utf8') 

import win32api
import win32gui
import win32con #导入win32api相关模块  
import time

from win32gui import *

from selenium import webdriver 
# 打开Chrome浏览器 
#browser = webdriver.Chrome()
#browser.get("https://www.yestae.com/login")


print "hello"

import datetime
print datetime.datetime.now()


begin_time = datetime.datetime.now()
time.sleep(0.511111111)

end_time = datetime.datetime.now()
d_time = end_time - begin_time

print d_time.total_seconds()


import time
print str(int(time.time()*1000000))  #打印时间戳 时间戳是个啥？
print time.time()
