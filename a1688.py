 # -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from common import getRequestContent
from common import filter_tags
import re
from conf import SOURCE_ZHUBAJIE
from conf import maxThreadSum
import threading
from Queue import Queue
import time
import db
import urllib2
q = Queue()


def getListData(page,searchKey):
    url ='https://s.1688.com/selloffer/rpc_async_render.jsonp?startIndex=0&categoryId=1031910&n=y&pageSize=60&from=industrySearch&rpcflag=new&async=true&filt=y&templateConfigName=marketOfferresult&enableAsync=true&industryFlag=clothing&qrwRedirectEnabled=false&asyncCount=20&_pageName_=market&offset=9&uniqfield=pic_tag_id&leftP4PIds=528629958809,531479255456,532769217382,529040266394,533955975938,528035738,532648039880,531687841341&filterP4pIds=528629958809,531479255456,532769217382,529040266394,533955975938,528035738,532648039880,531687841341&callback=jQuery1830679384980656206_1466514015151&_=1466514046429'# 'http://task.zhubajie.com/s5p%s.html?kw=%s ' %  (page,searchKey)
    url = url+'&beginPage='+ str(page)
    url = url+'&keywords='+ urllib2.quote(searchKey.decode('utf8').encode("gbk"))
    url = url + '&province=%C9%CF%BA%A3'
    #$keywords=%C1%AC%D2%C2%C8%B9
    print("正在收集爬取列表:%s" % url)
    content = getRequestContent(url)
    #content = "1234klwofferResult edfs2wwd beaconP4Pidsfsdf"
    p = re.compile(r'"html":(.*?)},\s+"beaconP4Pid"',re.S)
    result =  re.findall( p,content.decode('gbk').encode("utf8"))
    #if(result!=None):
        #print(result[0])
   # print(content.decode('gbk').encode("utf8"))

    if(result!=None and  result): #列表内容分析
        originalListData = result[0].replace('\\','');
        partten = re.compile(r'<a[^\>]*?class="sm-offer-photoLink sw-dpl-offer-photoLink".*?href="(http.*?)(?!css)".*?>',re.S)
        projectList = re.findall( partten ,  originalListData)
        for i in projectList:

            if(i != None and i ):
                q.put((i,searchKey))
        #patten = r'<tr.*?</tr>'
        #list = re.findall(patten,projectList.group())
        #if(list):
            #for td in list:
                #pa = re.compile(r'<tr.*?>.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?</tr>')
                #item = re.findall(pa,td)
                #for i in item:
                    #subUrl = i[0]
                    #processPageContent(subUrl,searchKey)

        page = page + 1
        getListData(page,searchKey)
class processDetail(threading.Thread):
    def __init__(self,threadingSum,url,searchKey ):
        threading.Thread.__init__(self)
        self.url =  url
        self.searchKey = searchKey
        self.threadingSum = threadingSum

    def run(self):
        with self.threadingSum:
            processPageContent(self.url,self.searchKey)
            time.sleep(1)
#具体的处理函数，负责处理单个任务
def processPageContent(url,searchKey):
    print("正在爬取页面：%s" % url)

    subContent = getRequestContent(url)
   # print(subContent)
    contactUrl = re.findall(re.compile(r'data-page-name="contactinfo">\s*<a.*?href="(.*?)"',re.S),subContent)
    if(contactUrl!=None and contactUrl):

        contactPageUrl = contactUrl[0];
        detailContent = getRequestContent(contactPageUrl)
        if (detailContent ==None):
            return
        else:
            detailContent = detailContent.decode('gbk', 'ignore').encode("utf8")

        contactDesc =  re.search(re.compile(r'<div class="fd-clr">(.*?)<div class="map-container">',re.S),detailContent)

        if (contactDesc ==None):
            return
        else:
            contactDesc = contactDesc.group()

        companyInfo = re.findall(re.compile(r'class="contact-info".*?<h4>(.*?)</h4>',re.S),contactDesc)
        descInfo =  re.findall(re.compile(r'<dl.*?>.*?<dt>(.*?)</dt>.*?<dd.*?>(.*?)</dd>(.*?)</dl>',re.S),contactDesc)
        #print(contactDesc)
       # print(descInfo)
        if(descInfo):
            company_name = companyInfo[0];
            robot_key = searchKey;
            contact = '';
            contact_title = '';
            tel = '';
            mobile = '';
            fax = '';
            address = '';
            post_code = '';
            website = '';

            for item in descInfo:
                 #for item in descInfo[i]:
                if (item[0] == '联&nbsp;系&nbsp;&nbsp;人：'):
                    #print(item[1])
                    detail = re.findall(re.compile('<a.*?class="membername".*?>(.*?)</a>(.*?)<a',re.S),item[1])
                    contact =  detail[0][0]
                    contact_title =  detail[0][1].replace('&nbsp;','')

                elif(item[0] == '电&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;话：'):
                    tel = filter_tags(item[1])
                elif(item[0] == '移动电话：'):
                    mobile =  item[1]
                elif(item[0] == '传&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;真：'):
                    fax = filter_tags(item[1])
                elif(item[0] == '地&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;址：'):
                    address = filter_tags(item[1])
                elif(item[0] == '邮&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;编：'):
                    post_code = filter_tags(item[1])
                elif(item[0] == '公司主页：'):
                    webSitedetail = re.findall(re.compile('<a.*?>(.*?)</a>',re.S),item[1])
                    if(webSitedetail !=None and webSitedetail):
                        for item in webSitedetail:
                            website =  website + item

                else:
                    pass
                #print(item[1])
            robot_page = contactPageUrl
            db.addOrUpdateCostomer(robot_page,company_name,robot_key,contact,contact_title,tel,mobile,fax,address,post_code,website)
                    #print("联系人:"+item+"\n")
    return

page = 1
getListData(page,'连衣裙');
getListData(page,'半身裙');
getListData(page,'T恤');
getListData(page,'衬衫');
getListData(page,'套装');
getListData(page,'蕾丝衫');
getListData(page,'外套');
getListData(page,'针织衫');
getListData(page,'风衣');
getListData(page,'牛仔裤');
getListData(page,'打底裤');
getListData(page,'休闲裤');

getListData(page,'童鞋');
getListData(page,'男鞋');
getListData(page,'爸爸鞋');
getListData(page,'休闲鞋');
getListData(page,'童运动鞋');
getListData(page,'家居拖鞋');
getListData(page,'牛津鞋');
getListData(page,'女鞋');
getListData(page,'凉鞋上新');
getListData(page,'单鞋');
getListData(page,'厚底松糕');
getListData(page,'绑带鞋');

getListData(page,'小白鞋');
getListData(page,'鱼嘴鞋');
getListData(page,'高跟鞋');
getListData(page,'妈妈鞋');
getListData(page,'英伦风');
getListData(page,'夏精选');
getListData(page,'潮流女包');
getListData(page,'潮流女包');
getListData(page,'潮流女包');
getListData(page,'卡包卡套');
getListData(page,'拉杆箱');
getListData(page,'万向轮');
getListData(page,'行李箱');
getListData(page,'男包');
getListData(page,'书包');
print("列表收集完毕")


#设置线程数
threadingSum = threading.Semaphore(maxThreadSum)
for t in threading.enumerate():
    if t is threading.currentThread():
        continue
    t.join()
while True:
    arguments = q.get()
    t = processDetail(threadingSum,arguments[0],arguments[1])
    t.start()


