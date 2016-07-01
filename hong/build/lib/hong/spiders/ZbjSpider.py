#! /usr/bin/env python
# coding=utf-8
#
import logging
from scrapy.spiders.init import InitSpider

from scrapy.selector import Selector
from hong.items import ZbjItem
from scrapy.http import Request, FormRequest
import re

class ZbjSpider(InitSpider):
    name = "zbj"
    start_urls = ['http://www.zbj.com/rjkf/pp.html',
                  'http://www.zbj.com/rjkf/pp1.html',
                  'http://www.zbj.com/rjkf/pp2.html',
                  'http://www.zbj.com/rjkf/pp3.html',
                  'http://www.zbj.com/rjkf/pp4.html',
                  'http://www.zbj.com/rjkf/pp5.html',
                  'http://www.zbj.com/rjkf/pp6.html',
                  'http://www.zbj.com/rjkf/pp7.html',
                  'http://www.zbj.com/rjkf/pp8.html',
                  'http://www.zbj.com/rjkf/pp9.html',
                  'http://www.zbj.com/rjkf/pp10.html',
                  'http://www.zbj.com/rjkf/pp11.html',
                  'http://www.zbj.com/rjkf/pp12.html',
                  'http://www.zbj.com/rjkf/pp13.html',
                  'http://www.zbj.com/rjkf/pp14.html',
                  'http://www.zbj.com/rjkf/pp15.html',
                  'http://www.zbj.com/rjkf/pp16.html',
                  'http://www.zbj.com/rjkf/pp17.html',
                  'http://www.zbj.com/rjkf/pp18.html',
                  'http://www.zbj.com/rjkf/pp19.html',
                  'http://www.zbj.com/rjkf/pp20.html',
                  'http://www.zbj.com/rjkf/pp21.html',
                  'http://www.zbj.com/rjkf/pp22.html',
                  'http://www.zbj.com/rjkf/pp23.html',
                  'http://www.zbj.com/rjkf/pp24.html'
    ]
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'GBK,utf-8;q=0.7,*;q=0.3',
                'Connection': 'close',
                'Cookie':'_uq=4a43c4e762ea4feb6b9c763044e3f557; _ga=GA1.2.925409157.1452653479; __utma=168466538.925409157.1452653479'
+'.1467354001.1467357686.17; __utmz=168466538.1467357686.17.11.utmcsr=zbj.com|utmccn=(referral)|utmcmd'
+'=referral|utmcct=/yidongkf/ppp.html; searchArrayRandUsed=0%2C2; uniqid=d01w3kby2petnr; __utmc=168466538'
+'; marketing-dialog=opened; _uv=8; __utmb=168466538.4.10.1467357686; __utmt=1; _gat=1',
                'Host':'www.zbj.com',
                'Referer': 'www.zbj.com'  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
            }
    def start_requests(self):
        try:

            for i in range(1,2,1) :#self.start_urls :
                url = "http://www.zbj.com/rjkf/pp" + str(i)+".html"
                yield Request(url,headers=self.headers)
        finally:
            pass

    def parse(self, response):
        hxs = Selector(response)
        items = hxs.xpath("//div[@class='fws-detail clearfix']")


        for item in items:
            sites = item.xpath('div/div/div[@class="fws-item-webim"]/a[@target="_blank"]/@href').extract()
            companyName = item.xpath("h5/a[@class='witkey-item-name']/text()").extract()
            service = item.xpath("div/div/p[@class='like']/a/text()").extract()
            location = item.xpath("div/div/p[@class='fws-item-area']/span/a/text()").extract()
            isCompany = item.xpath("div/div/p[@class='fws-item-area']").re('"fws-item-area">(.*?)<span')
            # logging.info(isCompany)
            # logging.info(companyName)
            # logging.info(service)
            # logging.info(location)
            # logging.info("dddddddddddddddddddddddddddddddddddddddddddddddddddd")
            detail_url = sites[0]
            yield Request(detail_url,headers=self.headers , callback=self.parse_detail,meta={'detail_url':detail_url,'name':companyName,'service':service,'location':location,'isCompany':isCompany})

    def parse_detail(self,response):
        # return
        hxs = Selector(response)
        # title = hxs.xpath("//div[@class='shop-fixed-im-name']/div[@class='fix-im-cate']/text()").extract()
        tels = hxs.xpath("//div[@class='shop-fix-im-time']/div[@class='time-item']").re("[\d-]{7,13}")
        detail = hxs.xpath("//div[@class='company-module-info']/pre[@class='detail']/text()").extract()
        items = []
        item = ZbjItem()
        item['url'] = response.meta['detail_url']
        item['service']= response.meta['service'][0]
        item['location']=response.meta['location'][0]
        item['company']= response.meta['name'][0]
        item['isCompany']= response.meta['isCompany'][0]
        item['tel']=''
        item['mobile']=''
        item['detail']=''

        if(detail):
            item['detail']= detail[0]
        if(tels):
            temp = ''
            for tel in tels:
                if(temp != ''):
                    temp = temp + ',' + tel
                else:
                    temp =  tel
                if(re.search("\d{11}",tel)):
                    item['mobile'] = tel;
            item['tel'] = temp
        logging.info(item)
        items.append(item)
        return items