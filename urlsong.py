#coding:utf-8

import urllib,json,sys
print sys.stdin.encoding

def getData(name):
    name=urllib.quote(name.decode('gbk').encode('utf-8'))
    #传递中文参数给URL,UTF-8的URL编码
    html=urllib.urlopen('http://music.163.com/#/search/m/?s=%s&type=1'%name).read()
    print html
    dict=json.loads(html)
    songname=dict['result']['songs'][0]['audio']
    picurl=dict['result']['songs'][0]['album']['picUrl']
    return songname,picurl
if __name__ == '__main__':
    print getData('海阔天空')
