# import nose

# class TestBar(object):

#     @nose.allure.severity(nose.allure.severity_level.CRITICAL)
#     def test_bar(self):
#         pass

#     # custom severity
#     @nose.allure.severity("hard")
#     def test_bar(self):
#         pass


import nose,sys
from selenium import webdriver
from allure.constants import AttachmentType

class TestBar():

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://www.baidu.com")

    @nose.allure.severity(nose.allure.severity_level.CRITICAL)
    def test_bar(self):
        assert 1==2
        nose.allure.attach('screenshot',self.driver.get_screenshot_as_png(), type= AttachmentType.PNG)

    # custom severity
    @nose.allure.severity("hard")
    def test_bar_xx(self):
        assert 4==4
        #nose.allure.attach('screenshot', self.driver.get_screenshot_as_png(), type='png')   -----该方法错误
        # nose.allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    def tearDown(self):
        if sys.exc_info()[0]:
            nose.allure.attach('screenshot',self.driver.get_screenshot_as_png(), type= AttachmentType.PNG)
