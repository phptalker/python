from scrapy.spider import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import Rule
from hong.items import DmozItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
class MininovaSpider(CrawlSpider):
    name = 'mininova'
    allowed_domains = ['mininova.org']
    start_urls = ['http://www.mininova.org/today']
    rules = [Rule(SgmlLinkExtractor(allow=['/tor/\d+'])),
             Rule(SgmlLinkExtractor(allow=['/abc/\d+']), 'parse_torrent')]
    def parse_torrent(self, response):
        x = HtmlXPathSelector(response)
        torrent = DmozItem()
        torrent['url'] = response.url
        torrent['name'] = x.select("//h1/text()").extract()
        torrent['description'] = x.select("//div[@id='description']").extract()
        torrent['size'] = x.select("//div[@id='info-left']/p[2]/text()[2]").extract()
        return torrent