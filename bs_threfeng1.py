#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 11:02:39
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$

import requests,json,random
import re,threading,time
from lxml import etree

lock=threading.Lock()
semaphore=threading.Semaphore(100)   ###每次限制只能100线程

user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" ,\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
count=0

def sina(page_url):    ##列表页
    if semaphore.acquire():
        header={}

        header['User-Agent']=random.choice(user_agent_list)
        header.update({
            "Host":"platform.sina.com.cn",

            #"Cookie":"global_cookie=fb1g6d0w64d2cmu86sv4g9n3va0j137sk48; vh_newhouse=3_1491312022_2816%5B%3A%7C%40%7C%3A%5D833300ee3177d88529c7aa418942ece9; newhouse_user_guid=2F163DE7-8201-7FA9-2FB6-E507FE6F03B1; SoufunSessionID_Esf=3_1495389730_232; sf_source=; s=; showAdsh=1; hlist_xfadhq_SZ=0%7c2017%2f5%2f25+1%3a21%3a47%7c; city=sz; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; logGuid=a768dd46-b85b-47f4-a7a0-0a6596cab4cd; __utma=147393320.1111837171.1491290389.1495646208.1495650134.9; __utmb=147393320.12.10.1495650134; __utmc=147393320; __utmz=147393320.1495650134.9.4.utmcsr=esf.sz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; unique_cookie=U_cqyov4ut5vv1al8e2858qhzgt17j2z06mph*14"
            })
        while(1):
            content=''
            try:
                content=requests.get(page_url,headers=header,timeout=5).content

            except Exception as e:
                print e
            if content!='':
                break




        jsona=re.findall('jQuery191012358189839869738_1495880348059\(([\s\S]*?"}]}})',content)[0]
        #print jsona
        dict= json.loads(jsona)
        #print type(dict)
        #print dict
        #print dict['result']['data']
        for l in dict['result']['data']:
            title= l['title']
            url= l['url']
            biaoqian=get_biaoqian(url)

            lock.acquire()
            global count
            count+=1
            print time.strftime('%H:%M:%S',time.localtime(time.time())),'    ',count
            print '列表页：'
            print ' title: %s\n url: %s'%(title,url)

            print '详情页:'
            print ' biaoqian: %s \n'%(biaoqian)
            print '**************************************************************'
            lock.release()

        semaphore.release()



def get_biaoqian(url):    ###新闻页，爬取标签

    header={'User-Agent':random.choice(user_agent_list)}
    header.update({"Host":"mil.news.sina.com.cn"})

    while(1):
        content=''
        try:
            content=requests.get(url,headers=header,timeout=10).content
        except Exception as  e:
            #print e
            pass
        if content!='':
            break


    se=etree.HTML(content)
    #print etree.tounicode(se)
    biaoqian=se.xpath('//p[@class="art_keywords"]/a/text()')
    return  ' '.join(biaoqian)




def singe_req():
    for i in range(1,301):
        page_url='http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=lishi&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page=%s&show_num=10&callback=jQuery191012358189839869738_1495880348059&_=1495880348069'%i
        sina(page_url)
    print 'over'

def threading_red():
    threads=[]
    for i in range(1,301):
        t=threading.Thread(target=sina,args=('http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=lishi&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page=%s&show_num=10&callback=jQuery191012358189839869738_1495880348059&_=1495880348069'%i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print 'over'

def  muiltiprocessing_req():
    import multiprocessing
    pool = multiprocessing.Pool(100)
    #pool = multiprocessing.Pool(multiprocessing.cpu_count())

    pool.map(sina, ['http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=lishi&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page=%s&show_num=10&callback=jQuery191012358189839869738_1495880348059&_=1495880348069'%i for i in range(1,301)])
    pool.close()
    pool.join()
    print 'over'

def gevent_req():
    ######################利用pool######################
    from gevent import monkey
    from gevent.pool import Pool

    monkey.patch_all()
    pool = Pool(100)
    data= pool.map(sina, ['http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=lishi&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page=%s&show_num=10&callback=jQuery191012358189839869738_1495880348059&_=1495880348069'%i for i in range(1,301)])
    print 'over'

if __name__=='__main__':
    pass
    singe_req()                     ##单线程
    #threading_red()                  ###多线程
    #muiltiprocessing_req()             ####多进程
    #gevent_req()                      ##协程
