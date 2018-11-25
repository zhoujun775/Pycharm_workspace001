#encoding:utf-8
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

def getPageNum(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    pageinfo = soup.select('#wp_paging_w4 .page_nav a.last')[0]
    pattern = '.*?list(.*?).htm'
    last = re.findall(pattern, pageinfo['href'], re.S)
    #print(int(last[0]))
    return int(last[0])


def getCount(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    thispage = webdriver.Chrome(chrome_options=chrome_options)
    thispage.get(url)
    count = thispage.find_element_by_class_name("WP_VisitCount")
    return count.text


def write2file(txt):
    with open('E:\\test\\SEU_News.txt', 'a+', encoding='utf-8') as f:
        f.write(txt)
        f.close()


def main():
    page = 1
    pageNum = getPageNum('http://news.seu.edu.cn/5486/list5.htm')
    for page in range(1, pageNum+1):
        url = 'http://news.seu.edu.cn/5486/list' + str(page) + '.htm'
        content = requests.get(url).text
        soup = BeautifulSoup(content, 'lxml')
        res = soup.select('#wp_news_w4 table tr td[align="left"]')
        res2 = soup.select('#wp_news_w4 table tr td[width="30px"] div')
        print('正在爬取第' + str(page) + '页新闻')
        print('进度：', end='')
        i = 0
        temUrl = 'http://news.seu.edu.cn'
        for e in res:
            if i % 2 == 0:
                t = e.select('a["href"]')[0]
                recentUrl = temUrl + t['href']
                write2file(recentUrl + '\t' + t['title'] + '\t')
                #print(t['href'], t['title'], end='\t')

            else:
                t = e.select('div')[0]
                now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                #print(t.text, end=' ')
                #print(getCount(recentUrl))
                #print(now)
                write2file(getCount(recentUrl) + '\t' + t.text + '\t' + now + '\n')
                print('>', end='')
            i = i + 1
        print("\n-------------------------------------")


if __name__ == '__main__':
    main()
