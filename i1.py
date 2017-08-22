#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-26 13:40:18
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$
from functools import wraps
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com')
# builder = ActionChains(driver)
# builder.key_down(Keys.F12).perform()
# sleep(5)
def highlight(func):

    def apply_style(element):
        js = "arguments[0].style.border='6px solid red'"

        # 实现的方式很简单，就是定位到元素后，执行js样式
        driver.execute_script(js, element)

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        element = func(self, *args, **kwargs)

        apply_style(element)
        return element

    return wrapper

def screenshot(func):

    def screen_shot(screen_name):
        driver.save_screenshot(screen_name)

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        element = func(self, *args, **kwargs)

        screen_shot(str(args[-1]) + '.jpg') # 默认是以定位元素属性为文件名
        return element


    return wrapper
class Action(object):
    def __init__(self, driver):
        self.driver = driver

    @screenshot
    @highlight
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            return e
# def highlight(element, element_name=None, debug=True):
#         '''
#         debug 参数用来开关截图功能
#         '''
#     def apply_style():
#         driver.execute_script("arguments[0].style.border='6px solid red'", element)


#     def screen_shot(screen_name):
#         driver.save_screenshot(screen_name)

#     if debug:
#         try:
#             screen_shot(str(element_name) + '_before.jpg')
#             apply_style()
#             screen_shot(str(element_name) + '_after.jpg')
#         except Exception as e:
#             return e

#     apply_style()

# #  使用也很简单
# element = driver.find_element(By.ID, 'kw')
# highlight(element, 'kw')


driver = webdriver.Firefox()

driver.get('http://www.baidu.com')

action = Action(driver)

action.find_element(By.ID, 'kw')
time.sleep(3)
# driver.quit()
# from selenium import webdriver
# # 引入 Keys 模块
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")

# # 输入框输入内容
# driver.find_element_by_id("kw").send_keys("seleniumm")

# # 删除多输入的一个 m
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)


# # 输入空格键+“教程”
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)
# driver.find_element_by_id("kw").send_keys("教程")

# # ctrl+a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# # ctrl+x 剪切输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# ctrl+v 粘贴内容到输入框
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# 通过回车键来代替单击操作
# driver.find_element_by_id("su").send_keys(Keys.F12)
# driver.quit()

# 需要说明的是， 上面的脚本没有什么实际意义， 仅向我们展示模拟键盘各种按键与组合键的用法。

# from selenium.webdriver.common.keys import Keys
# 在使用键盘按键方法前需要先导入 keys 类。


'''
以下为常用的键盘操作：

send_keys(Keys.BACK_SPACE) 删除键（BackSpace）

send_keys(Keys.SPACE) 空格键(Space)

send_keys(Keys.TAB) 制表键(Tab)

send_keys(Keys.ESCAPE) 回退键（Esc）

send_keys(Keys.ENTER) 回车键（Enter）

send_keys(Keys.CONTROL,‘a’) 全选（Ctrl+A）

send_keys(Keys.CONTROL,‘c’) 复制（Ctrl+C）

send_keys(Keys.CONTROL,‘x’) 剪切（Ctrl+X）

send_keys(Keys.CONTROL,‘v’) 粘贴（Ctrl+V）

send_keys(Keys.F1) 键盘 F1

……

send_keys(Keys.F12) 键盘 F12
'''