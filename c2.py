# -*- coding: utf-8 -*-

# from selenium import webdriver
# from time import sleep


# options = webdriver.ChromeOptions()
# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
# options.add_experimental_option('prefs', prefs)

# driver = webdriver.Chrome(chrome_options=options)
# driver.get('http://sahitest.com/demo/saveAs.htm')
# driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
# sleep(3)
# driver.quit()


# # -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', 'd:\\')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

driver = webdriver.Firefox(firefox_profile=profile)

driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
sleep(3)
# driver.quit()