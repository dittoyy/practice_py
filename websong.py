#coding:utf-8
__Author__='dido'

import web
urls=(#定义的网站路由：把请求映射到某一个类方法来处理
'/qiangzi','Qiangzi',
'/','Index',
'/psb\.jpg','Psb',
'/s','Se'
    )
render=web.template.render('templates')


class Qiangzi(object):
    """docstring for Qiangzi"""
    def GET(self):
        return render.index()
    def POST():
        pass
class Index(object):
    """docstring for index"""
    def GET(self):
        return render.abc123()
class Psb(object):
    """docstring for Psb"""
    def GET(self):
        return open('psb.jpg','rb').read()
class Search:
    def GET(self):
        i=web.input()#获取用户请求的数据
        name=i.get('name',None)
        songurl,picurl=get_url.getData(name)
        # return songname,picurl
        return render.abc123(songurl,picurl)

if __name__ == '__main__':
    web.application(urls,globals()).run()
