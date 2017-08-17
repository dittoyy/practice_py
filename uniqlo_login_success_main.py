# coding:utf-8
import time
from uniqlo_login import *
import sys
sys.path.append(r'D:\template\template1')
from common.selenium_pack1 import *
main_url = "http://uniqlotest.r-pac.com.hk"

class LoginSuccessMain(Seleniumpack1):
    # 定位器，定位页面元素
    place_order =('xpath',"//*[contains(text(),'Place an Order')]")
    check_order =('xpath',"//*[contains(text(),'Check Order Status')]")

    nav_main =('xpath',"//*[contains(text(),'Main')]")
    nav_addressbook =('xpath',"//*[contains(text(),'Address Book')]")
    nav_master =('xpath',"//*[contains(text(),'Master')]")
    nav_access =('xpath',"//*[contains(text(),'Help')]")
    nav_help =('xpath',"//*[contains(text(),'Access')]")

    nav_all =('css selector','.menu_bt')
    nav_current =('class name','.menu_bt_current')

    user_name=('css selector','td.user_text')


    log_out=('css selector','td a[href="/logout"]')
    rpac=('css selector','td a[title="About r-pac"]')
    # cookie1={'name':'uid','value':'1'}
    # cookie2={'name':'displayname','value':'Administrator'}
    # auth:BE8F0D3FA5CAD5B23166BDA7625235C16A42380505446CF69CFF98DBEC747861AF813692E3AFC01BD8162363B2DE63CFAF801002CBF91CEEF3C3BC25CDEA4AEA193025BE484B077945B5876C76E39F9FB5A2268E8B9B806D800DA2A0E7BB3DF8939892C7CB8E99553E05C4698629E1A4D034A1C54FE0EE8C7284AA2F5708A44EE2FAFFA9FDB1E46A1E73059016EC9BCA37239AB04F27C813D077232F9021DB6AEDC41777599249933929214780CF003DCCCB5C1B8DD59152BF27226C9F9421361D6FDF399CD7FE03500C18793ADE43EAF997D3671D135A166913F6BACC039A140E9536A20FB2CA764B2CF2DBA79CEC86EBC81D3FFCAEDCDAD3CD21C1A1AA9D87F05F7B2071251F5155E12A9B3C82EC1CCAD61FE3BE2D1CB19584E8ACB5373DBE71C3DDAAF8622CBF3206AAF492C9439C3A566EC9CCA46ABDED0B9FD28321B99E22CB2F303F519CD5A38192D21D01E1CB4E7BDA42EF8A3F6DA0CE3F36040AB11D6B7EF9BAF9ADE1E18173D197BCA19EE67A0738726EB58760E3C7CA8F46F5B98FBA72E34794D4DF114304694ADF7E8CB3C2224212C61E8B21318E4D040C915FBC365866FE05F607138AA35FE99F00F2FF987D27DFDBF40230A131F575300ECE5C1068FAF31651E324B750E6C9347B622168C81FE2030FDA45CD6DF0C6AEB061395E8067A3714BB36539FBD6EA00E78C84)
    # def cookiein(cookie1,cookie2):
    #     driver.add_cookie(cookie1)
    #     driver.add_cookie(cookie2)
    #     driver.refresh()

    def  findNavAll(self,nav_all):
        '''选择全部nav'''
        finda=self.find_elements(self.nav_all)
        for x in len(finda):
            time.sleep(2)
            print x
            self.click(finda[x])

    def to_order(self):
        '''去下单'''
        self.click(self.place_order)

    def to_status(self):
        '''status'''
        self.click(self.check_order)



    def logined(self):
        '''检查登陆名字，来check登陆账号正确'''
        self.is_text_in_element(rpac,"Administrator")

    def rpaccom(self):
        '''去rpac公司了'''
        self.click(self.rpac)

    def to_access(self):
        '''去access界面'''
        self.click(self.nav_access)
    def to_master(self):
        '''去master界面'''
        self.click(self.nav_master)
    def to_help(self):
        '''去help界面'''
        self.click(self.nav_help)
    def to_address(self):
        '''去addressbook界面'''
        self.click(self.nav_addressbook)
    def logout(self):
        self.click(self.log_out)
if __name__ == '__main__':
    s=browser()#一个browser()就会打开一次，每次的browser()不同，so///
    blog2=LoginPage(s)
    blog2.open(main_url,'Main')
    blog2.login('admin','test1104')
    blog3=LoginSuccessMain(s)

    # blog3.logout()




