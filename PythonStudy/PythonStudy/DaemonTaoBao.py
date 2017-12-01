#coding=utf-8
__author__ = 'Daemon'

import requests
import re,os,datetime
from selenium import webdriver
from bs4 import BeautifulSoup

class Spider:
    def __init__(self):
        self.page = 1
        self.dirName = 'MMSpider'
        #这是一些配置 关闭loadimages可以加快速度 但是第二页的图片就不能获取了打开(默认)
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = False
        cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
        #self.driver = webdriver.PhantomJS(desired_capabilities=cap)
        #driver = webdriver.PhantomJS("D:/phantomjs/bin/phantomjs.exe)
        self.driver = webdriver.PhantomJS("C:\Program Files\Python36\Scripts\phantomjs.exe")

    def getContent(self,maxPage):
        for index in range(1,maxPage + 1):
            self.LoadPageContent(index)

    def getjdcontent(self):
        self.loadjdcontent()

#获取页面内容提取
    def LoadPageContent(self,page):
        #记录开始时间
        begin_time = datetime.datetime.now()
        url = "https://mm.taobao.com/json/request_top_list.htm?page=" + str(page)
        self.page+=1

        USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'
        headers = {'User-Agent':USER_AGENT }

        request = urllib3.Request(url,headers=headers)
        response = urllib3.urlopen(request)

        #正则获取
        pattern_link = re.compile(r'<div.*?class="pic-word">.*?<img src="(.*?)".*?'
                            r'<a.*?class="lady-name".*?href="(.*?)".*?>(.*?)</a>.*?'
                            r'<em>.*?<strong>(.*?)</strong>.*?'
                            r'<span>(.*?)</span>'
                             ,re.S)
        items = re.findall(pattern_link,response.read().decode('gbk'))

        for item in items:
        #头像，个人详情，名字，年龄，地区
            print(u'发现一位MM 名字叫%s 年龄%s 坐标%s' % (item[2],item[3],item[4]))
            print(u'%s的个人主页是 %s' % (item[2],item[1]))
            print(u'继续获取详情页面数据...')
        #详情页面
            detailPage = item[1]
            name = item[2]
            self.getDetailPage(detailPage,name,begin_time)

    def getDetailPage(self,url,name,begin_time):
        url = 'http:' + url
        self.driver.get(url)
        base_msg = self.driver.find_elements_by_xpath('//div[@class="mm-p-info mm-p-base-info"]/ul/li')
        brief = ''
        for item in base_msg:
            print(item.text)
            brief+=item.text + '\n'
            #保存个人信息
        icon_url = self.driver.find_element_by_xpath('//div[@class="mm-p-model-info-left-top"]//img')
        icon_url = icon_url.get_attribute('src')

        dir = self.dirName + '/' + name
        self.mkdir(dir)

    #保存头像
        try:
            self.saveIcon(icon_url,dir,name)
        except Exception:
            print(u'保存头像失败 %s' % e.message)

    #开始跳转相册列表
        images_url = self.driver.find_element_by_xpath('//ul[@class="mm-p-menu"]//a')
        images_url = images_url.get_attribute('href')
        try:
            self.getAllImage(images_url,name)
        except Exception:
            print(u'获取所有相册异常 %s' % e.message)

        end_time = datetime.datetime.now()
        #保存个人信息 以及耗时
        try:self.saveBrief(brief,dir,name,end_time - begin_time)
        except Exception:
            print(u'保存个人信息失败 %s' % e.message)


#获取所有图片
    def getAllImage(self,images_url,name):
        self.driver.get(images_url)
    #只获取第一个相册
        photos = self.driver.find_element_by_xpath('//div[@class="mm-photo-cell-middle"]//h4/a')
        photos_url = photos.get_attribute('href')

        #进入相册页面获取相册内容
        self.driver.get(photos_url)
        images_all = self.driver.find_elements_by_xpath('//div[@id="mm-photoimg-area"]/a/img')

        self.saveImgs(images_all,name)


    def saveImgs(self,images,name):
        index = 1
        print(u'%s 的相册有%s张照片, 尝试全部下载....' % (name,len(images)))

        for imageUrl in images:
            splitPath = imageUrl.get_attribute('src').split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = self.dirName + '/' + name + '/' + name + str(index) + "." + fTail
            print(u'下载照片地址%s ' % fileName)

            self.saveImg(imageUrl.get_attribute('src'),fileName)
            index+=1


    def saveIcon(self,url,dir,name):
        print(u'头像地址%s %s ' % (url,name))

        splitPath = url.split('.')
        fTail = splitPath.pop()
        fileName = dir + '/' + name + '.' + fTail
        print(fileName)
        self.saveImg(url,fileName)

    #写入图片
    def saveImg(self,imageUrl,fileName):
        print(imageUrl)
        u = urllib3.urlopen(imageUrl)
        data = u.read()
        f = open(fileName,'wb')
        f.write(data)
        f.close()

    #保存个人信息
    def saveBrief(self,content,dir,name,speed_time):
        speed_time = u'当前MM耗时 ' + str(speed_time)
        content = content + '\n' + speed_time

        fileName = dir + '/' + name + '.txt'
        f = open(fileName,'w+')
        print(u'正在获取%s的个人信息保存到%s' % (name,fileName))
        f.write(content.encode('utf-8'))

#创建目录
    def mkdir(self,path):
        path = path.strip()
        print(u'创建目录%s' % path)
        if os.path.exists(path):
            return False
        else:
            os.makedirs(path)
            return True

    def loadjdcontent(seft):
         #记录开始时间
        begin_time = datetime.datetime.now()
        url = "https://item.jd.com/1294243.html" 
        USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'
        headers = {'User-Agent':USER_AGENT }

        request = requests.get(url,headers=headers)
        request.encoding = 'gbk'
        #print(request.text)
        html=request.text
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

spider = Spider()
#获取前5页
spider.getjdcontent()