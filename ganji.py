#coding:utf-8
__Author__='dido'

import requests,csv,bs4,html5lib
from bs4 import BeautifulSoup

url='http://bj.ganji.com/fang1/o{page}p{price}'
ADDR='http://bj.ganji.com/'

if __name__ == '__main__':
    start_page=1
    end_page=10
    price=7
    with open('ganji.csv','wb') as f:
        csv_writer=csv.writer(f,delimiter=',')
        print 'start...........................'
        while start_page<=end_page:
            start_page+=1
            s=url.format(page=start_page,price=price)
            print 'get:{0}'.format(s)
            response=requests.get(s)

            html=BeautifulSoup(response.text,'html.parser')
            # print html
            house_list=html.select('.f-list>.flist-item>.f-list-item-wrap')#list
            # if not house_list:
            #     break
            for house in house_list:
                house_title=house.select('.title>a')[0].string.encode('utf-8')
                house_address=house.select('.address>.area>a')[-1].string.encode('utf-8')
                house_price=house.select('.info>.price>.num')[0].string.encode('utf-8')
                house_url=urljoin(ADDR,house.select('.title>a')[0]['href'])
                csv_writer.writerow([house_title,house_address,house_price,house_url])
        print 'end....................................'
