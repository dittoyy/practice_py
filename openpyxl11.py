#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-10 14:33:38
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$

import requests
from openpyxl import Workbook

if __name__ == "__main__":
    print "爬取豆瓣网书籍数据写入excel示例"

    # 通过豆瓣网搜索API，搜索python关键词，采集书籍数据
    # 本示例只采集第一页的数据
    url = "https://api.douban.com/v2/book/search?q=python"
    response = requests.get(url).text
    # print response
    response=eval(response)#将string转换成dict

    # 构建一个Workbook对象
    wb = Workbook()    # 激活第一个sheet
    ws = wb.active    # 写入表头
    ws.append(["书名", "作者", "描述", "出版社", "价格"])

    # 写入书信息
    for book in response["books"]:
        ws.append([book["title"],
            ",".join(book["author"]),
            book["summary"],
            book["publisher"],
            book["price"]])

    # 保存
    wb.save("ebook.xlsx")
