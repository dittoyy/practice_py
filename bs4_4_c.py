# coding:utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.cnblogs.com/yoyoketang/")
# 请求首页后获取整个html界面
blog = r.content
# 用html.parser解析html
soup = BeautifulSoup(blog, "html.parser")
# find方法查找页面上第一个属性匹配的tag对象
tag_soup = soup.find(class_="c_b_p_desc")
# len函数获取子节点的个数
print len(tag_soup.contents)
# 循环打印出子节点
for i in tag_soup.contents:
    print i

# # 通过下标取出第1个string子节点
# print tag_soup.contents[0]
# # 通过下标取出第2个a子节点
# print tag_soup.contents[1]
#
#

'''contents可以改为children节点，string 也算一个子节点，但是只可以for循环读取
contens和children只能读取第一代不能读取总的后代
descendants是generator没有len'''

chi=tag_soup.children
print chi
# print list(chi)
# print len(list(chi))

for x in chi:
    print x



print '.........................'
des=tag_soup.descendants
print des
# print list(des)
# print len(list(des))

for i in des:
    print i
