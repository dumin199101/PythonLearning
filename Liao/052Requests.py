import requests
#发起get请求
r = requests.get('https://www.douban.com/')
#获取响应码跟文本
print(r.status_code)
# print(r.text)
#获取URL
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
#获取encoding：
print(r.encoding)
#获取响应内容（bytes）：
# print(r.content)
#获取json
r = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())
#传入header
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)
#post请求：
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
#携带cookie：
cs = {'token': '12345', 'status': 'working'}
r = requests.get("https://www.baidu.com", cookies=cs)
#响应时间：
r = requests.get("https://www.baidu.com", timeout=2.5) # 2.5秒后超时
#获取响应头：
print(r.headers)

