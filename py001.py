import pymysql
import time
import requests
from bs4 import BeautifulSoup
import re

'''
conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='mysql')
cursor = conn.cursor()
cursor.execute('select * from db')
print(cursor)
cursor.fetchone()
print(cursor.description)

'''
'''
for i in range(10):
    with open('E:\\test\\SEU_News.txt', 'a+') as f:
        f.write("abcc")
        f.close()
'''

'''
#解决编码问题：在windows下默认的文本文件编码为gbk，需要指定编码
str1 = '国际能源宪章秘书长乌尔班•鲁斯纳克一行访问东南大学'
print(str1)
with open('E:\\test\\test.txt', 'a+', encoding='utf-8') as f:
    f.write(str1)
    f.close()

'''

def getPageNum(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    pageinfo = soup.select('#wp_paging_w4 .page_nav a.last')[0]
    pattern = '.*?list(.*?).htm'
    last = re.findall(pattern, pageinfo['href'], re.S)
    #print(int(last[0]))
    return  int(last[0])

getPageNum('http://news.seu.edu.cn/5486/list5.htm')