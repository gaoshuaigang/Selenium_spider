# -*- coding: utf-8 -*-
# 先启动自定义浏览器
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir='/Users/gaosg/Public'

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

dir_path = "/Users/gaosg/Selenium_spider/result/PM/"
chrome_option = Options()
chrome_option.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_option)

for URL in open('/Users/gaosg/Selenium_spider/value/PMspider'):
    driver.get(URL)
    driver.implicitly_wait(5)
    title = driver.find_element_by_xpath('//*[@id="content"]/h2').text
    full_path = dir_path + title + '.txt'
    try:
        os.remove(full_path)
        file = open(full_path, 'a+')
        file.write(title)
        file.close()

        driver.find_element_by_xpath('//*[@id="filters"]/legend').click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="add_filter_select"]/option[7]').click()
        driver.implicitly_wait(3)
        # 选择目标窗口
        driver.find_element_by_xpath('//*[@id="values_fixed_version_id_1"]/optgroup[1]/option[6]').click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="query_form_with_buttons"]/p/a[1]').click()

        html = driver.find_element_by_xpath('//*[@id="content"]/form[2]/div/table/tbody').get_attribute('outerHTML')
        soup = BeautifulSoup(html, 'lxml')

        file_1 = dir_path + title + '.txt'

        text = soup.find().text

        f_cont = open(file_1, 'a+')
        for a in soup.find_all('tr'):
            id_ = a.find_all(class_='id')
            id1 = BeautifulSoup(str(id_), 'lxml')

            assigned_to_ = a.find_all(class_='assigned_to')
            assigned_to1 = BeautifulSoup(str(assigned_to_), 'lxml')

            subject_ = a.find_all(class_='subject')
            subject1 = BeautifulSoup(str(subject_), 'lxml')

            status_ = a.find_all(class_='status')
            status1 = BeautifulSoup(str(status_), 'lxml')

            id2 = str(id1.text).strip('[').strip(']')
            if len(id2):
                cont1_1_1 = '\n' + status1.text + ',' + id1.text + ',' + assigned_to1.text + ',' + subject1.text
                f_cont.write(str(cont1_1_1))
        f_cont.close()
    except Exception:
        file = open(full_path, 'a+')
        file.write(title)
        file.close()

        driver.find_element_by_xpath('//*[@id="filters"]/legend').click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="add_filter_select"]/option[7]').click()
        driver.implicitly_wait(3)
        # 选择目标窗口
        driver.find_element_by_xpath('//*[@id="values_fixed_version_id_1"]/optgroup[1]/option[6]').click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="query_form_with_buttons"]/p/a[1]').click()

        html = driver.find_element_by_xpath('//*[@id="content"]/form[2]/div/table/tbody').get_attribute('outerHTML')
        soup = BeautifulSoup(html, 'lxml')

        file_1 = dir_path + title + '.txt'

        text = soup.find().text

        f_cont = open(file_1, 'a+')
        for a in soup.find_all('tr'):
            id_ = a.find_all(class_='id')
            id1 = BeautifulSoup(str(id_), 'lxml')

            assigned_to_ = a.find_all(class_='assigned_to')
            assigned_to1 = BeautifulSoup(str(assigned_to_), 'lxml')

            subject_ = a.find_all(class_='subject')
            subject1 = BeautifulSoup(str(subject_), 'lxml')

            status_ = a.find_all(class_='status')
            status1 = BeautifulSoup(str(status_), 'lxml')

            id2 = str(id1.text).strip('[').strip(']')
            if len(id2):
                cont1_1_1 = '\n' + status1.text + ',' + id1.text + ',' + assigned_to1.text + ',' + subject1.text
                f_cont.write(str(cont1_1_1))
        f_cont.close()
driver.close()
