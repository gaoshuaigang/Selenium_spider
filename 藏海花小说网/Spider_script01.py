# -*- coding: utf-8 -*-
# 先启动自定义浏览器
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir='/Users/gaosg/Public'
import os
import re
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
        driver.get('https://www.zanghaihua.org/book/40438/')
        driver.implicitly_wait(5)
        # 获取章节名称和地址
        content = driver.find_element(By.XPATH, value='//*[@id="section-list"]').get_attribute('outerHTML')
        # 打印爬取的HTML内容
        # print(a)
        # 解析返回内容
        soup = BeautifulSoup(content, 'html.parser')

        # 打开一个excel文件，存入目录内容
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # 在content内容中，遍历li标签
        for li in soup.find_all('li'):
            # 在li标签中，获取a标签文本和href属性
            a_tag = li.find('a')
            if a_tag:
                text = a_tag.get_text()
                href = 'https://www.zanghaihua.org/book/40438/'+a_tag['href']
                # 将数据写入Excel文件的第一列和第二列
                worksheet.append([text, href])

        # 保存Excel文件
        workbook.save('content.xlsx')


if __name__ == '__main__':
    download.setUp(webdriver)
