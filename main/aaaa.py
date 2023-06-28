import re

xxx = 'https://www.zhihu.com/market/paid_column/1323317566170271744/section/1323321845911953408'
url1 = re.findall('(.*?)section', str(xxx))
print(url1)
