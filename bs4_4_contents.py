# coding:utf-8
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.cnblogs.com/yoyoketang/mvc/blog/sidecolumn.aspx?blogApp=yoyoketang")
# 请求首页后获取整个html界面
blog = r.content
# 用html.parser解析html
soup = BeautifulSoup(blog, "html.parser")
tag_soup = soup.find(class_="catListTag")
print tag_soup

# print body.prettify()
print "..........................."
ul_soup = tag_soup.find_all("a")
print ul_soup
print "..........................."

for i in ul_soup:
    print i.string
