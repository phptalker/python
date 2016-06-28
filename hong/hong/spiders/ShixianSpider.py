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
        try:
            f = open('test.txt', 'w')
            f.write(response)
        finally:
            f.close()
        hxs = HtmlXPathSelector(response)
        print(hxs)
        sites = hxs.select('//div[contains(@class,"a-topic with-white-background-color col-md-12 show xs-no-padding fix_flat")]')
        items = []
        # for site in sites:
        item = ShixianItem()
           # item['title'] = site.select('a/text()').extract()
           # item['link'] = site.select('a/@href').extract()
           # item['desc'] = site.select('text()').extract()
        items.append(item)
        return items