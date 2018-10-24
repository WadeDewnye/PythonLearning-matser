from urllib.parse import urlparse
import requests
from requests import Request, Session
import re


result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)

result1 = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='', allow_fragments=False)
# print(result1)
# print(result1.scheme, result1[0], result1.netloc, result1[1], sep='\n')

# 维持一个会话
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
# print(r.text)

# 证书验证
response = requests.get("https://www.12306.cn", verify=False)
print(response.status_code)

url = 'http://httpbin.org/post'
data = {
    'name': 'germy'
}
headers = {
    'User-Agent': 'Mozilla/s.o  (Macintosh;  Intel  MacOS  X  10 _11_4)  AppleWebKit/537.36  (KH TML,  lik e  Gecko )Chrome/53 .0.2785.116 Safari/537.36'
}
s = Session()
request = Request('Post', url, data=data, headers=headers)
prepared = s.prepare_request(request)
r = s.send(prepared)
print(r.text)

