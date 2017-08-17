# coding:utf-8
import time
from uniqlo_login import *
import sys,random
sys.path.append(r'D:\template\template1')
from common.selenium_pack1 import *
from uniqlo_login_success_main import *
main_url = "http://uniqlotest.r-pac.com.hk"

class PlaceOrder(Seleniumpack1):
    # 定位器，定位页面元素
    Addressbook=('css selector','.passaddressDropdown')

    import random
    text_menu=('css selector','inner_main_div')
    order_url='http://uniqlotest.r-pac.com.hk/order/catalog/new'
    select_address=('id','addressDropdown')
    view_address=('name','editAddress')
    select_pl=('id','printShopId')
    file_input=('css selector','input[title="file input"]')#2个file
    file_input1=('xpath','//tr[2]/td[2]/div/div/div[3]/input')
    file_input2=('xpath','//tr[3]/td[2]/div/div/div[3]/input')

    span_file=('css selector','.qq-upload-file')#2个file的title有显示,错误的有错误的颜色
    comfirm=('css selector','.sub')#2个Confirm
    confirm1=('css selector','li .sub')
    confirm2=('css selector','input.sub')

    dialog_msg=('css selector','.qq-dialog-message-selector')

    menu_bar=('css selector','div div:nth-child(2) a')#按数来取

    file_retry=('css selector','.qq-upload-retry')
    file_cancel=('css selector','.qq-upload-cancel')#$('.qq-upload-cancel')[0].click()

    unfile=('css selector','.qq-alert-dialog-selector .qq-cancel-button-selector:eq(1)')
    #$('.qq-alert-dialog-selector .qq-cancel-button-selector:eq(1)').click()

    jqmsg=('css selector','.jqimessage')#每次弹窗都是他们三，但是变的是title
    jqok=('css selector','.jqibutton')
    jqno=('css selector','.jqiclose')

    # for (var i in $('.menu_bt a')){console.log($('.menu_bt a')[i].text)}
    # $('#printShopId option').length

    add_options=('css selector','.addressDropdown option')
    pl_options=('css selector','#printShopId option')

    def se_add(self):
        '''1选地址'''
        le=random.randint(0,self.leth(self.add_options)-1)
        print le
        self.select_by_index(self.select_address,le)
    def se_pl(self):
        '''2选productionlocation'''
        le=random.randint(0,self.leth(self.pl_options)-1)
        print le
        self.select_by_index(self.select_pl,le)
    def send_file1(self,file1):
        '''3传文件pofile'''
        self.send_keys(self.file_input1,file2)
    def send_file2(self,file2):
        '''4传mtfile'''
        self.send_keys(self.file_input2,file2)
    def send_files(self,*files):
        '''一次传多个文件
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(“Id”))
         is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).
         until_not(lambda x: x.find_element_by_id(“someId”).is_displayed())
         until(method, message=’’)
        调用该方法提供的驱动程序作为一个参数，直到返回值不为 False
        *可以通过(*args)打开
        '''
        # result=WebDriverWait(self.driver, timeout, 1).until(lambda x:self.send_file1(x))
        # self.send_keys(files)
        pass
        #

    def confirm_order(self):
        '''5点confirm'''
        # self.click(self.comfirm1)#一样的
        self.click(self.confirm2)
    # def place_order(self,file1,file2):
    #     '''下单该填的都填好'''
    #     self.se_add()
    #     self.se_pl()
    #     self.send_file1(file1)
    #     import time
    #     time.sleep(3)
    #     self.send_file2(file2)
    #     self.confirm_order()
    def switch_another(self,menubar):
        '''跳到新的界面去'''
        self.click(self.menubar)
    def miss_some(self):
        '''有些每填然后就confirmm'''
        self.confirm_order()
    def jqi_ok(self):
        '''js弹出处理ok'''
        # js_ok='document.getElementById("jqibutton").click()'

        jq_msg="$(self.jqmsg).text()"
        jq_ok="$(self.jqok).click()"
        print self.js_execute(jq_msg)
        self.js_execute(jq_ok)

    def jqi_no(self):
        '''js弹出处理no'''
        # js_ok='document.getElementById("jqibutton").click()'
        # print jq_msg="$(self.jqmsg).text()"
        jq_no="$(self.jqno).click()"
        self.js_execute(jq_no)

    def jqi_retry(self):
        '''js文件失败处理retry'''
        # js_ok='document.getElementById("jqibutton").click()'
        jq_text1="$(self.file_retry).text()"
        print self.js_execute(jq_text2)
        jq_retry="$(self.file_retry).click()"
        self.js_execute(jq_retry)
    def jqi_cancel(self):
        '''js文件失败处理cancel'''
        # js_ok='document.getElementById("jqibutton").click()'
        jq_text2="$(self.file_cancel).text()"
        jq_cancel="$(self.file_cancel).click()"
        print self.js_execute(jq_text2)
        self.js_execute(jq_cancel)



    def alert_jqi(self):
        '''弹窗选择ok /no'''
        pass

if __name__ == '__main__':
    s=browser()#一个browser()就会打开一次，每次的browser()不同，so///
    blog1=LoginPage(s)
    blog1.open(main_url,'Main')
    blog1.login('admin','test1104')
    blog2=LoginSuccessMain(s)
    blog2.to_order()

    file1=r'C:\Users\ditto.he\Desktop\uniqlo\PO 05327F002B KR-1 (66) 06.15 WH  05.22 ETD (6576pcs) 02.03.2017.xls'
    file2=r'C:\Users\ditto.he\Desktop\uniqlo\MaterialAndTrimSheet_05327F002B_KR 03.03.2017.xls'
    # blog3.place_order(file1,file2)
    blog3=PlaceOrder(s)
    # blog3.se_add()
    # blog3.se_pl()
    blog3.send_file1(file1)
    import time
    time.sleep(3)
    blog3.send_file1(file2)
    blog3.confirm_order()
    # blog3.logout()




