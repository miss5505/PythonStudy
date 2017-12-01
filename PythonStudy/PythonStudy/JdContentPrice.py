"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
 
driver = webdriver.Chrome()
driver.get("https://item.jd.com/1294243.html")

#点击搜索按钮
#assert "Python" in driver.title
#elem = driver.find_element_by_id("choose-attrs")
elem=driver.find_element_by_class_name("form")
inputs=elem.find_element_by_tag_name("input")
inputs.send_keys("python")
buttonss=elem.find_element_by_class_name("cw-icon").click()
#buttonss.send_keys(Keys.ENTER)

cookiess=driver.get_cookies()
print(cookiess)
#遍历cookies中的name 和value信息打印，当然还有上面添加的信息
for cookie in cookiess:
    print ("%s -> %s" % (cookie['name'], cookie['value']))
print("-----------------------------------------------------")
areaId=driver.get_cookie("areaId");
print(areaId)
print("-----------------------------------------------------")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
html = driver.page_source
#driver.close()
driver.quit()

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
  print("小错误")   
#print(driver.page_source)

