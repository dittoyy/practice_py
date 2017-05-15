# coding:utf-8
import sys
sys.path.append(r'D:\yoyo\yoyo')
# print sys.path
from common import *
from common.yoyo_selenium import *
login_sucess_url = "https://home.cnblogs.com/"

class LoginSucessPage(Yoyo):
    # 定位器，定位页面元素
    name_loc = ("id", 'lnk_current_user')  # 账号名称
    input_sign_loc = ("id", 'txt_ing')     # 签名
    radio_open_loc = ("id", 'ing_type_public')
    radio_private_loc = ('id', 'ing_type_private')
    add_tag_loc = ('link text', '加标签')
    btn_pulish_loc = ('id', 'btn_ing_publish')  # 发布
    my_blog_loc = ('link text', '我的博客')  # 我的博客首页

    def click_username(self):
        '''点击个人账号，进个人中心'''
        self.click(self.name_loc)

    def input_sign(self,text):
        '''输入签名'''
        self.send_keys(self.input_sign_loc, text)

    def select_radio_open(self):
        '''选中公开按钮'''
        self.click(self.radio_open_loc)

    def select_radio_private(self):
        '''选中私有按钮'''
        self.click(self.radio_private_loc)

    def select_add_tag(self):
        '''选中添加标签'''
        self.click(self.add_tag_loc)

    def click_btn_pulish_(self):
        '''点击发布按钮'''
        self.click(self.btn_pulish_loc)

    def click_by_blog(self):
        '''点击我的博客链接'''
        self.click(self.my_blog_loc)
if __name__ == '__main__':
    blog1=LoginSucessPage(browser())
    blog1.open(login_sucess_url,'首页 - 园子 - 博客园')
    # blog1.login('969956574@qq.com','969956574@qq.com')