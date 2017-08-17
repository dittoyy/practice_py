#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 15:57:25
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$

class Zhima(object):

    get_proxy_url=''
    check_http_url='http://www.ip.cn '
    check_https_url ='https://www.baidu.com '
    def get_proxies(self):
        while(1):
            try:
                resp=requests.get(self.get_proxy_url)
                break
            except Exception ,e:
                logger.warning('从芝麻代理获取代理错误： %s'%str(e))
                time.sleep(3)

        dictx = json.loads(resp.content)

        thread_pool = threadpool.ThreadPool(50)
        prs=[{"http": "http://%s:%s " % (i['ip'], i['port'])} for i in dictx['data']]
        requestsx = threadpool.makeRequests(self.check_proxy, prs)
        [thread_pool.putRequest(req) for req in requestsx]
        thread_pool.wait()

    def check_proxy(self,pr):

        try:
            if 'http' in pr:
                if requests.get(self.check_http_url, proxies=pr, timeout=10).status_code == 200:
                    r.sadd('http_proxies', pr)
            if 'https' in pr:
                if requests.get(self.check_https_url, proxies=pr, timeout=10).status_code == 200:
                    r.sadd('https_proxies', pr)
        except Exception, e:
            logger.warning('检测代理ip不可用： %s' % str(e))

