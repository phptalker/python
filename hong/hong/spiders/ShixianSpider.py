#! /usr/bin/env python
# coding=utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hong.items import ShixianItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
class ShixianSpider(BaseSpider):
    name = "shixian"
    start_urls = ['http://shixian.com/consultants/2']
    def start_requests(self):

        try:
            # for i in range(3,4,1):
            #     self.start_urls.append( i)

            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            pass

    def parse(self, response):
        # try:
            # f = file('test.txt', 'w')
            # f.write(response)
        # finally:
            # f.close()
        hxs = HtmlXPathSelector(response)
        print(response)
        sites = hxs.select('//div[contains(@class,"a-topic with-white-background-color col-md-12 show xs-no-padding fix_flat")]')
        items = []
        # for site in sites:
        item = ShixianItem()

        item['nick'] = sites.select("//span[contains(@class,'topic-title-txt link-blue programmer-username')]/text()").extract()
        work = sites.select("//span[contains(@class,'topic-title-txt')]/text()").extract()
        item['company'] = work[0]
        item['title'] = work[1]
        item['workYear'] = work[2]
        item['city'] = sites.select("//span[contains(@class,'topic-title-txt')]/text()").extract()
        item['kind'] = sites.select("//span[contains(@itemprop,'itemprop')]/text()").extract()
        item['techExp'] = sites.select("//span[contains(@itemprop,'technical_experience-show')]/text()").extract()
        item['proExp'] = sites.select("//span[contains(@class,'project_experience-show')]/text()").extract()
        item['daySalary'] = sites.select("//div[contains(@itemprop,'itemprop')]/text()").extract()
        item['partTime'] = sites.select("//div[contains(@class,'appointment_time-region-address')]/text()").extract()
        item['expLocation'] = sites.select("//a[contains(@class,'region-address')]/text()").extract()
           # item['title'] = site.select('a/text()').extract()
           # item['link'] = site.select('a/@href').extract()
           # item['desc'] = site.select('text()').extract()
        items.append(item)
        return item