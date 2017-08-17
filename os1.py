import os
case_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'case')
print case_dir
print __file__
print os.path.realpath(__file__)
print os.path.isfile(__file__)
print os.path.getsize(__file__)
print os.path.split(__file__)[0]
print os.stat(__file__)
print os.path.getmtime(__file__)
print os.curdir
print os.getcwd()
print os.path.dirname(__file__)
print os.path.abspath(__file__)
print os.listdir(os.path.dirname(__file__))

lists = os.listdir(os.path.dirname(__file__))
lists.sort(key=lambda fn: os.path.getmtime(os.path.join(os.path.dirname(__file__), fn)))
print lists
w=os.walk(__file__)
print w

# def walk_dir(target_dir):

#     walk_result = os.walk(target_dir)
#     # print(type(walk_result))


#     for root, dirs, files in walk_result:
#         # print(type(root), type(dirs), type(files))
#         print("-" , root)

#         for name in dirs:
#             print(" --", name)

#         for name in files:
#             print(" --", name)

# if __name__ == "__main__":
    # for root,dirs,files in os.walk(os.curdir):
    #     print root,'\n',dirs,'\n',files
    #     for dir in dirs:
    #         print dir
    #     for file in files:
    #         print file
    # target_dir = os.curdir
    # walk_dir(target_dir)
# for i in w:
#     print
# import unittest
# def all_case():
#     testcase=unittest.TestSuite()
#     discover=unittest.defaultTestLoader.discover(
#         case_dir,pattern='test*.py',top_level_dir=None)
#     for test_suite in discover:
#         for test_case in test_suite:
#             testcase.addTests(test_case)
#     print testcase
#     return testcase
# @unittest.skipped('skipmsg')
# def test_skip1():
#     pass

# if __name__ == '__main__':
#     runner=unittest.TextRunner()
#     runner.run(all_case())
#     r1=unittest.TextRunner(verbosity=2).run(testcase)
#     print r1.testsRun
#     print r1.failure
#     print r1.error
#     print r1.skipped