import urllib3
import re
import os
from pyquery import PyQuery as pq

# weburl = 'http://www.ireadweek.com'
weburl = 'http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E6%91%84%E5%BD%B1%E6%8A%80%E5%B7%A7&ie=utf8&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=0&sourceid=sugg&sut=0&sst0=1517384243808&lkt=0%2C0%2C0&p=40040108'


if __name__ == "__main__":
    http = urllib3.PoolManager()
    r = http.request('GET', weburl);
    # for link, t in re.findall(r'(/index.php/bookInfo[^\s]*?(html))', str(r.data)):
    for link, t in re.findall(r'(http://mp.weixin.qq.com/s[^\s]*?(&new=1))', str(r.data)):
        print(link)
        # downloadurl = weburl + link
        # dr = http.request('GET', downloadurl)
        # doc = pq(downloadurl)
        # print("book:" + doc('.hanghang-za-title').eq(0).text() + " Url: " + doc('.downloads').attr('href'))

