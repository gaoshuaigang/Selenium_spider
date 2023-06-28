# -*- coding: utf-8 -*-
#先启动自定义浏览器
#/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir='/Users/gaosg/Public'

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

dir_path = "/Users/gaosg/Selenium_spider/result/ebook/"
chrome_option = Options()
chrome_option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_option)


for URL in open('/Users/gaosg/Selenium_spider/value/ebook'):
    driver.get(URL)
    time.sleep(2)
    title = driver.find_element_by_xpath(
        '//*[@id="root"]/div/main/div/div/div[3]/div[1]/a/section/h3').text
    full_path = dir_path + title + '.txt'

    try:
        os.remove(full_path)
        file = open(full_path, 'a+')
        file.write(title)
        file.close()
        print('新建-' + title)

        driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div/div/div[1]/ul/li[1]/span').click()
        driver.implicitly_wait(5)
        tt1 = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[2]/div[1]/ul').get_attribute(
            'outerHTML')

        html = tt1
        soup = BeautifulSoup(html, 'lxml')
        file_1 = dir_path + title + '.txt'
        f_cont = open(file_1, 'a+')
        for item in soup.find_all("a"):
            tt_all = item["href"]
            url1 = "https://www.zhihu.com" + tt_all
            # print("https://www.zhihu.com"+tt_all)
            driver.get(url1)
            time.sleep(4)
            cont1 = driver.find_element_by_xpath(
                '//*[@id="root"]/div/main/div/div/div[2]/div[2]/div').get_attribute('outerHTML')
            cont1_1 = BeautifulSoup(cont1, 'lxml')
            cont1_1_1 = cont1_1.text
            f_cont.write(str(cont1_1_1))

        f_cont.close()

    except Exception:
        file = open(full_path, 'a+')
        file.write(title)
        file.close()
        print('新建-' + title)

        driver.find_element_by_xpath(
            '//*[@id="root"]/div/main/div/div/div[1]/ul/li[1]/span').click()
        driver.implicitly_wait(5)
        tt1 = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[2]/div[1]/ul').get_attribute(
            'outerHTML')

        html = tt1
        soup = BeautifulSoup(html, 'lxml')
        file_1 = dir_path + title + '.txt'
        f_cont = open(file_1, 'a+')
        for item in soup.find_all("a"):
            tt_all = item["href"]
            url1 = "https://www.zhihu.com" + tt_all
            # print("https://www.zhihu.com"+tt_all)
            driver.get(url1)
            time.sleep(4)
            cont1 = driver.find_element_by_xpath(
                '//*[@id="root"]/div/main/div/div/div[2]/div[2]/div').get_attribute('outerHTML')
            cont1_1 = BeautifulSoup(cont1, 'lxml')
            cont1_1_1 = cont1_1.text
            f_cont.write(str(cont1_1_1))

        f_cont.close()


driver.close()