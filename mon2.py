#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-13 15:32:19
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

class Singleton(object):
    # 单例模式写法,参考：http://ghostfromheaven.iteye.com/blog/1562618
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MongoConn(Singleton):
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

def check_connected(conn):
    #检查是否连接成功
    if not conn.connected:
        raise NameError, 'stat:connected Error'

def save(table, value):
    # 一次操作一条记录，根据‘_id’是否存在，决定插入或更新记录
    try:
        my_conn = MongoConn()
        check_connected(my_conn)
        my_conn.db[table].save(value)
    except Exception:
        print traceback.format_exc()

def insert(table, value):
    # 可以使用insert直接一次性向mongoDB插入整个列表，也可以插入单条记录，但是'_id'重复会报错
    try:
        my_conn = MongoConn()
        check_connected(my_conn)
        my_conn.db[table].insert(value, continue_on_error=True)
    except Exception:
        print traceback.format_exc()

def update(table, conditions, value, s_upsert=False, s_multi=False):
    try:
        my_conn = MongoConn()
        check_connected(my_conn)
        my_conn.db[table].update(conditions, value, upsert=s_upsert, multi=s_multi)
    except Exception:
        print traceback.format_exc()

def upsert_mary(table, datas):
    #批量更新插入，根据‘_id’更新或插入多条记录。
    #把‘_id’值不存在的记录，则插入数据库
    #如果更新的字段在mongo中不存在，则直接新增一个字段
    try:
        my_conn = MongoConn()
        check_connected(my_conn)
        bulk = my_conn.db[table].initialize_ordered_bulk_op()
        for data in datas:
            _id=data['_id']
            bulk.find({'_id': _id}).upsert().update({'$set': data})
        bulk.execute()
    except Exception:
        print traceback.format_exc()

def upsert_one(table, data):
    #更新插入，根据‘_id’更新一条记录，如果‘_id’的值不存在，则插入一条记录
    try:
        my_conn = MongoConn()
        check_connected(my_conn)
        query = {'_id': data.get('_id','')}
        if not my_conn.db[table].find_one(query):
            my_conn.db[table].insert(data)
        else:
            data.pop('_id') #删除'_id'键
            my_conn.db[table].update(query, {'$set': data})
    except Exception:
        print traceback.format_exc()

def find_one(table, value):
    #根据条件进行查询，返回一条记录
    try:
        my_conn = MongoConn()
        check_connected(my_conn)
        return my_conn.db[table].find_one(value)
    except Exception:
        print traceback.format_exc()

def find(table, value):
    #根据条件进行查询，返回所有记录
    try:
        my_conn = MongoConn()
        check_connected(my_conn)
        return my_conn.db[table].find(value)
    except Exception:
        print traceback.format_exc()

def select_colum(table, value, colum):
    #查询指定列的所有值
    try:
        my_conn = MongoConn()
        check_connected(my_conn)
        return my_conn.db[table].find(value, {colum:1})
    except Exception:
        print traceback.format_exc()


if __name__ == "__main__":
    file_path = 'testmon2.txt'#读取文本里的数再导入，数据类型为string
    company_list = []
    with open(file_path, "r") as in_file:
        for line in in_file:
            dic={}
            dic['_id']=line.split()[0]#生成的是字符串
            dic['name']=line.split()[1]
            company_list.append(dic)
    print '-'*15
    # print company_list
    # upsert_mary('myt1',company_list)#this

    datas = [
        {'_id':8, 'data':88},
        {'_id':9, 'data':99},
        {'_id':36, 'data':3366}
    ]

    #插入,'_id' 的值必须不存在，否则报错?
    #为什么没有报错，原来一个是数字8，一个是字符串8？？？
    # insert('myt1', datas)
    # #插入
    # data={'_id':6, 'data':66}
    # save('myt1',data)

    #更新数据
    # update('myt1',{'_id':8},{'$set':{'data':'888'}}, False, False)

    #更新或插入
    # data={'_id':36, 'data':'dsd'}
    # upsert_one('myt1',data)

    # #查找。相对于 select _id from myt1
    # res=select_colum('myt1',{},'_id')
    # for k in res:
    #     for key, value in k.iteritems():
    #         print key,":",value

    # #查找。相对于 select * from myt1
    # res=find('myt1',{})
    # for k in res:
    #     for key, value in k.iteritems():
    #         print key,":",value,
    #     print

    # #查找。相对于 select * from myt1 limit 1
    res=find_one('myt1',{})
    for k in res:
        print k,':',res[k]
    '''def ensure_index(table, colum):
                    #插入索引
                    try:
                        my_conn = MongoConn()
                        check_connected(my_conn)
                        return my_conn.db[table].ensureIndex({colum:-1})
                    except Exception:
                        print traceback.format_exc()

                def get_indexes(table):
                    #检索索引
                    try:
                        my_conn = MongoConn()
                        check_connected(my_conn)
                        return my_conn.db[table].getIndexes()
                    except Exception:
                        print traceback.format_exc()
                def drop_indexes(table,colum):
                    #删除索引
                    try:
                        my_conn = MongoConn()
                        check_connected(my_conn)
                        return my_conn.db[table].dropIndexes({colum})
                    except Exception:
                        print traceback.format_exc()'''