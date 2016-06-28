__author__ = 'CQC'
# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import re
import webbrowser
import tool

#模拟登录淘宝类
class Taobao:

    #初始化方法
    def __init__(self):
        #登录的URL
        self.loginURL = "https://login.taobao.com/member/login.jhtml"
        #代理IP地址，防止自己的IP被封禁
        self.proxyURL = 'http://192.168.254.37:843'
        #登录POST数据时发送的头部信息
        self.loginHeaders =  {
            'Host':'login.taobao.com',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer' : 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive'
        }
        #用户名
        self.username = '18721150691'
        #ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua = '067#bxPmKDmxh+Pmo7hkmmmmmQTuo0q9f5qwbFl6o3hAz9mYAa4xmPLX9Zl2Mk7PZ+VkbQ75ordmzP4Sb0PO3OZvfQgr4IlPF9LhmhTRRIusXej2iOPoM9kQyOTBgheRmLmFmfm3+5tsJBqW0yyhkUTfDYqZA5mqWDQmP7PmZ9HHJIY5j8zcfferP8A29FXD+3im7hLhmhTRzkusXaSmePPoM9kQyOTBgheRmLmFmfm3+5tsJBqYQeHhkUTfDYqZA5mqWDQmP7PmZ9iJJIY5KlLUfferP8A29FXD+3im7hLhmhTRZ0usXawatlPoM9kQyOTBgheRmLh6mfmPcTarsflhmmDmhJL6sGnx8DjHI08bmfm8mm9S89OR8c8w79g0g7PmhPeoyzl7mfmwIfkl1kIWg7PmhPeoyzr6mfmPcTarsflhmhuJhAT6ld8x8D9rakJwe2enqW8wfK0qWZMR8FmhmmjomJcnXKDgmfmcuZQJD8Pti3I9ybGoZrGgjFcaEhDhmmlmTJ0m50IxUzGQmfmPmfZO/+Lhmm9ocjWyEDPmh7mhOnQxVulhmh/5TAz2UPrx/TnMsBZxgcP0DI2yYmPmhrh8LT3uKB4hmm7mmZd0mBP9rQuhmQ7mm+uRzImkmDmmR/xs8mQEmmhi1+uDhxlmm+0nzImms7mmRJ9s8mk6k7PmHfkemycDv+Wios8x8Rc5MEWSt2MIHGy7tGLagUG5HUcVbrMO8Rc5MEWStSxYv/3Xn6qUMSNs1Upt3F3J/vkiqRD5TIf5EillNr8IFQzsNc/Aq5qd8/0yKEtUHIhrHvTlNr8IFwBiv++vuvLxKNRNjJpC9aoxsErEuIKaK0+e1U0E3CgxKNRNKNr+tSxYv/3Xn0g+K0vyEIkEHEL58nQG8sb0T04sDKDeN5/CJck5tk+3xI4uj8WiKNxCH2qaxRx0G3MCqwRniW/yolqW3ocZjRV+h5T2EBO603LIo0cJBcJdLa9dzRGaqz5abSoxXEXEt3LIo0cJZDPmwreNEyPKfxLVLx6Ti4ujJwdSWMIa83ZjRaeq+mPmQfhfunQ1J/Z4OxDhmmlmTAImEkIxMefbmfm8mmTP8VLF8c8P4pT0g7PmhPeoyzlgmfmWtZkLD/ttiUjM9MQoblCTqkq5B18qMif7mfmT7Dkl1m48FlKhWn1AhXMl3Ghlul4bmfm8mmc/8bQF8c8PKQP0LmPmZL8hdJxaqPywD31J67KUMZR7MAbwLmPmhuOhdJ0WMflhmmDmhPm0sJ7x8DFLZI8Fmfm+Pf8sJBTiw6mhmmjomzcnzkubmfmUQ79g804a8c8wnjT0S8qHWwqykWwHxflhmmDmhJP6szlx8DjOek8Fmfm3+DtsJBq0/aXhkUTfDYqZA5mqWDQmP7PmZ9iRJIY5R0o2fferP8A29FXD+3im7+Lhmm9ocjWyP7PmZ9ivJIY5Mpc7fferP8A29FXD+3im7hLhmhTRZ0usXahB/OPoM9kQyOTBgheRmLmFmfm3+xgsJBqNq6ohkUTfDYqZA5mqWDQmP7PmZ9H5JIY5jnGKfferP8A29FXD+3im7mlhmhuJhAO6wVux8Dg8e0J4xabw4SOA9t+eTPqy4D==='
        #密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2 = '610c85da37069c430299b6e3358cbec3934b5dad83275f56370db62e3d6feb9b2eb857c7a37b999304459de08bdb1ab142118984d7b279f56872a44e8cf41393eaaee542aece456875a089505562c0123ce982567c03f324f2a58dc720d313db9f0c95ca2037681bb2c689399c64d62b04b2e1e1441298c5e565d369495cf8c7'
        self.post = post = {
            'TPL_username':"18721150691",
            'TPL_password':"",
            'ncoSig':"",
            'ncoSessionid':"",
            'ncoToken':"6b67f0f2b6e3d9bd71046780742305110231b8b9",
            'slideCodeShow':"false",
            'loginsite':"0",
            'newlogin':"0",
            'TPL_redirect_url':"https://www.taobao.com/",
            'from':"tb",
            'fc':"default",
            'style':"default",
            'css_style':"",
            'keyLogin':"false",
            'qrLogin':"true",
            'newMini':"false",
            'newMini2':"false"	,
            'tid':"",
            'loginType':"3",
            'minititle':"",
            'minipara':"",
            'pstrong':"",
            'sign':"",
            'need_sign':"",
            'isIgnore':"",
            'full_redirect':"",
            'popid':"",
            'callback':"",
            'guf':"",
            'not_duplite_str':"",
            'need_user_id':"",
            'poy':"",
            'gvfdcname':"10",
            'gvfdcre':"68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E35303836322E3735343839343433372E372E6F5830596C6326663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246",
            'from_encoding':"",
            'sub':"",
            'TPL_password_2':"610c85da37069c430299b6e3358cbec3934b5dad83275f56370db62e3d6feb9b2eb857c7a37b999304459de08bdb1ab142118984d7b279f56872a44e8cf41393eaaee542aece456875a089505562c0123ce982567c03f324f2a58dc720d313db9f0c95ca2037681bb2c689399c64d62b04b2e1e1441298c5e565d369495cf8c7",
            'loginASR':"1",
            'loginASRSuc':"1",
            'allp':"",
            'oslanguage':"zh-CN",
            'sr':"1680*1050",
            'osVer':"windows|6.1",
            'naviVer':"firefox|47",
            'miserHardInfo':"",
            'um_token':"HV01PAAZ0be3faae72507cee576ca6f800064808",
            'ua':"067#bxPmKDmxh+Pmo7hkmmmmmQTuo0q9f5qwbFl6o3hAz9mYAa4xmPLX9Zl2Mk7PZ+VkbQ75ordmzP4Sb0PO3OZvfQgr4IlPF9LhmhTRRIusXej2iOPoM9kQyOTBgheRmLmFmfm3+5tsJBqW0yyhkUTfDYqZA5mqWDQmP7PmZ9HHJIY5j8zcfferP8A29FXD+3im7hLhmhTRzkusXaSmePPoM9kQyOTBgheRmLmFmfm3+5tsJBqYQeHhkUTfDYqZA5mqWDQmP7PmZ9iJJIY5KlLUfferP8A29FXD+3im7hLhmhTRZ0usXawatlPoM9kQyOTBgheRmLh6mfmPcTarsflhmmDmhJL6sGnx8DjHI08bmfm8mm9S89OR8c8w79g0g7PmhPeoyzl7mfmwIfkl1kIWg7PmhPeoyzr6mfmPcTarsflhmhuJhAT6ld8x8D9rakJwe2enqW8wfK0qWZMR8FmhmmjomJcnXKDgmfmcuZQJD8Pti3I9ybGoZrGgjFcaEhDhmmlmTJ0m50IxUzGQmfmPmfZO/+Lhmm9ocjWyEDPmh7mhOnQxVulhmh/5TAz2UPrx/TnMsBZxgcP0DI2yYmPmhrh8LT3uKB4hmm7mmZd0mBP9rQuhmQ7mm+uRzImkmDmmR/xs8mQEmmhi1+uDhxlmm+0nzImms7mmRJ9s8mk6k7PmHfkemycDv+Wios8x8Rc5MEWSt2MIHGy7tGLagUG5HUcVbrMO8Rc5MEWStSxYv/3Xn6qUMSNs1Upt3F3J/vkiqRD5TIf5EillNr8IFQzsNc/Aq5qd8/0yKEtUHIhrHvTlNr8IFwBiv++vuvLxKNRNjJpC9aoxsErEuIKaK0+e1U0E3CgxKNRNKNr+tSxYv/3Xn0g+K0vyEIkEHEL58nQG8sb0T04sDKDeN5/CJck5tk+3xI4uj8WiKNxCH2qaxRx0G3MCqwRniW/yolqW3ocZjRV+h5T2EBO603LIo0cJBcJdLa9dzRGaqz5abSoxXEXEt3LIo0cJZDPmwreNEyPKfxLVLx6Ti4ujJwdSWMIa83ZjRaeq+mPmQfhfunQ1J/Z4OxDhmmlmTAImEkIxMefbmfm8mmTP8VLF8c8P4pT0g7PmhPeoyzlgmfmWtZkLD/ttiUjM9MQoblCTqkq5B18qMif7mfmT7Dkl1m48FlKhWn1AhXMl3Ghlul4bmfm8mmc/8bQF8c8PKQP0LmPmZL8hdJxaqPywD31J67KUMZR7MAbwLmPmhuOhdJ0WMflhmmDmhPm0sJ7x8DFLZI8Fmfm+Pf8sJBTiw6mhmmjomzcnzkubmfmUQ79g804a8c8wnjT0S8qHWwqykWwHxflhmmDmhJP6szlx8DjOek8Fmfm3+DtsJBq0/aXhkUTfDYqZA5mqWDQmP7PmZ9iRJIY5R0o2fferP8A29FXD+3im7+Lhmm9ocjWyP7PmZ9ivJIY5Mpc7fferP8A29FXD+3im7hLhmhTRZ0usXahB/OPoM9kQyOTBgheRmLmFmfm3+xgsJBqNq6ohkUTfDYqZA5mqWDQmP7PmZ9H5JIY5jnGKfferP8A29FXD+3im7mlhmhuJhAO6wVux8Dg8e0J4xabw4SOA9t+eTPqy4D==",
        }
        #将POST的数据进行编码转换
        self.postData = urllib.urlencode(self.post)
        #设置代理
        self.proxy = urllib2.ProxyHandler({'http':self.proxyURL})
        #设置cookie
        self.cookie = cookielib.LWPCookieJar()
        #设置cookie处理器
        self.cookieHandler = urllib2.HTTPCookieProcessor(self.cookie)
        #设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib2.build_opener(self.cookieHandler,urllib2.HTTPHandler)
        #赋值J_HToken
        self.J_HToken = ''
        #登录成功时，需要的Cookie
        self.newCookie = cookielib.CookieJar()
        #登陆成功时，需要的一个新的opener
        self.newOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.newCookie))
        #引入工具类
        self.tool = tool.Tool()

    #得到是否需要输入验证码，这次请求的相应有时会不同，有时需要验证有时不需要
    def needCheckCode(self):
        #第一次登录获取验证码尝试，构建request
        request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
        #得到第一次登录尝试的相应
        response = self.opener.open(request)
        #获取其中的内容
        content = response.read().decode('gbk')
        #print(content)
        #获取状态吗
        status = response.getcode()
        print(status)
        #状态码为200，获取成功
        if status == 200:
            print u"获取请求成功"
            #\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801这六个字是请输入验证码的utf-8编码
            pattern = re.compile(u'\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801',re.S)
            result = re.search(pattern,content)
            #如果找到该字符，代表需要输入验证码
            if result:
                print u"此次安全验证异常，您需要输入验证码"
                return content
            #否则不需要
            else:
                #返回结果直接带有J_HToken字样，表明直接验证通过
                tokenPattern = re.compile('id="J_HToken" value="(.*?)"')
                print(content)
                tokenMatch = re.search(tokenPattern,content)
                if tokenMatch:
                    self.J_HToken = tokenMatch.group(1)
                    print u"此次安全验证通过，您这次不需要输入验证码"
                    return False
        else:
            print u"获取请求失败"
            return None

    #得到验证码图片
    def getCheckCode(self,page):
        #得到验证码的图片
        pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"',re.S)
        #匹配的结果
        matchResult = re.search(pattern,page)
        #已经匹配得到内容，并且验证码图片链接不为空
        if matchResult and matchResult.group(1):
            return matchResult.group(1)
        else:
            print u"没有找到验证码内容"
            return False

    #输入验证码，重新请求，如果验证成功，则返回J_HToken
    def loginWithCheckCode(self):
        #提示用户输入验证码
        checkcode = raw_input('请输入验证码:')
        #将验证码重新添加到post的数据中
        self.post['TPL_checkcode'] = checkcode
        #对post数据重新进行编码
        self.postData = urllib.urlencode(self.post)
        try:
            #再次构建请求，加入验证码之后的第二次登录尝试
            request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
            #得到第一次登录尝试的相应
            response = self.opener.open(request)
            #获取其中的内容
            content = response.read().decode('gbk')
            #检测验证码错误的正则表达式，\u9a8c\u8bc1\u7801\u9519\u8bef 是验证码错误五个字的编码
            pattern = re.compile(u'\u9a8c\u8bc1\u7801\u9519\u8bef',re.S)
            result = re.search(pattern,content)
            #如果返回页面包括了，验证码错误五个字
            if result:
                print u"验证码输入错误"
                return False
            else:
                #返回结果直接带有J_HToken字样，说明验证码输入成功，成功跳转到了获取HToken的界面
                tokenPattern = re.compile('id="J_HToken" value="(.*?)"')
                tokenMatch = re.search(tokenPattern,content)
                #如果匹配成功，找到了J_HToken
                if tokenMatch:
                    print u"验证码输入正确"
                    self.J_HToken = tokenMatch.group(1)
                    return tokenMatch.group(1)
                else:
                    #匹配失败，J_Token获取失败
                    print u"J_Token获取失败"
                    return False
        except urllib2.HTTPError, e:
            print u"连接服务器出错，错误原因",e.reason
            return False

    #通过token获得st
    def getSTbyToken(self,token):
        tokenURL = 'https://passport.alipay.com/mini_apply_st.js?site=0&token=%s&callback=stCallback6' % token
        request = urllib2.Request(tokenURL)
        response = urllib2.urlopen(request)
        #处理st，获得用户淘宝主页的登录地址
        pattern = re.compile('{"st":"(.*?)"}',re.S)
        result = re.search(pattern,response.read())
        #如果成功匹配
        if result:
            print u"成功获取st码"
            #获取st的值
            st = result.group(1)
            return st
        else:
            print u"未匹配到st"
            return False

    #利用st码进行登录,获取重定向网址
    def loginByST(self,st,username):
        stURL = 'https://login.taobao.com/member/vst.htm?st=%s&TPL_username=%s' % (st,username)
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Host':'login.taobao.com',
            'Connection' : 'Keep-Alive'
        }
        request = urllib2.Request(stURL,headers = headers)
        response = self.newOpener.open(request)
        content =  response.read().decode('gbk')
        #检测结果，看是否登录成功
        pattern = re.compile('top.location = "(.*?)"',re.S)
        match = re.search(pattern,content)
        if match:
            print u"登录网址成功"
            location = match.group(1)
            return True
        else:
            print "登录失败"
            return False

    #获得已买到的宝贝页面
    def getGoodsPage(self,pageIndex):
        goodsURL = 'http://buyer.trade.taobao.com/trade/itemlist/listBoughtItems.htm?action=itemlist/QueryAction&event_submit_do_query=1' + '&pageNum=' + str(pageIndex)
        response = self.newOpener.open(goodsURL)
        page =  response.read().decode('gbk')
        return page

    #获取所有已买到的宝贝信息
    def getAllGoods(self,pageNum):
        print u"获取到的商品列表如下"
        for x in range(1,int(pageNum)+1):
            page = self.getGoodsPage(x)
            self.tool.getGoodsInfo(page)

    #程序运行主干
    def main(self):
        #是否需要验证码，是则得到页面内容，不是则返回False
        needResult = self.needCheckCode()
        #请求获取失败，得到的结果是None
        if not needResult ==None:
            if not needResult == False:
                print u"您需要手动输入验证码"
                checkCode = self.getCheckCode(needResult)
                #得到了验证码的链接
                if not checkCode == False:
                    print u"验证码获取成功"
                    print u"请在浏览器中输入您看到的验证码"
                    webbrowser.open_new_tab(checkCode)
                    self.loginWithCheckCode()
                #验证码链接为空，无效验证码
                else:
                    print u"验证码获取失败，请重试"
            else:
                print u"不需要输入验证码"
        else:
            print u"请求登录页面失败，无法确认是否需要验证码"

        #判断token是否正常获取到
        if not self.J_HToken:
            print "获取Token失败，请重试"
            return
        #获取st码
        st = self.getSTbyToken(self.J_HToken)
        #利用st进行登录
        result = self.loginByST(st,self.username)
        if result:
            #获得所有宝贝的页面
            page = self.getGoodsPage(1)
            pageNum = self.tool.getPageNum(page)
            self.getAllGoods(pageNum)
        else:
            print u"登录失败"

taobao = Taobao()
taobao.main()