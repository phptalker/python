 # -*- coding: utf-8 -*-
import requests
import urllib2
import time
import re

def getRequestContent(url,params = None):
    return getpage_content(url)
    try:
#         headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept':'text/html;q=0.9,*/*;q=0.8',
# 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
# 'Accept-Encoding':'GBK,utf-8;q=0.7,*;q=0.3',
# 'Connection':'close',
# 'Referer':'http://s.1688.com'
#                     }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'GBK,utf-8;q=0.7,*;q=0.3',
            'Connection': 'close',
            'Referer': 'http://s.1688.com'  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
        }
        r = requests.get(url,headers = headers,params = params )
        r.encoding = 'utf-8'
        content = r.content
        return content
    except:
        print 'get url excepton'
        return ''
def getpage_content(url):
    try:
        req_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'gbk,utf-8;q=0.7,*;q=0.3',
            #'Accept-Encoding': 'gzip, deflate, br',
            #'Host':'cssdmy.1688.com',
            'Connection': 'close',
            'Referer': 'http://s.1688.com',  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
            'Cookie':'cna=Da76DluikCsCAXJQfO7pc+Y8; ali_beacon_id=114.80.124.238.1452136028574.821040.9; l=AlBQCoBiQKf-sPxYk9QbcWThAJSiFzRj'
+'; alicnweb=touch_tb_at%3D1466583194732%7Clastlogonid%3D%25E7%259B%25B8%25E5%25AE%258Fhong%7Cshow_inter_tips'
+'%3Dfalse; ali_ab=114.80.124.238.1461749204425.5; __last_loginid__=%E7%9B%B8%E5%AE%8Fhong; ad_prefer="2016'
+'/06/22 12:03:00"; h_keys="%u8fde%u8863%u88d9#%u534a%u8eab%u88d9#T%u6064#%u51c9%u978b%u5973%u4e0a%u65b0"'
+'; JSESSIONID=8L780Huu1-KItVHf755eMiEiYMz9-rIQkkoP-J4; _tmp_ck_0="Txa1L15%2BuAvdneEEsujDZu0v62IhDyqMZaInjlo0vXMn2vocMBrqOc9vtGeKqQHXK'
+'%2BLNee2c9XZjeT%2FfXMGLLyCx6%2B6Keai%2FR%2F%2Bkb%2B7uGpQkZO7LRwqnZg%2BAfr1YcVZBf0MbE1S7uFo%2FLT%2FPUNG5LbiedlPr6dR43xt'
+'%2FQJ5TSs0kKhKym15KXjRJhmjKH7CSXew8ppFAGeyT0Vg6cPy19zqSeXdc9yp2MX2FaK24mta90T2xvk6b88d2XfxhGoKjUVVx6u3lNLwz'
+'%2FIidg3JHDnzDNHtaO1JIqZRY6DfzDP7o61%2FsWzqrWUd6gpddMxolIrwR7ze%2Fu6cMpdfAooHicStM3hg%2B2T%2FjNPLq5SXYv'
+'%2FBjsyCx01gyWPwAj5ebvAtjO3Rj4WJN3vKwMe27lRlws7kB1j9IlRqCQPG1hlQtJqsse8VIjHe9X0P66DL%2BB2sBYtpav3B9wxx8bqsePbrWpeF6zOp14JXaYuVvyI511vpUvHqUVjhpo0EBAtZJUCT'
+'%2FqdsZLxTBv6s%3D"; __cn_logon__=true; _csrf_token=1466563136810; _ITBU_IS_FIRST_VISITED_=*xC-i2FILvGcSvFc4MFNYxClCONTT'
+'%3Apm0gksfuco%7C*xC-i2FIWMmkSvCx0OFNT%3Apm0gksir9j%7C*xC-i2FILMFcLvGIyvGvYMmZlZQTT%3Apm0gkvicu1%7Ccssdmy'
+'%3Apm0gl01d89%7Clovevivi8%3Apm0gl2clh0; ali_apache_track="c_ms=1|c_mid=b2b-2024604987|c_lid=%E7%9B%B8'
+'%E5%AE%8Fhong"; ali_apache_tracktmp="c_w_signed=Y"; _cn_slid_="tDgmPI%2Bv1N"; _nk_="w5jRBvAskw06sOlEpJKl9g'
+'%3D%3D"; tbsnid=DS7J7VYP3UB4BHbok0SiDqryct0VVMF%2BuLNqytnw4to6sOlEpJKl9g%3D%3D; LoginUmid="uTJWw7VoBxpE'
+'%2FBhjWfebRUN2RDa8pd7HoJfbPRSLqLcQoN5blcC8mQ%3D%3D"; userID="ayKurTm%2BYO7Ngy89m3B1lMdhUB88RRguF5qtP'
+'%2BqBLUE6sOlEpJKl9g%3D%3D"; last_mid=b2b-2024604987; userIDNum="%2F59DgCPWlF3MNAmuq23ipg%3D%3D"; login'
+'="kFeyVBJLQQI%3D"; __cn_logon_id__=%E7%9B%B8%E5%AE%8Fhong'
        }
        req_timeout = 5
        req = urllib2.Request(url, None, req_header)
        resp = urllib2.urlopen(req, None, req_timeout)
        page = resp.read()
        #content = page.encoding = 'gbk'
        return page
    except Exception, e:
        print e
    print "fail to get web ,redownload"
    #time.sleep(5)  # 休眠10秒
    #page = getpage_content(url)
    return ''




    ##过滤HTML中的标签
    #将HTML中标签等信息去掉
    #@param htmlstr HTML字符串.
def filter_tags(htmlstr):
    #先过滤CDATA
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_br=re.compile('<br\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    s=re_cdata.sub('',htmlstr)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    s=re_br.sub('\n',s)#将br转换为换行
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释
    #去掉多余的空行
    blank_line=re.compile('\n+')
    s=blank_line.sub('\n',s)
    #s=replaceCharEntity(s)#替换实体
    return s
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ',
    'lt':'<','60':'<',
    'gt':'>','62':'>',
    'amp':'&','38':'&',
    'quot':'"','34':'"',}

    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()#entity全称，如&gt;
        key=sz.group('name')#去除&;后entity,如&gt;为gt
    try:
        htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
        sz=re_charEntity.search(htmlstr)
    except KeyError:
        #以空串代替
        htmlstr=re_charEntity.sub('',htmlstr,1)
        sz=re_charEntity.search(htmlstr)
    return htmlstr

def repalce(s,re_exp,repl_string):
    return re_exp.sub(repl_string,s)