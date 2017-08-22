# -*- coding: utf-8 -*-
# from selenium import webdriver
# from time import sleep


# mobileEmulation = {'deviceName': 'Apple iPhone 4'}
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")#设置为 headless 模式
# options.add_argument("--window-size=100,100")#设置窗口大小
# options.add_experimental_option('mobileEmulation', mobileEmulation)

# driver = webdriver.Chrome(chrome_options=options)

# driver.get('http://m.baidu.com')

# sleep(3)
# driver.close()



# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://m.baidu.com')

# sleep(3)
# driver.close()