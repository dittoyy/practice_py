# coding:utf-8
import unittest
import sys
sys.path.append(r'D:\yoyo\yoyo')
from blog.blog_retrieve_page import *

class Retrieve_test(unittest.TestCase):
    u'''登录页面的case'''
    def setUp(self):
        self.driver = RetrievePage()
        self.driver.open(retrieve_url)

    def test_retrieve(self):
        '''测试密码找回'''
        # 第一步输入邮箱
        self.driver.input_email("1233445")
        # 第二步输入验证码
        self.driver.input_authen("1234")
        # 点击提交按钮
        self.driver.submit_button()