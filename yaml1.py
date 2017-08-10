# -*- coding: utf-8 -*-

import yaml

'''yaml
load-str-dict
dump-dict-str
load_all()
dump_all()
- - -
字符串
整型
浮点型
布尔型
null
时间
日期
'''

yaml_str = """
name: 媛媛
age: 0
job: Tester
"""
y = yaml.load(yaml_str)
print y


python_obj = {"name": u"媛媛",
              "age": 0,
              "job": "Tester"
              }
y = yaml.dump(python_obj, default_flow_style=False)
print y
# a = ['中文', 'ab']
# print str(a).decode('string_escape')//change list to chinese
# print str(python_obj).decode('string_escape')

#未分段
# y = yaml.load(file('test.yaml', 'r'))
# print y


#分段---读取
ys = yaml.load_all(file('test.yaml', 'r'))
for y in ys:
    print y

# dump_all,写入
# obj1 = {"name": "James", "age": 20}
# obj2 = ["Lily", 19]

# with open('test1.yaml', 'w') as f:
#     yaml.dump_all([obj1, obj2], f)


# dump() 和 dump_all() 方法可以传入列表，
# 也可以传入一个可序列化生成器，如 range(10)
y = yaml.dump(range(10))
print y