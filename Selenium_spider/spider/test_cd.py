#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


class TestCd(unittest.TestCase):
    """回收商网首页菜单主功能页是否正常"""

    def setUp(self):
        chrome_option = Options()
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=chrome_option)
        #self.driver.implicitly_wait(30)  # 隐性等待时间为30秒

    def test_gy1(self):
        """供应跳转页面打开是否正常"""
        driver = self.driver
        driver.get("http://www.huishoushang.com/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        #driver.find_element_by_xpath("//div[@id='nav']/div/a[2]").click()
        driver.find_element_by_xpath('//*[@id="nav"]/div/a[2]').click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(5)
        title2 = driver.title
        title3 = ""

        self.assertEqual(title3, title2, msg="断言失败")

    def test_gy2(self):
        """供应跳转页面打开是否正常"""
        driver = self.driver
        driver.get("http://www.huishoushang.com/")
        driver.implicitly_wait(5)
        driver.maximize_window()
        #driver.find_element_by_xpath("//div[@id='nav']/div/a[2]").click()
        driver.find_element_by_xpath('//*[@id="nav"]/div/a[2]').click()
        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(5)
        title2 = driver.title
        title3 = "二手设备出售_二手设备供应|价格,回收商网提供转让,处理,供应信息,第1页_回收商"

        self.assertEqual(title3, title2, msg="断言成功")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # 它是全局方法，把它屏蔽后，不在suite的用例就不会跑，exit = False表示中间有用例失败也继续执行,还有比较常用的verbosity=2，表示显示def名字
    unittest.main(exit=False, verbosity=2)
