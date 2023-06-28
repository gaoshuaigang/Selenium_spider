# -*- coding: utf-8 -*-
#先启动自定义浏览器
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir='/Users/gaosg/Public'

import os
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#接管自启动的谷歌浏览器
from selenium.webdriver.common.by import By

dir_path = "/Users/gaosg/Selenium_spider/result/yanxaun/caishang/"
chrome_option = Options()
chrome_option.add_argument('--ignore-certificate-errors')   #主要是该条
chrome_option.add_argument('--ignore-ssl-errors')
chrome_option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_option)


for URL in open('/Users/gaosg/Selenium_spider/value/yanxuan'):

    driver.get(URL)
    driver.implicitly_wait(5)
    title = driver.find_element('xpath',
        '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]').text
    full_path = dir_path + title + '.txt'
    print(full_path)

    try:
        os.remove(full_path)
        file = open(full_path, 'a+')
        file.write(title)
        file.close()
        print('新书-' + title)

        try:
            driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]').click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath('//*[@id="bottomToolBar"]/div/div/div[2]/div[1]').click()
            time.sleep(3)
            # 获取当前页面域，后边访问子页面需要拼接使用
            currentPageUrl = driver.current_url
            currenturl = re.findall('(.*?)section', currentPageUrl)

            # 分析div中的子页面地址
            tt1 = driver.find_element_by_xpath('//*[@id="app"]/div').get_attribute('outerHTML')
            soup_0 = BeautifulSoup(tt1, 'lxml')
            # 取到目录的链接地址
            for n in soup_0.find_all('div', attrs={"class": re.compile('CatalogItem-catalogItem-uuMxb')}):

                url1 = re.findall('id\":\"(.*?)\"', str(n))
                # 打开文档保存子页面内容
                file_1 = dir_path + title + '.txt'
                f_cont = open(file_1, 'a+')
                # 访问每个子页面并保存内容
                for m in url1:
                    driver.get(currenturl[0] + 'section/' + m)
                    driver.implicitly_wait(5)
                    cont1 = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]').get_attribute('outerHTML')
                    cont1_1 = BeautifulSoup(cont1, 'lxml')
                    cont1_1_1 = cont1_1.text
                    f_cont.write(str(cont1_1_1))

                f_cont.close()
        except Exception:
            os.remove(full_path)
            print('***********爬取失败1************')

        continue

    except Exception:
        file = open(full_path, 'a+')
        file.write(title)
        file.close()
        print('新书-' + title)

        try:
            driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]').click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath('//*[@id="bottomToolBar"]/div/div/div[2]/div[1]').click()
            time.sleep(3)
            # 获取当前页面域，后边访问子页面需要拼接使用
            currentPageUrl = driver.current_url
            currenturl = re.findall('(.*?)section', currentPageUrl)

            # 分析div中的子页面地址
            tt1 = driver.find_element_by_xpath('//*[@id="app"]/div').get_attribute('outerHTML')
            soup_0 = BeautifulSoup(tt1, 'lxml')
            # 取到目录的链接地址
            for n in soup_0.find_all('div', attrs={"class": re.compile('CatalogItem-catalogItem-uuMxb')}):

                url1 = re.findall('id\":\"(.*?)\"', str(n))
                # 打开文档保存子页面内容
                file_1 = dir_path + title + '.txt'
                f_cont = open(file_1, 'a+')
                # 访问每个子页面并保存内容
                for m in url1:
                    driver.get(currenturl[0] + 'section/' + m)
                    driver.implicitly_wait(5)
                    cont1 = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]').get_attribute('outerHTML')
                    cont1_1 = BeautifulSoup(cont1, 'lxml')
                    cont1_1_1 = cont1_1.text
                    f_cont.write(str(cont1_1_1))

                f_cont.close()
        except Exception:
            os.remove(full_path)
            print('***********爬取失败2************')

        continue








driver.close()