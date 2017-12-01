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
        r.encoding = 'gbk'
        return r.text
    except:
        return " ERROR "

def get_content(url):
    comments = []
    html = get_html(url)
    #Out2File(html)

    soup = BeautifulSoup(html,'lxml')
    title = soup.title.string
    print('标题' + title)
    try:
        skuname = soup.find_all('div',attrs={'class':'sku-name'})      
        print(skuname[0].text.strip())
        nprice = soup.find_all('span',attrs={'class':'price J-p-1294243'})
        print(nprice[0])
        oprice = soup.find_all('del',attrs={'id':'page_origin_price'})
        print(oprice[0].text.strip())
    except Exception:
       traceback.print_exc()   
   
    #print('标题： {} \t 链接：{} \t 秒杀价：{} \t 原始价格：{} \n'.format(title, skuname,
    #nprice, oprice))
    return comments

def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中,注意保存文档编码问题。

    '''
    with open('TTJD.txt', 'a',encoding='utf8') as f:
        f.write("\n-------------------------------------我是分割线-----------------------------------------\n")
        f.write(dict)
        print('当前页面写入完成')



def main():
    get_content('https://item.jd.com/1294243.html')   
if __name__ == "__main__":
    main()

