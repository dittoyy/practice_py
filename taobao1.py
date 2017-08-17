#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-14 10:11:50
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$

#coding=utf-8
import time,os,chardet,random,requests,json

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from useragents import  agents

class Taobao(object):

    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.login_url='https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
        self.order_url='https://buyertrade.taobao.com/trade/itemlist/asyncBought.htm?action=itemlist/BoughtQueryAction&event_submit_do_query=1&_input_charset=utf8'
        self.num=0

    def login(self):　　　　　　###如果用phantomjs就用这几句，为了方便观察登录点击，才用chrome浏览器。
        # dcap = dict(DesiredCapabilities.PHANTOMJS)
        # dcap["phantomjs.page.settings.userAgent"] = ('Mozilla/5.0(WindowsNT6.1;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/59.0.3071.115Safari/537.36x-requested-with:XMLHttpRequest')#(random.choice(agents))
        # dcap["phantomjs.page.settings.loadImages"] = True
        # driver = webdriver.PhantomJS(executable_path='C:\\Python27\\phantomjs.exe',desired_capabilities=dcap)

        driver=webdriver.Chrome()
        driver.get(self.login_url)
        driver.find_element_by_id('J_Quick2Static').click()

        WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, 'TPL_username_1')))
        driver.find_element_by_id('TPL_username_1').send_keys(self.name)
        driver.save_screenshot('1.jpg')                 ###如果用phantomjs，最好需要截图，因为phantomjs没有界面。
        driver.find_element_by_id('TPL_password_1').send_keys(self.password)
        driver.save_screenshot('2.jpg')
        driver.find_element_by_id('J_SubmitStatic').click()
        time.sleep(10)
        driver.save_screenshot('3.jpg')
        self.cookies={}
        for dictx in driver.get_cookies():                ##取出driver的cookie，组装成requests的cookie样式
            self.cookies[dictx['name']]=dictx['value']
        driver.quit()



    def get_orders(self,p,flag):
        if flag==0:                    ###flag==1时候，不需要重复登陆了。
            self.login()
            print self.cookies
        datax={'pageNum':p+1,
                'pageSize':15,
               'prePageNo':p,
               }
        header = {'origin': 'https://buyertrade.taobao.com',
                'referer':'https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm',
                'user-agent':'Mozilla/5.0(WindowsNT6.1;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/59.0.3071.115Safari/537.36x-requested-with:XMLHttpRequest',
                  #'cookie':'miid=8452520455432281194; thw=cn;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.....',           ###如果不登陆，可以用headers携带cookie的方式
                  }
        resp=requests.post(self.order_url,data=datax,cookies=self.cookies,headers=header)
        #resp=requests.post(self.order_url,data=datax,headers=header)
        #print resp.content.decode('gbk')
        orders_dictx = json.loads(resp.content.decode('gbk'))
        pages=orders_dictx['page']['totalPage']
        for order in orders_dictx['mainOrders']:
            self.num+=1
            print self.num,' ',order['subOrders'][0]['itemInfo']['title'],'    价格是： ',order['payInfo']['actualFee'],'元 交易状态是：',order['statusInfo']['text']

        if flag==0:             ##因为是调用函数自己，只需要第一次做这个就可以。
            for p in range(1,pages+1):
                self.get_orders(p,1)

if __name__=="__main__":
    pass
    tb=Taobao('969956574@qq.com','20112011oo')   ##传入账号 密码
    tb.get_orders(0,0)
