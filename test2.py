#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average((20, 30, 70))
    40
    >>> print average((2, 30, 70))
    40
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试
import unittest

# class TestStatisticalFunctions(unittest.TestCase):

#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         self.assertRaises(ZeroDivisionError, average, [])
#         self.assertRaises(TypeError, average, 20, 30, 70)

# unittest.main() # Calling from the command line invokes all tests

import unittest

class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        print d
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertIn('key', d,'fuckoff')
        self.assertIn(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
            print value

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            # print value
unittest.main()