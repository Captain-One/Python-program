# 爬虫步骤 两种方法分别介绍
# 1.使用urllib2 模块 python 3 使用 urllib.Request
# 2.使用tornado 模块

# urllib.request 主要 Functions:
# 1.urllib.request.urlopen(url,data=None,context=None)
# 2.urllib.request.Request(url,data=None,headers={},origin_req_host=None,unverifiable=Flase,method=None)

# tornado.httpclient 主要的类及方法
# 1.HTTPClient() 类
# 创建一个http客户端
# 方法：fetch()
# 2.HTTPRequest(url,methd="GET",headers=None,connect_timeout=None,request_timeout=None,...) 类
# 得到一个Request

# 爬虫一般步骤：
# 1.定义http头
# 2.定义一个请求，包含url、header等信息
# 3.根据请求得到响应
# 4.从响应中提取所需信息

# 示例

import urllib.request

# define header