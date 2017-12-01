
import os
import urllib
import logging
import sys
import urllib.request
import requests 
 
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    stream=sys.stdout)
 
file_path = os.path.join(os.getcwd(),'dir_name\\file_name\\')
 
if not os.path.isfile(file_path):
    logging.info("File doesn't exist.")
    # replace with url you need
    url = 'http://127.0.0.1:99/Image/add.png'
 
    # if dir 'dir_name/' doesn't exist
    file_dir = file_path[:-9]
    if not os.path.exists(file_dir):
        #logging.info("Mkdir 'dir_name/'.")
        os.mkdir(file_dir)
 
    def down(_save_path, _url):
        print(_save_path)
        print(_url)
        #urllib.urlretrieve(_url, _save_path)
        #urllib.request.urlretrieve(_url,_save_path)
               
        pic = requests.get(_url, timeout=30)      
        if pic.status_code == 200:
            #写入图片
            names = _url.split('/')
            name = names[len(names) - 1]
            fileName = file_path + name
            fp = open(fileName,'wb')
            fp.write(pic.content)
            fp.close()
        else :
            print(pic.status_code)
 
    #logging.info("Downloading file.")
    down(file_path, url)
else:
    logging.info("File exists.")

