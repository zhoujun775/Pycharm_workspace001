#encoding:utf-8
import requests
import re

'''
response = requests.get('http://www.baidu.com')
print(response.text)
print(response.headers)
print(response.status_code)
'''

'''
#抓取图片，二进制，content
response1 = requests.get('https://www.baidu.com/img/bd_logo1.png')
print(response1.content)
with open('E:\Personal Files\pic1.png', 'wb') as f:
    f.write(response1.content)
    f.close()
'''

#豆瓣

content = requests.get('https://book.douban.com/').text
#results = re.findall('<li.*?info.*?.*?title.*?href="(.*?)"\stitle="(.*?)".*?author">(.*?)</div>', content, re.S)
results2 = re.findall('<div class="author">(.*?)</div>', content, re.S)
results3 = re.findall('<div class="info">.*?<a class="" href="(.*?)".title="(.*?)".*?</a>', content, re.S)
print(results3)
for results in results3:
    print("-------------")
    print(results)
print("-----------over------------")
'''
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
for result in results:
    url, name, author, date = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    print(url, name, author, date)
'''
