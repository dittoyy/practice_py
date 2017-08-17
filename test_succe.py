#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-10 14:12:18
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$
from selenium import webdriver
import unittest
import ddt
import sys
sys.path.append(r'D:\template\template1')
from blog.blog_login_page import LoginPage, login_url
from read_exl import read_excel
from common.selenium_pack1 import *
from selenium.webdriver.support import expected_conditions as EC
url='https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F'
class Login_success(unittest.TestCase):
    def setUp(self):
        self.driver=browser()

    def denglu(self):
        driver_login=Loginpage(self.driver)
        driver_login.open(url)
        driver_login.input_username('杰杰xhyl')
        driver_login.input_password('!aa120827')
        driver_login.remember()
        driver_login.click_submit()

    def test_denglu(self):
        '''测试前置条件登录成功'''
        self.denglu()

    def test01(self):
        '''进入我的主页,测试我关注的人 '''
        self.denglu()
        driver=Login_succ(self.driver)
        #第1步：查找主页
        driver.fin_J()
        #第2步：点击我关注的人
        driver.click_Focus()
        #第3步：测试结果,判断是否存在字段
        result =driver.text_in_element(('id', 'a_followees'), '杰杰xhyl关注的人(0)')
        driver.get_ele_text(('id', 'a_followees'))
        #第4步：期望结果
        expect_result = True
        print(result)
        #第5步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)
        #第6步：判断成功返回主页
        driver.bsck_home()
    def test02(self):
        '''进入我的主页,测试我的粉丝'''
        self.denglu()
        driver = Login_succ(self.driver)
        # 第1步：查找主页
        driver.fin_J()
        # 第2步：点击我的粉丝
        driver.click_fs()
        # 第3步：测试结果,判断是否存在字段
        result = driver.text_in_element(('id', 'a_followers'), '杰杰xhyl的粉丝(0)')
        driver.get_ele_text(('id', 'a_followers'))
        # 第4步：期望结果
        expect_result = True
        print(result)
        # 第5步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)
        # 第6步：判断成功返回主页
        driver.bsck_home()
    def test03(self):
        '''成功的上传头像图片'''
        self.denglu()
        driver = Login_succ(self.driver)
        # 第1步：查找主页
        driver.fin_J()
        # 第2步，点击修改头像
        driver.edit_head()
        time.sleep(1)
        # 第3步，导入图片
        driver.input_img('E:\\QQ图片20170510133440.jpg')
        # 第4步，点击保存
        driver.keep_img()
        # 第5步：测试结果,判断是否存在字段
        result = driver.text_in_element(('id', 'croped_message'), '裁切并保存')
        driver.get_ele_text(('id', 'croped_message'))
        # 第6步：期望结果
        expect_result = True
        print(result)
        # 第7步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)
    def test04(self):
        '''上传头像图片点击取消 '''
        self.denglu()
        driver = Login_succ(self.driver)
        # 第1步：查找主页
        driver.fin_J()
        # 第2步，点击修改头像
        driver.edit_head()
        time.sleep(1)
        # 第3步，导入图片
        driver.input_img('E:\\QQ图片20170510133440.jpg')
        # 第4步，点击返回
        driver.img_back()
        # 第5步：测试结果,判断是否存在字段
        result = driver.text_in_element(('xpath',".//*[@id='header_user_right']/a[2]"), '杰杰xhyl')
        driver.get_ele_text(('xpath', ".//*[@id='header_user_right']/a[2]"))
        # 第6步：期望结果
        expect_result = True
        print(result)
        # 第7步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)
    def test05(self):
        '''上传头像未上传点击取消 '''
        self.denglu()
        driver = Login_succ(self.driver)
        # 第1步：查找主页
        driver.fin_J()
        # 第2步，点击修改头像
        driver.edit_head()
        time.sleep(1)
        # 第4步，点击返回
        driver.img_back()
        # 第4步：测试结果,判断是否存在字段
        result = driver.text_in_element(('xpath', ".//*[@id='header_user_right']/a[2]"), '杰杰xhyl')
        driver.get_ele_text(('xpath', ".//*[@id='header_user_right']/a[2]"))
        # 第5步：期望结果
        expect_result = True
        print(result)
        # 第6步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)
    def test06(self):
        '''进入我的闪存搜索内容不存在点击返回 '''
        self.denglu()
        driver = Login_succ(self.driver)
        # 第1步：查找主页
        driver.fin_J()
        # 第2步，点击我的闪存
        driver.flash_homepage()
        time.sleep(1)
        # 第3步，输入搜索字段
        driver.fh_search('哈哈哈哈')
        # 第4步：点击确认
        driver.click_search()
        # 第5步：测试结果,判断是否存在字段
        result = driver.text_in_element(('class name','back-ing'), '返回')
        driver.get_ele_text(('xpath', ".//*[@id='main']/h3"))
        # 第6步：期望结果
        expect_result = True
        print(result)
        # 第7步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)
        # 第8步：点击返回成功
        driver.back_serach()
    def test07(self):
        '''进入我的闪存搜索内容为空点击返回 '''
        self.denglu()
        driver = Login_succ(self.driver)
        # 第1步：查找主页
        driver.fin_J()
        # 第2步，点击我的闪存
        driver.flash_homepage()
        time.sleep(1)
        # 第3步，输入搜索字段
        driver.fh_search(' ')
        # 第4步：点击确认
        driver.click_search()
        # 第5步：测试结果,判断是否存在字段
        result = driver.text_in_element(('class name','back-ing'), '返回')
        driver.get_ele_text(('xpath', ".//*[@id='main']/h3"))
        # 第6步：期望结果
        expect_result = False
        print(result)
        # 第7步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)
    def test08(self):
        '''进入我的闪存导出闪存点击确认 '''
        self.denglu()
        driver = Login_succ(self.driver)
        # 第1步：查找主页
        driver.fin_J()
        # 第2步，点击我的闪存
        driver.flash_homepage()
        time.sleep(1)
        # 第3步，成功导出闪存
        driver.click_myfs(True)
        time.sleep(4)
        # 第4步：测试结果,判断是否存在字段
        result = driver.text_in_element(('xpath', ".//*[@id='main']/h3"), '杰杰xhyl的闪存')
        driver.get_ele_text(('xpath', ".//*[@id='main']/h3"))
        # 第5步：期望结果
        expect_result = True
        print(result)
        # 第6步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)
    def test09(self):
        '''进入我的闪存导出闪存点击取消 '''
        self.denglu()
        driver = Login_succ(self.driver)
        # 第1步：查找主页
        driver.fin_J()
        # 第2步，点击我的闪存
        driver.flash_homepage()
        time.sleep(1)
        # 第3步，导出闪存点击取消
        driver.click_myfs(False)
        # 第4步：测试结果,判断是否存在字段
        time.sleep(4)
        result = driver.text_in_element(('xpath',"//*[contains(text(),'导出我的闪存')]"), '导出我的闪存')
        driver.get_ele_text(('xpath', ".//*[@id='main']/h3"))
        # 第5步：期望结果
        expect_result = True
        print(result)
        # 第6步：断言测试结果与期望结果一致
        self.assertEquals(result, expect_result)



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()