# coding:utf-8
from common.yoyo_selenium import Yoyo
retrieve_url = "https://passport.cnblogs.com/GetUsername.aspx"
import sys
sys.path.append(r'D:\yoyo\yoyo')
class RetrievePage(Yoyo):
    # 定位器，定位页面元素
    email_input_loc = ("id", "txt_email")  # 输入账号
    authen_input_loc = ("id", 'txt_authen_code')
    submit_button_loc = ("class", 'btn_submit')

    def input_email(self, text):
        self.send_keys(self.email_input_loc, text)

    def input_authen(self, text):
        self.send_keys(self.authen_input_loc, text)

    def submit_button(self):
        self.click(self.submit_button_loc)

if __name__ == "__main__":
    dr = RetrievePage()
    dr.input_email("xxx")
    dr.input_authen("xxx1111")
    dr.submit_button()
