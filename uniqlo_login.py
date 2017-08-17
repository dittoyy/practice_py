# coding:utf-8
import sys
sys.path.append(r'D:\template\template1')
from common.selenium_pack1 import *
login_url = "http://uniqlotest.r-pac.com.hk/login?ReturnUrl=%2f"

class LoginPage(Seleniumpack1):
    # 定位器，定位页面元素
    username_loc = ("id", 'Username')  # 输入账号
    password_loc = ("id", 'Password')
    submit_loc = ("id", 'btn_login')




    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        '''输入密码框'''
        self.send_keys(self.password_loc, password)

    def click_submit(self):
        '''登录按钮'''
        self.click(self.submit_loc)

    def login(self, username, password):
        '''登录方法'''
        self.input_username(username)
        self.input_password(password)
        self.click_submit()

    def cookiein(self,s,cookie1,cookie2):
        '''cookies登陆'''
        print s.get_cookies()
        s.add_cookie(cookie1)
        s.add_cookie(cookie2)
        import time
        time.sleep(2)
        s.refresh()
        print s.get_cookies()

if __name__ == '__main__':
    s=browser('phantomjs')
    blog1=LoginPage(s)
    blog1.open(login_url,'r-pac & Uniqlo')
    # print s.get_cookies()
    # blog1.login('admin','test1104')
    cookie1={'name':'user','value':'uid=1&displayname=Administrator'}
    cookie2={'name':'auth','value':'BE8F0D3FA5CAD5B23166BDA7625235C16A42380505446CF69CFF98DBEC747861AF813692E3AFC01BD8162363B2DE63CFAF801002CBF91CEEF3C3BC25CDEA4AEA193025BE484B077945B5876C76E39F9FB5A2268E8B9B806D800DA2A0E7BB3DF8939892C7CB8E99553E05C4698629E1A4D034A1C54FE0EE8C7284AA2F5708A44EE2FAFFA9FDB1E46A1E73059016EC9BCA37239AB04F27C813D077232F9021DB6AEDC41777599249933929214780CF003DCCCB5C1B8DD59152BF27226C9F9421361D6FDF399CD7FE03500C18793ADE43EAF997D3671D135A166913F6BACC039A140E9536A20FB2CA764B2CF2DBA79CEC86EBC81D3FFCAEDCDAD3CD21C1A1AA9D87F05F7B2071251F5155E12A9B3C82EC1CCAD61FE3BE2D1CB19584E8ACB5373DBE71C3DDAAF8622CBF3206AAF492C9439C3A566EC9CCA46ABDED0B9FD28321B99E22CB2F303F519CD5A38192D21D01E1CB4E7BDA42EF8A3F6DA0CE3F36040AB11D6B7EF9BAF9ADE1E18173D197BCA19EE67A0738726EB58760E3C7CA8F46F5B98FBA72E34794D4DF114304694ADF7E8CB3C2224212C61E8B21318E4D040C915FBC365866FE05F607138AA35FE99F00F2FF987D27DFDBF40230A131F575300ECE5C1068FAF31651E324B750E6C9347B622168C81FE2030FDA45CD6DF0C6AEB061395E8067A3714BB36539FBD6EA00E78C84'}
    # u'value': u'uid=1&displayname=Administrator'
    blog1.cookiein(s,cookie1,cookie2)
    # print s.get_cookies()