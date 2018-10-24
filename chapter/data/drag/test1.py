import urllib.request
import urllib.parse
import urllib.error
import socket
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, HTTPCookieProcessor
from urllib.error import URLError
from urllib.request import ProxyHandler
import http.cookiejar
import urllib.request
from urllib.request import HTTPError


# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheaders())
# print('server is ' + response.getheader('Server'))

# data = bytes(urllib.parse.urlencode({'hello': 'world'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# 处理请求超时的问题
# try:
#     response2 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
#     print(response2.read())
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# request1 = urllib.request.Request('https://www.python.org')
# response3 = urllib.request.urlopen(request1)
# print(response3.read().decode('utf-8'))

#使用Request来构造请求参数
# url = 'http://httpbin.org/post'
# headers = {
#     'User-agent': ' Mozilla/4.0(compatible;  MSIE 5.5;  Windows NT )',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# req.add_header('Content-Length', '10')
# response4 = urllib.request.urlopen(req)
# print(response4.read().decode('utf-8'))

# 高级用法  验证
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# 高级用法 代理
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
#
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


# cookies
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + " = " + item.value)

filename = 'cookie1.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# cookie = http.cookiejar.LWPCookieJar()
# cookie.load(filename, ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

try:
    response1 = urllib.request.urlopen('https://cuiqingcai.com/index.html')
    print('finished')
except HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except URLError as e:
    print(e.reason)
else:
    print('Request Successfully')


try:
    response2 = urllib.request.urlopen('https://www.baidu.com/', timeout=0.01)
except URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')










