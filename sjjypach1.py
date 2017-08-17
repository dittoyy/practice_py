# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy import log
import logging
#from zhihu.items import ZhihuItem
from zhihu.items import ZhihuItem
from scrapy_redis.spiders import RedisSpider
import re
import json
import time

class BaoxianSpider(RedisSpider):       ##使用redis分布式

    name = "baoxian"
    allowed_domains = ["zhihu.com"]
    #redis_key='baoxian:start_urls'
    keywords='软件测试'                                        ###要爬的关键词
    from urllib import quote
    urlencode_keywords=quote(keywords)

    start_urls = ['https://www.zhihu.com/r/search?q='+urlencode_keywords+'&type=content&offset=0'] #'https://www.zhihu.com/r/search?q=%E4%BF%9D%E9%99%A9&type=content&offset=0'
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse,dont_filter=True)

    def parse(self, response):
        body=response.body  #{"paging":{"next":"\/r\/search?q=%E4%BF%9D%E9%99%A9&type=content&offset=50"},"htmls"
        #print body

        #获取问题链接
        question_href_reg=r'<div class=\\"title\\"><a target=\\"_blank\\" href=\\"\\/question\\/(.*?)\\"'
        all_question_href=re.findall(question_href_reg,body)
        print 'all_question_href:',all_question_href
        for aqh in all_question_href:
            question_href='https://www.zhihu.com/question/'+str(aqh)
            yield Request(url=question_href, callback=self.parse_question,dont_filter=True)
            print question_href

            log.msg("question_href:%s \n list_question_page:%s"%(question_href,response.url), level=log.INFO)
            #self.log
        #获取下一页的链接

        reg=r'{"paging":{"next":"(\\/r\\/search\?q=.*?&type=content&offset=.*?)"},"htmls"'
        next_page=re.findall(reg,body)
        print '下一页问题：',next_page
        if len(next_page):
            #print next_page[0]   #https://www.zhihu.com/r/search?q=%E4%BF%9D%E9%99%A9&type=content&offset=10
            next_page_url='https://www.zhihu.com'+ next_page[0].replace('\\','')
            print 'next_page_url:',next_page_url
            yield Request(url=next_page_url, callback=self.parse,dont_filter=True)
            log.msg("next_page_url:%s"%next_page_url, level=log.INFO)

                                           #data-type=\"Answer\"><div class=\"title\"><a target=\"_blank\" href=\"\/question\/22316395\"


    def parse_question(self,response):                             ####问题详情页面
        #print response.body

        print 'response.url:',response.url
        title=response.xpath('//h1[@class="QuestionHeader-title"]/text()').extract_first()
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print 'title:',title
        #editableDetail&quot;:&quot;，国内的保险员说风险太大，不受法律保护什么的。大神推荐我赴港买保险吗？&quot;,&quot;visitCount&quot
        reg='editableDetail&quot;:&quot;([\s\S]*?)&quot;,&quot;visitCount&quot'
        content_match=re.findall(reg,response.body)
        if  content_match:
            content=content_match[0]
        else:
            content=''               #有可能问题无具体描述
        print 'content:',content
        question={}
        question['url']=response.url
        question['title']=title

        question['content']=content
        #https://www.zhihu.com/question/19904068
        question['comment']=[]
        #https://www.zhihu.com/api/v4/questions/20214716/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccollapsed_counts%2Creviewing_comments_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.is_blocking%2Cis_blocked%2Cis_followed%2Cvoteup_count%2Cmessage_thread_token%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=3&offset=3
        answer_json='https://www.zhihu.com/api/v4/questions/'+re.findall('(\d+)',response.url)[0]+'/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccollapsed_counts%2Creviewing_comments_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.is_blocking%2Cis_blocked%2Cis_followed%2Cvoteup_count%2Cmessage_thread_token%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=0'
        print 'answer_json:',answer_json
        yield Request(url=answer_json, callback=self.parse_json,meta=question,dont_filter=False)
        """
        item=ZhihuItem()
        item['title']=question['title']
        item['url']=question['url']
        item['content']=question['content']
        yield item
        print item
        """

    def parse_json(self,response):                           ####答案列表
        meta=response.meta
        dict=json.loads(response.body)

        #print 'dict:',dict
        print 'dcit to json:',json.dumps(dict,ensure_ascii=False)
        comment_list=meta['comment']
        for data  in  dict['data']:                    # dict['data']是列表，每个元素是字典
            try:
                comment_dict={}
                comment_dict['comment_content']=data['content']
                if data['author']['name']:
                    comment_dict['author']=data['author']['name']
                else:
                    comment_dict['author']=''
                comment_dict['voteup_count']=data['voteup_count']
                comment_dict['comment_count']=data['comment_count']
                comment_dict['comment_time']=time.strftime('%Y-%m-%d',time.localtime(data['created_time']))
                comment_list.append(comment_dict)
            except Exception,e:
                print e
        meta['comment']=comment_list
        meta['answer_num']=dict['paging']['totals']



        if dict['paging']['is_end']==False:             ###自动翻页
            yield Request(url=dict['paging']['next'], callback=self.parse_json,meta=meta,dont_filter=False)
        else:
            #log.msg("last:%s"%next_page_url, level=log.INFO)
            print 'last:',meta['title'],meta['url'] ,meta['content'],meta['answer_num'],len(meta['comment'])#,meta['comment']
            item=ZhihuItem()
            item['title']=meta['title']
            item['url']=meta['url']
            item['content']=meta['content']
            item['answer_num']=meta['answer_num']
            item['comment']=meta['comment']
            yield item