# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir='/Users/gaosg/Public'
# https://pm.zzbank.cn/devbook_works_report?utf8=%E2%9C%93&devbook_id=135206

import xlrd
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import test

dir_path = "/Users/gaosg/Selenium_spider/result/PM/"
chrome_option = Options()
chrome_option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_option)

for i in range(0,136):
    xlsx01 = xlrd.open_workbook(filename='ceshizirenwu.xlsx')
    table = xlsx01.sheet_by_name(sheet_name='Sheet1')
    value = table.cell_value(rowx=i+1, colx=3)
    print(value)
    url = 'https://pm.zzbank.cn/devbook_works_report?utf8=%E2%9C%93&devbook_id='+str(int(value))
    driver.get(url)
    #driver.get('https://pm.zzbank.cn/devbook_works_report?utf8=%E2%9C%93&devbook_id=145602')
    driver.implicitly_wait(5)
    try:
        inner = driver.find_element_by_xpath('//*[@id="option-filter"]/div[3]/table/tbody').get_attribute('innerHTML')
        # text = driver.find_element_by_xpath('//*[@id="option-filter"]/div[3]/table/tbody').text
        soup = BeautifulSoup(inner,'html.parser')
        #行数
        trcount = inner.count('<tr>')
        #标签数
        tdcount = inner.count('<td>')
        #计算出列数
        col = tdcount/trcount-1

        alltag = soup.find_all('p')
        c = list()
        for a in alltag:
            #b = a.text
            c.append(a.text)
        #分表，将列表按照列数分隔开
        code_list = test.list_of_groups(c, int(col))

        xlsx01 = openpyxl.load_workbook('ceshizirenwu2.xlsx')
        ws = xlsx01.worksheets[0]

        for value in code_list:
            #print(value)
            xiangmu = value[0]
            taskid = value[2]
            name = value[4]
            gongsi = value[5]
            shixiang = value[7]
            jine = value[8]
            ws.append([xiangmu,taskid,name,gongsi,shixiang,jine])
        xlsx01.save('ceshizirenwu2.xlsx')
    except:
        print('未找到元素')
        # xlsx01 = openpyxl.load_workbook('ceshizirenwu1.xlsx')
        # sheet = xlsx01['Sheet']
        # b = 'B' + str(i + 2)
        # sheet[b] = '任务类，单独查询'
    # xlsx01.save('ceshizirenwu1.xlsx')

# driver.close()

