#! /usr/bin/env python
# coding=utf-8
import urllib2
import time
import json
import re
import cgi
def getpage_content(url):
    try:
        req_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'GBK,utf-8;q=0.7,*;q=0.3',
            'Connection': 'close',
            'Referer': 'http://s.1688.com'  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
        }
        req_timeout = 5
        req = urllib2.Request(url, None, req_header)
        resp = urllib2.urlopen(req, None, req_timeout)
        page = resp.read().decode('gbk').encode("utf8")
        patten = re.compile(r'"offerResult":(.*?),\s+"beaconP4Pid"',re.S)

        r = re.search(patten , page)
        afterRemoveLastCommaInList =  r.groups()[0]
       # replacedQuoteJson = re.sub(r"\\x26([a-zA-Z]{2,6});", r"&\1;", afterRemoveLastCommaInList);
        #logging.info("replacedQuoteJson=%s", replacedQuoteJson);

       # page = json.loads(afterRemoveLastCommaInList)
        return  afterRemoveLastCommaInList
    except Exception, e:
        print e
    print "fail to get web ,redownload"
    time.sleep(5)  # 休眠10秒
    page = getpage_content(url)
    return page


def main(keyword):
    search_url_head = 'http://s.1688.com/selloffer/offer_search.htm?keywords='
    search_url = search_url_head + urllib2.quote(keyword) + '&button_click=top&earseDirect=false&n=y'
   # search_url =''
    url ='https://s.1688.com/selloffer/rpc_async_render.jsonp?keywords=%C1%AC%D2%C2%C8%B9&startIndex=0&categoryId=1031910&n=y&pageSize=60&from=industrySearch&rpcflag=new&async=true&filt=y&templateConfigName=marketOfferresult&enableAsync=true&industryFlag=clothing&qrwRedirectEnabled=false&asyncCount=20&_pageName_=market&offset=9&uniqfield=pic_tag_id&leftP4PIds=529599399267,532596255040,530486935347,531995465542,521378507594,532737265109,527113475889,531531294267&filterP4pIds=529599399267,532596255040,530486935347,531995465542,521378507594,532737265109,527113475889,531531294267&callback=jQuery183027903151603541654_1464844444380&beginPage=4&_=1464844655887'# 'http://task.zhubajie.com/s5p%s.html?kw=%s ' %  (page,searchKey)

    page = getpage_content(url)
    print(page)

main('女鞋')
