#! /usr/bin/env python
# coding=utf-8
#
import logging
from scrapy.spiders.init import InitSpider

from scrapy.selector import Selector
from hong.items import ShixianItem
from scrapy.http import Request, FormRequest

class ShixianSpider(InitSpider):
    name = "shixian"
    start_urls = ['http://shixian.com/consultants/2']
    login_page = 'https://github.com/login?return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3Dd17ee315d7c2a8bf8a89%26redirect_uri%3Dhttp%253A%252F%252Fshixian.com%252Fusers%252Fauth%252Fgithub%252Fcallback%26response_type%3Dcode%26state%3D2e9d600e04df65c161ada29922ed57c37c52debf2a7fd550'
    check_login_response = 'http://shixian.com'
    def __init__(self):
        self.init_request()

    def init_request(self):
        """This function is called before crawling starts."""

        print("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'login': 'hong1070@qq.com', 'password': 'hong1070','authenticity_token':'k5CSe6yJCxBp1wWjTzI4dctk+LDK9FkeJUayWW3yGAmOgbHLh9Vl5b1G6nxH7dcdg4nFJADwnYoy8v95nyldMg==' },
                    callback=self.check_login_response)

    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if "Hi Herman" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            self.initialized()
        else:
            self.log("Bad timesdssss111111111111111111111111111111111111111111111111111111111111111111 :(")


    def start_requests(self):

        try:
            # for i in range(3,4,1):
            #     self.start_urls.append( i)
            cookie= {
                'Hm_lpvt_25e3b17ddf2b132427768bfebf751a76':"1467200067",
                'Hm_lvt_25e3b17ddf2b132427768bfebf751a76':"1467027139,1467027353,1467199243",
                'get_real_session':"cTM2WmxUN2sySlRBS091bmswUGxHRTN2QmdaS1RRcUlZSC9DclB0UDYrNWhrayszYWg4RWUwLzM3eWRpaE9QQ1V4UkpXL0JGbkk3cDJkaFVYODNMMCtTR3hwTzcrcjVWc3BpYjhhQWVDZVl0ZTFJejN2VWZ1WDREbUc3YS9pZlRsQXdBS3drTUswRm1CellxSnhOcUczUkM0V09uWHhucTRka25oWXdhelV6Qnd1eHhSOWYrSkI2QjJKR3VnU1hIQzlMZVI0UWZ0VnRpeEwwM1JkRWJLUT09LS04UngyN3VtVVdkRVI3WGEraDFkMGVBPT0=--0f43be854b686145883750a9b588b1a11ee2a55e",
                'gr_session_id_acf6ac3446a1dcb0':"141dc4f5-bba6-4361-820b-59d7ccaeeb31",
                'gr_user_id':"1cd58c8f-1278-46fd-a1ac-d610671f315f"
            }

            headers ={
                'Host':"shixian.com",
                'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
                'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                'Accept-Encoding':"gzip, deflate",
                'Cookie':"_get_real_session_=T2NIZGx6Z2dRYzNjM2dVVmN5alRra1R4RExubEFJM3I0ODNYQ01LNzRUTEhGZGtEQUwyR211alFhZmNjZDY0eUJUMHZQa3c0RFNNdEphWXpmWHhCSzVZWkFFTCs2WW9YeWdOUFJPM1JSQlpKS0VzWGtkWC9IQzZoYm1OUGhaTFhKVTkxRkxYYU90eGpWN3BCc2FjWVJLVnhIVWxkZHp5T2hiUVgyQW10dE8wT2VuWUtPRjE4VWlISU1md2p0dnlHNEpCalF1ZElrL0F5VXBDQis2Ly9mdz09LS12VWFSaDBMbWV3bW1vT3FqWWM5Mk13PT0%3D--a0a21b09d6976a145ac95b445530a70efc000af2; Hm_lvt_25e3b17ddf2b132427768bfebf751a76=1467027139,1467027353; gr_user_id=1cd58c8f-1278-46fd-a1ac-d610671f315f; Hm_lpvt_25e3b17ddf2b132427768bfebf751a76=1467190992; gr_session_id_acf6ac3446a1dcb0=3b94b20c-3545-4275-8ef2-c6e11423b206",
                'Connection':"keep-alive",
                'If-None-Match':'W/"e23480aef5800219a8f3cd6b4bc864f9"',
                'Cache-Control':"max-age=0"
            }

            for i in range(2,3,1):
                url = "http://shixian.com/consultants/" + str(i)
                yield Request(url,cookies=cookie ,meta={'item': str(i)}) #self.make_requests_from_url(url)
        finally:
            pass

    def parse(self, response):
        # try:
            # f = file('test.txt', 'w')
            # f.write(response)
        # finally:
            # f.close()

        hxs = Selector(response)

        logging.log(logging.INFO,hxs)

        sites = hxs.xpath('//div[contains(@class,"a-topic with-white-background-color col-md-12 show xs-no-padding fix_flat")]')
        items = []
        # for site in sites:
        item = ShixianItem()

        item['uid'] = response.meta['item']
        item['nick'] = hxs.xpath("//span[@class='topic-title-txt link-blue programmer-username']/text()").extract()
        if(item['nick']):
           item['nick'] = item['nick'][0].replace("\n",'')

        work = sites.xpath("//h2[@class='username-and-base-info']/span[contains(@class,'topic-title-txt')]/text()").extract()
        item['company'] = work[0]
        item['title'] = work[1]
        item['workYear'] = work[2]

        item['city'] = sites.xpath("//div[contains(@class,'programmer-profile-tags')]/a").re("<a.*?>(.*?)</a>")
        if(item['city']):
           item['city'] = item['city'][0]

        item['kind'] = sites.xpath("//span[contains(@itemprop,'category')]/text()").extract()
        if(item['kind']):
           item['kind'] = item['kind'][0]

        item['techExp'] = sites.xpath("//div[contains(@class,'technical_experience-show')]").re("<p>(.*?)</p>")
        if(item['techExp']):
           item['techExp'] = item['techExp'][0]

        item['proExp'] = sites.xpath("//div[@class='technical_experience-show']").re("<p>(.*?)</p>")
        if(item['proExp']):
           item['proExp'] = item['proExp'][0]

        item['daySalary'] = sites.xpath("//span[@itemprop='price']/@content").extract()
        if(item['daySalary']):
           item['daySalary'] = item['daySalary'][0]

        item['partTime'] = sites.xpath("//div[@class='appointment_time-region-address']/p/text()").extract()
        if(item['partTime']):
           item['partTime'] = item['partTime'][1].replace("\n",'')
        else:
            item['partTime'] = ''

        item['expLocation'] = hxs.xpath("//div[@itemprop='areaServed']/text()").extract()
        if(item['expLocation']):
           item['expLocation'] = item['expLocation'][0].replace("\n",'')
           # item['title'] = site.xpath('a/text()').extract()
           # item['link'] = site.xpath('a/@href').extract()
           # item['desc'] = site.xpath('text()').extract()
        items.append(item)
        # logging.log(logging.INFO,item)
        return item