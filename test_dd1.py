#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-10 14:12:18
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$
import unittest
import ddt
# from blog_login_page import LoginPage, login_url
# from read_exl import read_excel
# from common.yoyo_selenium import *
# da = read_excel("testdata.xlsx", u'login')
# test_li = da.read_dict()
# print test_li
test_li=[{u'username': u'123456781', u'psw': u'zhang', u'expect': u'True'},
         {u'username': u'123456', u'psw': u'111', u'expect': u'False'},
         {u'username': u'222', u'psw': u'33', u'expect': u'False'}]
@ddt.ddt
class test_ooooooooooo(unittest.TestCase):
    u'''登录页面的case'''
    def setUp(self):
        print 'start'
        # self.driver = LoginPage(browser())
        # self.driver.open(login_url)
    @ddt.data(*test_li)
    def test_login_01(self, data):
        '''登录成功按案例：输入正确账号密码'''
        print data["username"], data["psw"],data["expect"]

    # def test_login_02(self, data):
    #     '''登录888成功按案例：输入正确账号密码'''
    #     print data["username"], data["psw"],data["expect"]
    def tearDown(self):
        print 'end'

if __name__ == "__main__":
    unittest.main()
