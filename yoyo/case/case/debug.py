# coding:utf-8
import sys
sys.path.append(r'D:\yoyo\yoyo')
from blog.blog_login_page import  LoginPage, login_url
from blog.blog_login_sucess_page import LoginSucessPage, login_sucess_url
import unittest
from common.yoyo_selenium import browser
from selenium import webdriver


driver = webdriver.Firefox()

driver_login = LoginPage(driver)
driver_login.open(login_url)
driver_login.login(u"上海-悠悠", "xxx")

driver_sucess = LoginSucessPage(driver)
driver_sucess.input_sign("hao123")
driver_sucess.click_by_blog()

