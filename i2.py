# coding:utf-8
import unittest

# ================================================
def setUpModule():
    print 'test module start.........'

def tearDownModule():
    print 'test module end.........'

# setUpModule/tearDownModule在整个测试文件开始结束时被执行
# =================================================

# -------------------------------------------------

class Test(unittest.TestCase):
    # 修饰器
    @classmethod
    def setUpClass(cls):
        print 'test class start,,,,,,,,'

    # 修饰器
    @classmethod
    def tearDownClass(cls):
        print 'test class end ,,,,,,,,'
# setUpClass/tearDownClass在整个测试类的开始结束时被执行
# -------------------------------------------------


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def setUp(self):
        print 'test case start >>>>>>>>'

    def tearDown(self):
        print 'test case end >>>>>>>>>>'

# setUp/tearDown在每个测试用例的开始和结束时被执行
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


    def test_case1(self):
        print 'test case1'

    def test_case2(self):
        print 'test case2'
if __name__ == '__main__':
    unittest.main()