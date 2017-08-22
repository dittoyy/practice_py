#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-24 14:32:06
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$
import allure
@pytest.allure.testcase("http://www.qq.com")

def test_steps_demo(self):

    with pytest.allure.step('step one'):

        driver = webdriver.Chrome()

        driver.get('http://www.baidu.com')

    with pytest.allure.step('step two'):

        driver.find_element_by_id('kw').send_keys('hello')

        driver.find_element_by_id('su').click()

        time.sleep(5)

    with pytest.allure.step('step three'):

        driver.save_screenshot("b.png")

        f = open('./b.png','rb').read()

        allure.attach('this is a img',f,allure.attach_type.PNG)

    with pytest.allure.step('step four'):
        time.sleep(2)

    allure.attach('this is a attach','llllllll llllll aaaaa')
    f = open('./b.png','rb').read()
    allure.attach('this is a img',f,allure.attach_type.PNG)
    allure.environment(report='Allure report',browser='chrome',version='1.0')
@allure.feature('Feature1')
@allure.story('Story1')
def test_mminor():

    assert False