# -*- coding: utf-8 -*-
# 先启动自定义浏览器
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir='/Users/gaosg/Public'
import time

import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class download():
    def setUp(self):
        # 初始化浏览器，接管代理浏览器
        chrome_option = Options()
        chrome_option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        driver = webdriver.Chrome(executable_path='/Users/gaosg/chromedriver', options=chrome_option)

        # 打开网址
        driver.get('https://www.zhihu.com/pub/book/120044210')
        driver.implicitly_wait(5)
        shuming = driver.find_element(By.XPATH,
                                      value='//*[@id="root"]/div/main/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/h1').text
        driver.find_element(By.XPATH, value='//*[@id="root"]/div/main/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/a').click()
        driver.implicitly_wait(5)
        print(shuming)
        # 获取目录和地址
        driver.find_element(By.XPATH, value='//*[@id="root"]/div/main/div/div/div[1]/ul/li[1]/span').click()
        time.sleep(5)
        content = driver.find_element(By.XPATH, value='//*[@id="root"]/div/main/div/div/div[2]/div[1]/ul').get_attribute('outerHTML')

        # 解析返回内容
        soup = BeautifulSoup(content, 'html.parser')

        # 打开一个excel文件，存入目录内容
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # 在content内容中，遍历li标签
        for li in soup.find_all('li'):
            # 在li标签中，获取a标签文本和href属性
            a_tag = li.find('a')
            mulu = li.find('span')
            if a_tag:
                mulu = mulu.get_text()
                href = 'https://www.zhihu.com' + a_tag['href']
                # 将数据写入Excel文件的第一列和第二列
                worksheet.append([mulu, href])

        # 保存Excel文件
        workbook.save(f'cover/{shuming}.xlsx')


if __name__ == '__main__':
    download.setUp(webdriver)
