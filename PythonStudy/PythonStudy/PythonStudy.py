
'''
第一部分 requests 爬虫
import requests

url = "http://www.baidu.com"
r = requests.get(url)
# 如果状态码不是200 则应发HTTOError异常
#r.raise_for_status()
# 设置正确的编码方式
#r.encoding = r.apparent_encoding()
print(r.text)
'''

"""
'''第二部分 beautifulsoup4 '''
#导入bs4模块
from bs4 import BeautifulSoup

html=r"<html><head><title name='ceshi' class='ceshi'>The Dormouse's story</title></head><body><p class=title><b>The Dormouse's story</b></p><p class=story>Once upon a time there were three little sisters; and their names were<a href=/elsie class=sister id=link1>Elsie</a>,<a href=/lacie class=sister id=link2>Lacie</a> and<a href=/tillie class=siste id=link3>Tillie</a>and they lived at the bottom of a well.</p></html>";


#做一个美味汤
soup = BeautifulSoup(html,'html.parser')
#输出结果
#print(soup.prettify())

#找到文档的title
#print(soup.title)
#title的标签名
#print(soup.title.name)
#title中的字符串String
#print(soup.title.string)
#文档的第一个找到的段落
#print(soup.p)
#找到所有的a标签
#print(soup.find_all('a'))
#找到id值等于3的a标签
#soup.find(id="link3")
#print(soup.find(id="link3"))
#print(soup.find(class_="ceshi"))
#print(soup.find(attrs={'class','ceshi'}))
#print(soup.find(attrs={'name','ceshi'}))


#发现了没有，find_all方法返回的是一个可以迭代的列表
for link in soup.find_all('a'):
    print(link.get('id'))
    print(link.get('class'))
    print(link.get('href'))
"""

"""
''' 正则'''
import re

str1 = 'hello , world ,life is short ,use,who,what'
b = re.search(r'w.+D',str1,re.I)
print(b.group())

c = re.findall(r'w\w+',str1,re.M)
for x in c.group():
    print(x)

d = re.search(r'w+',str1,re.S)
print(d.group())

"""
"""
import time
import requests 
from bs4 import BeautifulSoup

# 首先我们写好抓取网页的函数
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "

def get_content(url):
    comments = []
    html = get_html(url)
    
    soup = BeautifulSoup(html,'lxml')
    liTags = soup.find_all('li',attrs={'class':' j_thread_list clearfix'})

    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find('a',attrs={'class':'j_th_tit '}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + li.find('a', attrs={'class': 'j_th_tit '})['href']
            comment['authorname'] = li.find('span', attrs={'class': 'tb_icon_author '}).text.strip()
            comment['time'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('出了点小问题')
    return comments

def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中,注意保存文档编码问题。

    '''
    with open('TTBT.txt', 'a',encoding='utf8') as f:
        f.write("\n-------------------------------------我是分割线-----------------------------------------\n")
        i=0
        for comment in dict:
            i+=1
            f.write('({})标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {}\n'.format(i,comment['title'], comment['link'], comment['authorname'], comment['time'],comment['replyNum']))

        print('当前页面爬取完成')

def main(base_url, deep):
    url_list = []
    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    #循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        Out2File(content)
        #print('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {}
        #\n'.format(content[0], content[1], content[2], content[3],
        #content[4]))
    print('所有的信息都已经保存完毕！')


base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
# 设置需要爬取的页码数量
deep = 3
if __name__ == '__main__':
    main(base_url, deep)
 """