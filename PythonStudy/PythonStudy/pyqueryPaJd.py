#pyquery使用总结  http://blog.csdn.net/cnmilan/article/details/8727308

from pyquery import PyQuery as pq

doc = pq('https://item.jd.com/1294243.html',encoding="utf-8")

t=doc('title')
print(t)
skuname = doc('.sku-name')      
print(skuname)

nprice = doc('div').find('.ellipsis')      
print(nprice)


