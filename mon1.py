#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-13 14:04:21
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$

# -*- coding: utf-8 -*-
import pymongo
import sys
import traceback

MONGODB_CONFIG = {
    'host': '127.0.0.1',
    'port': 27017,
    'db_name': 'test',
    'username': None,
    'password': None
}

class MongoConn(object):

    def __init__(self):
        # connect db
        try:
            self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
            self.db = self.conn[MONGODB_CONFIG['db_name']]  # connect db
            self.username=MONGODB_CONFIG['username']
            self.password=MONGODB_CONFIG['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True
        except Exception:
            # print traceback.format_exc()
            print 'Connect Statics Database Fail.'
            sys.exit(1)


if __name__ == "__main__":
    my_conn = MongoConn()
    # datas = [
    #     # #set _id with number
    #     # #是int32 int32
    #     {'_id':1, 'data':12},
    #     {'_id':2, 'data':22},
    #     {'_id':3, 'data':'cc'}
    #     # {'data':12},
    #     # {'data':22},
    #     # {'data':'cc'}
    # ]

    '''
    js里是这样的哈~
    js = 'for(var i=0;i<=1000;i++){db.my1test1.insert({'_id':i,'js1':'js'+i,$inc:{'age':i}})}'
    js1="for(var i=0;i<=100;i++){db.my1test1.update({'_id':i},{$inc:{'age':i}},true)}"'''
    # js循环插入数据
    # for i in  range(1000000):
    # db.my_collection.insert({"test":"tnt","index":i})

    '''#变成python是这样的
                for i in  range(1000):
                    my_conn.db.my1test1.insert({'_id':i,'js1':'js'+str(i),$inc:{'age':i}})
                    #这是最开始插入数据搞不懂为啥不可以像上面那样$inc'''

    # for i in  range(1000):
    #     my_conn.db.my1test1.update({'_id':i},{'$inc':{'age':i}},True)
    #插入数据，'mytest'是上文中创建的表名
    # my_conn.db['my1test'].insert(datas)

    import time
    start = time.time()

    #查询数据，'my1test'是上文中创建的表名
    res=my_conn.db['my1test1'].find({})
    for k in res:
        print k

    end=time.time()
    cost_time=end-start#处理时间

    print my_conn.db['my1test1'].find().count()


