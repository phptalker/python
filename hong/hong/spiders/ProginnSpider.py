#! /usr/bin/env python
# coding=utf-8
#
import logging
from scrapy.spiders.init import InitSpider

from scrapy.selector import Selector
from hong.items import ProginnItem
from scrapy.http import Request, FormRequest

class ProginnSpider(InitSpider):
    name = "proginn"
    start_urls = ['https://www.proginn.com/wo/2']
    login_page = 'https://github.com/login?return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3Dd17ee315d7c2a8bf8a89%26redirect_uri%3Dhttp%253A%252F%252Fshixian.com%252Fusers%252Fauth%252Fgithub%252Fcallback%26response_type%3Dcode%26state%3D2e9d600e04df65c161ada29922ed57c37c52debf2a7fd550'
    check_login_response = 'http://shixian.com'

    def start_requests(self):

        try:
            # for i in range(3,4,1):
            #     self.start_urls.append( i)
            for i in range(1,109929,1):
                url = "https://www.proginn.com/wo/" + str(i)
                yield Request(url ,meta={'item': str(i)}) #self.make_requests_from_url(url)
        finally:
            pass

    def parse(self, response):
        # try:
            # f = file('test.txt', 'w')
            # f.write(response)
        # finally:
            # f.close()

        hxs = Selector(response)

        # sites = hxs.xpath('//div[contains(@class,"ui grid clearfix")]')
        items = []
        # for site in sites:
        item = ProginnItem()
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
        item['nick'] = hxs.xpath("//div[@class=' nickname']/span/text()").extract()
        if(item['nick']):
           item['nick'] = item['nick'][0].replace("\n",'')

        experience = hxs.xpath("//div[@class='overflowhidden editor-style content']").extract()
        if(experience):
           item['experience'] = item['experience'][0].replace("\n",'')
        work = hxs.xpath("//div[@class='introduction']").re("<i.*?</i>(.*?)</div>")
        if(work):
            arr = work[0].split(" ",1)
            item['company'] = arr[0]
            item['title']   = arr[1]
        # item['title'] = work[1]
        # item['workYear'] = work[2]



        hireinfo = hxs.xpath("//div[@class='hire-info']/p")
        # item['company'] = work[0]
        if(hireinfo):
            item['daySalary'] = hireinfo.re("<span.*?>(.*?)</span>")[0]
            item['partTime'] =  hireinfo.xpath("text()").extract()[2]


        location =  hxs.xpath("//div[contains(@class,'tags')]/a/text()").extract()

        # item['city'] = hxs.xpath("//div[contains(@class,'programmer-profile-tags')]/a").re("<a.*?>(.*?)</a>")
        if(location):
           item['city'] = location[0]
           item['kind'] = location[1]

        # item['kind'] = hxs.xpath("//span[contains(@itemprop,'category')]/text()").extract()
        # if(item['kind']):
        #    item['kind'] = item['kind'][0]

        # item['techExp'] = hxs.xpath("//div[contains(@class,'technical_experience-show')]").re("<p>(.*?)</p>")
        # if(item['techExp']):
        #    item['techExp'] = item['techExp'][0]
        #
        # item['proExp'] = hxs.xpath("//div[@class='technical_experience-show']").re("<p>(.*?)</p>")
        # if(item['proExp']):
        #    item['proExp'] = item['proExp'][0]

        skill_list = hxs.xpath("//div[@class='skill-list']/div[@class='skill']/div[@class='name']/text()").extract()
        if(skill_list):
            temp = ''
            for skill in skill_list:
                if(temp != ''):
                    temp = temp + ',' + skill
                else:
                    temp =  skill
            item['skill'] = temp
        #
        # item['partTime'] = hxs.xpath("//div[@class='appointment_time-region-address']/p/text()").extract()
        # if(item['partTime']):
        #    item['partTime'] = item['partTime'][1].replace("\n",'')
        # else:
        #     item['partTime'] = ''

        # item['expLocation'] = hxs.xpath("//div[@itemprop='areaServed']/text()").extract()
        # if(item['expLocation']):
        #    item['expLocation'] = item['expLocation'][0].replace("\n",'')
           # item['title'] = site.xpath('a/text()').extract()
           # item['link'] = site.xpath('a/@href').extract()
           # item['desc'] = site.xpath('text()').extract()
        items.append(item)
        return item