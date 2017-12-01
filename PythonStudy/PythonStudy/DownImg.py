import re
import requests 
import urllib,urllib3


#通过url获取网页
"""
def getHtml(url):
    # 要设置请求头，让服务器知道不是机器人
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    request=urllib3.Request(url,headers=headers);
    page = urllib3.urlopen(request);
    html = page.read()
    return html
"""

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



#通过正则表达式来获取图片地址，并下载到本地
def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        imgurl=imgurl.replace("//","http://")
        print(imgurl)
        names=imgurl.split('/')
        name=names[len(names)-1]
        print(name);       
        string = 'pictures\\'+name
        #通过urlretrieve函数把数据下载到本地的D:\\images，所以你需要创建目录
        saveImg(imgurl,string)
        x = x + 1

 #写入图片
def saveImg(imageUrl,fileName): 
    pic= requests.get(imageUrl, timeout=30)
    fp = open(fileName,'wb')
    fp.write(pic.content)
    fp.close()



html = get_html("http://www.qiushibaike.com/imgrank/")
getImg(html)
