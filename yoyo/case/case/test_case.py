# coding:utf-8
import sys
sys.path.append(r'D:\yoyo\yoyo')
from blog.blog_login_page import  LoginPage, login_url
from blog.blog_login_sucess_page import LoginSucessPage, login_sucess_url
import unittest
from common.yoyo_selenium import browser

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = browser()

    def yewu1(self):
        # 登录页面操作,第一个页面
        driver_login = LoginPage(self.driver)
        driver_login.open(login_url)
        driver_login.login(u"上海-悠悠", "xxx")

    def yewu2(self):
        # # 登录成功页面操作 ,第二个页面
        driver_sucess = LoginSucessPage(self.driver)
        driver_sucess.input_sign("hao123")
        driver_sucess.click_by_blog()

    def test_yewu1(self):
        self.yewu1()

    def test_yewu2(self):
        self.yewu2()

    def test_01(self):
        self.yewu1()  # 登录
        self.yewu2()  # 下单
