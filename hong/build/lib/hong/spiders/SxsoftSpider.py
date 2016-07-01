#! /usr/bin/env python
# coding=utf-8
#
import logging
from scrapy.spiders.init import InitSpider

from scrapy.selector import Selector
from hong.items import SxsoftItem
from scrapy.http import Request, FormRequest

class SxsoftSpider(InitSpider):
    name = "sxsoft"
    start_urls = ['http://www.sxsoft.com/user/history/2']

    def start_requests(self):

        try:

            for i in range(1,258565,1):
                url = "http://www.sxsoft.com/user/gethuiyuan/" + str(i)
                yield Request(url ,meta={'item': str(i)}) #self.make_requests_from_url(url)
        finally:
            pass

    def parse(self, response):

        hxs = Selector(response)
        logging.log(logging.INFO,hxs)

        sites = hxs.xpath('//ul/li')
        # print(sites)
        items = []
        # for site in sites:
        item = SxsoftItem()
        item['uid']=''
        item['nick']=''
        item['company']=''
        item['title']=''
        item['workYear']=''
        item['city']=''
        item['kind']=''
        item['techExp']=''
        item['proExp']=''
        item['daySalary']=''
        item['partTime']=''
        item['expLocation']=''
        item['skill']=''
        item['experience'] = ''
        item['uid'] = response.meta['item']

        item['nick'] = sites[0].re("</span>(.*?)</li>")[0]
        print(item['nick'])
        if(item['nick']):
           item['nick'] = item['nick'].replace("\n",'')

        # work = sites.xpath("//h2[@class='username-and-base-info']/span[contains(@class,'topic-title-txt')]/text()").extract()
        # item['company'] = work[0]
        # item['title'] = work[1]
        # item['workYear'] = work[2]

        item['city'] = sites[1].re("</span>(.*?)</li>")[0]
        if(item['city']):
           item['city'] = item['city']

        # item['kind'] = sites.xpath("//span[contains(@itemprop,'category')]/text()").extract()
        # if(item['kind']):
        #    item['kind'] = item['kind'][0]

        # item['techExp'] = sites.xpath("//div[contains(@class,'technical_experience-show')]").re("<p>(.*?)</p>")
        # if(item['techExp']):
        #    item['techExp'] = item['techExp'][0]
        #
        # item['proExp'] = sites.xpath("//div[@class='technical_experience-show']").re("<p>(.*?)</p>")
        # if(item['proExp']):
        #    item['proExp'] = item['proExp'][0]

        skill_list = sites.xpath("//span[@class='green']/text()").extract()
        if(skill_list):
            temp = ''
            for skill in skill_list:
                if(temp != ''):
                    temp = temp + ',' + skill
                else:
                    temp =  skill
            item['skill'] = temp
        if(sites[5].re("qq:(\d{5,11})")):
            item['title'] = sites[5].re("qq:(\d{5,11})")[0]
        if(sites[5].re("tel:(\d{5,11})")):
            item['partTime'] = sites[5].re("tel:(\d{5,11})")[0]
        if(sites[5].re("email:(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)")):
            item['techExp'] = sites[5].re("email:(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)")[0]
        # item['partTime'] = sites.xpath("//span[@class='org']").re("<b>￥(.*?)</b>RMB/H")
        # if(item['partTime']):
        #    item['partTime'] = item['partTime'][0].replace("\n",'')
        # else:
        #     item['partTime'] = ''

        # item['expLocation'] = hxs.xpath("//div[@itemprop='areaServed']/text()").extract()
        # if(item['expLocation']):
        #    item['expLocation'] = item['expLocation'][0].replace("\n",'')
           # item['title'] = site.xpath('a/text()').extract()
           # item['link'] = site.xpath('a/@href').extract()
           # item['desc'] = site.xpath('text()').extract()
        items.append(item)
        logging.log(logging.INFO,item)
        return item