#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-10 14:12:18
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$
import unittest,time
import sys
sys.path.append(r'D:\template\template1')
from common.logger import Log
from selenium import webdriver
log = Log()
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(30)
    def test_01(self):
        log.info("-------测试用例开始---------")
        self.driver.find_element_by_id("kw").send_keys("yoyo")
        log.info("输入内容：yoyo")
        self.driver.find_element_by_id("su").click()
        log.info("点击按钮：id = su")
        time.sleep(2)
        t = self.driver.title
        log.info(u"获取title内容：%s"%t)
        self.assertIn(u"百度搜索",t)
    def tearDown(self):
        self.driver.quit()
        log.info("-------测试用例结束----------")
if __name__ == "__main__":
    unittest.main()