 # -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from common import getRequestContent
import re
from conf import SOURCE_ZHUBAJIE
from conf import maxThreadSum
import threading
from Queue import Queue
import time
import db
q = Queue()

def getSearchResult(page,searchKey):
    url = 'http://task.zhubajie.com/s5p%s.html?kw=%s ' %  (page,searchKey)
    print("正在收集爬取列表:%s" % url)
    content = getRequestContent(url)
    p = re.compile(r'<table class="list-task"><colgroup><col><col width="110px"><col width="130px"><col width="105px"></colgroup>(.+)</table>')
    projectList = re.search( p,content)
    if(projectList): #列表内容分析
        patten = r'<tr.*?</tr>'
        list = re.findall(patten,projectList.group())
        if(list):
            for td in list:
                pa = re.compile(r'<tr.*?>.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?</tr>')
                item = re.findall(pa,td)
                for i in item:
                    subUrl = i[0]
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
    keyworkPatten = re.compile('<meta name="keywords" content="(.*)" />',re.M)
    descriptionPatten = r'<meta name="description" content="(.*)" />'
    projectNamePatten = r'<h1 class="yahei">(.*?)</h1>'
    projectIdPatten = r'<input id="task_id" value="(.*?)" type="hidden"/>'
    orangePatten = r'<span class="orange">(.*?)</span>'
    prodescPatten = re.compile(r'<div class="task_info_content yahei hidden">\s+<div>(.*?)</div>', re.S)

    keyWordResult = keyworkPatten.search(subContent)
    descResult = re.search( descriptionPatten,subContent)
    projectNameResult = re.search( projectNamePatten,subContent)
    projectIdResult = re.search( projectIdPatten,subContent)
    proDescResult = re.search( prodescPatten,subContent)
    priceResult = re.search( orangePatten,subContent)

    keyWord =  keyWordResult.groups()[0] if keyWordResult else ''
    descWord =  descResult.groups()[0] if descResult else ''
    projectName =  projectNameResult.groups()[0] if projectNameResult else ''
    projectId =  projectIdResult.groups()[0] if projectIdResult else ''
    price =  priceResult.groups()[0] if priceResult else ''
    proDesc =  proDescResult.groups()[0] if proDescResult else ''

    if(projectId):
        db.addOrUpdateProject(projectName,SOURCE_ZHUBAJIE,keyWord,descWord,proDesc,price,searchKey,projectId,'',url)

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


