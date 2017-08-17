#coding:utf-8
import urllib,re,MySQLdb
def getList(page):
    html=urllib.urlopen('http://www.ygdy8.net/html/gndy/dyzz/list_23_%d.html'%page)
    text=html.read()
    text=text.decode('gbk').encode('utf-8')
    reg=r'<a href="(.*?)" class="ulink">([\S\s]*?)</a>'
    return re.findall(reg,text)
# getList()

def getContent(url):
    html=urllib.urlopen('http://www.ygdy8.net%s'%url).read()
    con_text=html.decode('gbk').encode('utf-8')
    reg=r'<div class="co_content8">(.*?)<p><strong><font color="#ff0000" size="4">'
    reg=re.compile(reg,re.S)#编译正则为对象，增加匹配效果
    text= re.findall(reg,con_text)
    if text:
        text=text[0]
    return text
    # # reg=r'<td style="WORD-Wrap:break-word" bgcolor="#fdfddf"><a href="(.*?)"'
    # reg=r'thunderrestitle="(.*?)" onclick'
    # reg=re.compile(reg,re.S)
    # link=re.findall(reg,con_text)[0]
    # return text,link
# getContent('/html/gndy/dyzz/20170530/54084.html')

# html=urllib.urlopen('http://www.ygdy8.net/html/gndy/dyzz/20170530/54084.html').read()
# con_text=html.decode('gbk').encode('utf-8')
# reg=r'<div class="co_content8">(.*?)<p><strong><font color="#ff0000" size="4">"'
# reg=re.compile(reg,re.S)
# link=re.findall(reg,con_text)
# print link




'''(.*?) 任意字符    ([\S\s]*?)      re.S贪婪模式多行'''
conn=MySQLdb.connect(
    host='127.0.0.1',
    port=3307,
    user='root',
    passwd='test',
    db='mysql',
    charset='utf8',
    )
cur=conn.cursor()
for i in range(1,159):
    for url,title in getList(page=i):
        # url,title=x[url],x[title]
        print 'now is%s ---%s'%(i,title)
        content=getContent(url)
        print 'save%s ---%s'%(i,title)
        cur.execute('insert into movie(id,title,content) values (%r,%r,%r)'%(i,title,content))
        conn.commit()
# conn.close()