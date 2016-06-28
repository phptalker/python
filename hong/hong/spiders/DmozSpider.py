from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hong.items import DmozItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
    ]
    def start_requests(self):
        file_object = open('keyword.txt','r')

        try:
            # url_head = 'https://s.1688.com/selloffer/rpc_async_render.jsonp?startIndex=0&categoryId=1031910&n=y&pageSize=60&from=industrySearch&rpcflag=new&async=true&filt=y&templateConfigName=marketOfferresult&enableAsync=true&industryFlag=clothing&qrwRedirectEnabled=false&asyncCount=20&_pageName_=market&offset=9&uniqfield=pic_tag_id&leftP4PIds=528629958809,531479255456,532769217382,529040266394,533955975938,528035738,532648039880,531687841341&filterP4pIds=528629958809,531479255456,532769217382,529040266394,533955975938,528035738,532648039880,531687841341&callback=jQuery1830679384980656206_1466514015151&_=1466514046429'
            # url_head = url_head +'&beginPage='+ str(1)
            for line in file_object:
                self.start_urls.append( line)

            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        finally:
            file_object.close()

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
           item = DmozItem()
           item['title'] = site.select('a/text()').extract()
           item['link'] = site.select('a/@href').extract()
           item['desc'] = site.select('text()').extract()
           items.append(item)
        return items