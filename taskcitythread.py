 # -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from common import getRequestContent
import re
from conf import SOURCE_TASKCITY
from conf import maxThreadSum
import threading
from Queue import Queue
import time
import db

q = Queue()

def getSearchResult(page,searchKey):
    url = 'http://www.taskcity.com/projects/search?category_id=&page=%s&keywords=%s&status= ' %  (page,searchKey)
    print("正在收集爬取列表:%s" % url)

    content = getRequestContent(url)
    p = re.compile(r'<table(.+?)</table>',re.S)
    projectList = re.search( p,content)
    if(projectList): #列表内容分析
        patten = re.compile(r'<tr\s+?>\s+<td>(.*?)</tr>' ,re.S)
        list = re.findall(patten,projectList.group())
        if(list):
            #i = 0
            for td in list:
                pa = re.compile(r'<a href="(.*?)" class="font13px font_bold" target="_blank" title="(.*?)">(.*?)</a>')
                item = re.findall(pa,td)
                if(item):
                    for i in item:
                        subUrl = 'http://www.taskcity.com/%s'% i[0]
                        #processPageContent(subUrl,searchKey)
                        q.put((subUrl,searchKey))
            page = page + 1
            getSearchResult(page,searchKey)

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
    keyworkPatten = re.compile(r'<meta name="keywords" content="(.*)"/>',re.M)
    descriptionPatten = r'<meta name="description" content="(.*)"/>'
    projectNamePatten = re.compile(r'<h1 id="project_title_name">\s+(.*?)\s+<', re.S)
    projectIdPatten = re.compile(r'div>项目编号 :\s+<b>\s+(.*?)\s+</b>\s+?</div>',re.S)
    orangePatten = re.compile(r'div>项目预算 :\s+<b>\s+(.*?)\s+</b>\s+?</div>',re.S)
    prodescPatten = re.compile(r'<div id="project_description_la" style="overflow:hidden;">(.*?)<div id="trans_content', re.S)
    publishtimePatten = re.compile(r'<div>发布日期 : <h2 class="inline" style="font-size:12px">\s+(.*?)\s+</h2></div>',re.S)
    statusPatten = re.compile(r'状态 : <em class="font16px">(.*?)</em>',re.S)


    keyWordResult = keyworkPatten.search(subContent)
    descResult = re.search( descriptionPatten,subContent)
    projectNameResult = re.search( projectNamePatten,subContent)
    projectIdResult = re.search( projectIdPatten,subContent)
    proDescResult = re.search( prodescPatten,subContent)
    priceResult = re.search( orangePatten,subContent)
    publishtimeResult = re.search( publishtimePatten,subContent)
    statusResult = re.search( statusPatten,subContent)

    keyWord =  keyWordResult.groups()[0] if keyWordResult else ''
    descWord =  descResult.groups()[0] if descResult else ''
    projectName =  projectNameResult.groups()[0] if projectNameResult else ''
    projectId =  projectIdResult.groups()[0] if projectIdResult else ''
    price =  priceResult.groups()[0] if priceResult else ''
    proDesc =  proDescResult.groups()[0] if proDescResult else ''
    publishtime =  publishtimeResult.groups()[0] if publishtimeResult else ''
    proStatus =  statusResult.groups()[0] if statusResult else ''

    statusDict = {"竞标中":1,"买家已托管-工作中":2,"竞标已取消":5,"完成":3,"竞标已结束":4,'买家已支付-工作中':2}

    status = statusDict.get(proStatus)
    print(status)
    if(projectId):
        db.addOrUpdateProject(projectName,SOURCE_TASKCITY ,keyWord,descWord,proDesc,price,searchKey,projectId,publishtime,url,status)
page = 1
getSearchResult(page,'网站定制');
getSearchResult(page,'APP开发');
getSearchResult(page,'微信开发');
getSearchResult(page,'前端开发');
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



