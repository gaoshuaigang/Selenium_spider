# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir='/Users/gaosg/Public'
# https://pm.zzbank.cn/devbook_works_report?utf8=%E2%9C%93&devbook_id=135206

import xlrd
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

dir_path = "/Users/gaosg/Selenium_spider/result/PM/"
chrome_option = Options()
chrome_option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_option)

for i in range(0,158):
    xlsx01 = xlrd.open_workbook(filename='ceshizirenwu.xlsx')
    table = xlsx01.sheet_by_name(sheet_name='Sheet3')
    value = table.cell_value(rowx=i+1, colx=2)
    url = 'https://pm.zzbank.cn/issues/'+str(int(value))
    driver.get(url)
    driver.implicitly_wait(2)
    try:
        text = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/div/p/a').text
        bookid = text[-6:]
        print(bookid)
        xlsx01 = openpyxl.load_workbook('ceshizirenwu1.xlsx')
        sheet = xlsx01['Sheet']
        b = 'B' + str(i+2)
        sheet[b] = bookid
    except:
        xlsx01 = openpyxl.load_workbook('ceshizirenwu1.xlsx')
        sheet = xlsx01['Sheet']
        b = 'B' + str(i + 2)
        sheet[b] = '任务类，单独查询'
    xlsx01.save('ceshizirenwu1.xlsx')

driver.close()

