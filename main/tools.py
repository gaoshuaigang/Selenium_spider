#用来分析获取a标签的href地址，前一步是把知乎某类书籍列表源码粘贴到html文件，然后将输出内容经过清洗，只选取pub域内的地址填入临时文件

from bs4 import BeautifulSoup

f = open('../value/ebok.html','r')
html = f.read()
soup = BeautifulSoup(html,'lxml')
for item in soup.find_all("a"):
    tt = item["href"]
    print(tt)