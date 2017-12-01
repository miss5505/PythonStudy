import requests 
import datetime  
import time 
import os

#通过正则表达式来获取图片地址，并下载到本地
def getImg(_url,file_path):
    print(_url)
    pic = requests.get(_url, timeout=30)      
    if pic.status_code == 200:
        #写入图片
        names = _url.split('/')
        name = names[len(names) - 1]
        fileName = file_path + name
        fp = open(fileName,'wb')
        fp.write(pic.content)
        fp.close()
        print("ok")
    else :
        print(_url)


# 2017 10 08 07 03 55 330136 _12387498.jpg
url = 'http://image2.58ubk.com/up/gcard/p20171008/20171008$_12387498.jpg'
file_path = os.path.join(os.getcwd(),'dir_name\\file_name\\')

sum = 70000099999
counter = 1
while counter <= 190000000009:
    urlss = ""
    sum = sum + counter    
    if len(str(sum)) < 12 and len(str(sum)) > 0:
        urlss = "0" + str(sum)
    else:
        urlss = str(sum)
    counter += 1
    newUrl = url.replace("$",urlss)   
    html = getImg(newUrl,file_path)
  