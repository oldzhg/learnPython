# -*- coding:utf-8 -*-
import urllib.request
url = 'http://www.xygz.com.cn/teacher/index.php?m=content&c=index&a=lists&catid=32'
webPage = urllib.request.urlopen(url)
date = webPage.read()
date = date.decode('gbk')
print(date)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
