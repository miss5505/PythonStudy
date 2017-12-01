"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import time
 
driver = webdriver.Chrome()
driver.get("http://192.168.2.84:94/admin/login")
time.sleep(5)

#点击搜索按钮
#elem=driver.find_element_by_class_name("form")
#inputs=elem.find_element_by_tag_name("input")
#inputs.send_keys("python")
#buttonss=elem.find_element_by_class_name("cw-icon").click()
username=driver.find_element_by_id("LoginName")
username.send_keys("a001")
pwd=driver.find_element_by_id("LoginPwd")
pwd.send_keys("123456")
buttonss=driver.find_element_by_id("logoSubmit").click()


cookiess=driver.get_cookies()
print(cookiess)
print("-----------------------------------------------------")
areaId=driver.get_cookie("enQuiryCook");
print(areaId)
print("-----------------------------------------------------")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)

#driver.close()
#driver.quit()

#Out2File(html)

#192.168.2.84:94/purchase/arrivalenquiry

#向cookie的name 和value添加会话信息。
#driver.add_cookie({'name':'enQuiryCook', 'value':'a001____9'})

# 开启新窗口
time.sleep(1)
newwindow = 'window.open("http://192.168.2.84:94/purchase/arrivalenquiry");'
driver.execute_script(newwindow)
# 切换到新的窗口
handles = driver.window_handles
driver.switch_to_window(handles[-1])

#driver.get("http://192.168.2.84:94/purchase/arrivalenquiry")
cookiess=driver.get_cookies()
print(cookiess)
print("-----------------------------------------------------")


#遍历cookies中的name 和value信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print ("%s -> %s" % (cookie['name'], cookie['value']))

html = driver.page_source
soup = BeautifulSoup(html,'lxml')
title = soup.find_all('button',attrs={'class':'btn-success'})[0].text      
print('标题' + title)



doc = pq(driver.page_source)
print("测试pyquery:"+doc(".btnaction").text())
cname=doc(".btn-success").children()
print(cname)
print(cname.attr("class"))
#for cc in doc(".btnaction").items():
#    print ("%s " % (cc.attr("class")))

for cc in doc(".btn-success").find('span').items():
    print ("%s " % (cc.attr("class")))


print("--------------------测试pyquery---------------------------------")


driver.get("http://192.168.2.84:94/purchase/purchasedemand")
cookiess=driver.get_cookies()
print(cookiess)
print("-----------------------------------------------------")
areaId=driver.get_cookie("enQuiryCook");
print("测试2：")
print(areaId)
print("测试值2：")
print(areaId['value'])

print("-----------------------------------------------------")


#遍历cookies中的name 和value信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print ("%s -> %s" % (cookie['name'], cookie['value']))


#driver.close()
#driver.quit()
'''
html = driver.page_source
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
  print("小错误")   
#print(driver.page_source)
'''
