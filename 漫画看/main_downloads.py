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
        chrome_option = Options()
        chrome_option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        driver = webdriver.Chrome(executable_path='/Users/gaosg/chromedriver', options=chrome_option)

        driver.get('http://m.ymh1234.com/comic/16279.html')
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, value='//*[@id="list_block"]/div/div[2]/a/span').click()
        driver.implicitly_wait(5)
        document = driver.find_element(By.XPATH,'//*[@id="chapter-list-1"]').get_attribute('outerHTML')

        # 创建保存Excel文件的文件夹
        folder_path = 'People'
        os.makedirs(folder_path, exist_ok=True)

        # 检查是否存在已有的Excel文件
        try:
            workbook = openpyxl.load_workbook('People/output.xlsx')
            sheet = workbook.active
        except FileNotFoundError:
            # 如果文件不存在，则创建一个新的Excel文件
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            # 添加标题行
            sheet.append(['章节', '地址链接', '页数'])

        # 使用BeautifulSoup解析HTML代码
        soup = BeautifulSoup(document, 'html.parser')

        # 查找所有的li标签
        li_tags = soup.find_all('li')

        # 遍历每个li标签
        for li in li_tags:
            # 查找span标签和a标签
            span_tag = li.find('span')
            a_tag = li.find('a')

            # 提取span内容和a标签的href
            span_content = span_tag.text if span_tag else ''
            href = a_tag['href'] if a_tag else ''

            driver.get('http://m.ymh1234.com' + href)
            page = driver.find_element(By.XPATH, '//*[@id="images"]/p').get_attribute('outerHTML')

            # 使用正则表达式匹配数字
            match = re.search(r'\((\d+)/(\d+)\)', page)

            if match:
                total = match.group(2)  # 获取第二个括号内的数字
            else:
                print("No match found.")

            # 将span内容和href写入Excel表格的新行
            sheet.append([span_content, 'http://m.ymh1234.com'+href, total])

            # 保存Excel文件
            file_path = os.path.join(folder_path, 'output.xlsx')
            workbook.save(file_path)

            time.sleep(2)

if __name__ == '__main__':
    download.setUp(webdriver)
