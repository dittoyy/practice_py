from testtools import TestCase


class TestLearnTesttools(TestCase):

    def setUp(self):
        super(TestLearnTesttools, self).setUp()
        print "this is setUp"

    def test_case_1(self):
        self.assertIn('a', 'cat')

    def test_case_2(self):
        assert 2 == 3

    def tearDown(self):
        super(TestLearnTesttools, self).tearDown()
        print "this is tearDown"

    @classmethod
    def setUpClass(cls):
        print "this is setUp class"